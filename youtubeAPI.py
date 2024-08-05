from datetime import datetime, timedelta, timezone
import re
import time
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class YoutubeAPI:
    def __init__(self, api_key, channel_id):
        self.CHANNEL_ID = channel_id
        self.api_key = api_key
        self.youtube = build("youtube", "v3", developerKey=self.api_key)
        self.DEFAULT_IMAGE_URL = "https://via.placeholder.com/400?text=No+Image+Found"
        self.video_ids = []

    def get_response_from_youtube_api(self):
        request = self.youtube.channels().list(
            part="snippet, contentDetails,brandingSettings, statistics ",
            id=self.CHANNEL_ID,
        )
        self.response = request.execute()
        return self.response

    def get_basic_statics(self):
        # st.write(self.response)
        self.basics_statics = dict(
            subscriber_count=self.response["items"][0]["statistics"]["subscriberCount"],
            view_count=self.response["items"][0]["statistics"]["viewCount"],
            video_count=self.response["items"][0]["statistics"]["videoCount"],
        )
        self.playlist_id = self.response["items"][0]["contentDetails"][
            "relatedPlaylists"
        ]["uploads"]
        return self.basics_statics

    def get_channel_images(self):
        try:
            logo = self.response["items"][0]["snippet"]["thumbnails"]["high"].get("url")
        except KeyError:
            st.warning("No logo found for this channel.")
            logo = None
        if logo == None:
            logo = self.DEFAULT_IMAGE_URL
        try:
            banner = (
                self.response["items"][0]["brandingSettings"]
                .get("image", {})
                .get("bannerExternalUrl")
            )
        except KeyError:
            st.warning("No banner found for this channel.")
            banner = None
        if banner == None:
            banner = self.DEFAULT_IMAGE_URL
        # st.write(banner)
        self.channel_images = dict(
            logo=logo,
            banner=banner,
        )

        # print(self.response["items"][0]["brandingSettings"])
        return self.channel_images

    def basic_information(self):
        channel_details = {
            "channel_name": self.response["items"][0]["snippet"]["title"],
            "description": self.response["items"][0]["snippet"]["description"],
            "youtube_handel": self.response["items"][0]["snippet"].get(
                "customUrl"
            ),  # Use get for customUrl (optional)
            "channel_id": self.response["items"][0]["id"],
            "country": (
                None
                if "country" not in self.response["items"][0]["snippet"]
                else self.response["items"][0]["snippet"]["country"]
            ),
            "published_at": self.response["items"][0]["snippet"]["publishedAt"],
        }
        return channel_details

    def get_all_video_ids_from_playlist(self, max_results_per_request=50):
        # self.video_ids = []
        request = self.youtube.playlistItems().list(
            part="contentDetails, snippet",  # Only request the contentDetails part
            playlistId=self.playlist_id,
            maxResults=max_results_per_request,
        )

        while request:
            response = request.execute()
            self.video_ids.extend(
                [item["contentDetails"]["videoId"] for item in response["items"]]
            )
            request = self.youtube.playlistItems().list_next(request, response)
            # print(response)
            time.sleep(1)  # Add a delay to avoid hitting rate limits

        return self.video_ids
