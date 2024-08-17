from datetime import datetime, timedelta, timezone
import re
import time
from typing import Dict, List, Optional, Tuple
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class YoutubeAPI:
    def __init__(self, api_key: str, channel_id: str) -> None:
        """
        Initialize the YoutubeAPI class.

        Args:
            api_key (str): The API key for accessing the YouTube Data API.
            channel_id (str): The ID of the YouTube channel.
        """
        self.CHANNEL_ID = channel_id
        self.api_key = api_key
        self.youtube = build("youtube", "v3", developerKey=self.api_key)
        self.DEFAULT_IMAGE_URL = "https://via.placeholder.com/400?text=No+Image+Found"
        self.video_ids: List[str] = []
        self.video_counts: int = 0
        self.published_at = None

    def channel_life_spans(self, timestamp: str) -> str:
        """
        Parse the input timestamp string and calculate the time span in days, hours, minutes, and seconds.

        Parameters:
            timestamp (str): The input timestamp string to parse.

        Returns:
            str: A formatted string representing the time span in days, hours, minutes, and seconds.
        """

        # Parse the input timestamp string
        try:
            if "." in timestamp:
                # Milliseconds present, use full format string
                input_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
            else:
                # Milliseconds missing, use format string without milliseconds
                input_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
            # Use datetime_obj for further processing
        except ValueError:
            print("Error parsing timestamp:", timestamp)
        # input_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        input_time = input_time.replace(tzinfo=timezone.utc)

        # Get the current time in UTC
        current_time = datetime.now(timezone.utc)

        # Calculate the time difference
        time_difference = current_time - input_time
        total_seconds = int(time_difference.total_seconds())

        # Calculate days, hours, minutes, and seconds
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the time span
        life_span = (
            f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds"
        )

        return life_span, total_seconds

    def convert_seconds_to_time(self, total_seconds: int) -> Tuple[int, int, int, int]:
        """
        Convert total seconds to days, hours, minutes and seconds.

        Args:
            total_seconds (int): Total number of seconds to convert.

        Returns:
            Tuple[int, int, int, int]: A tuple containing the number of days, hours, minutes and seconds.
        """

        delta = timedelta(seconds=total_seconds)

        days, remainder = divmod(delta.total_seconds(), 86400)  # 86400 seconds in a day
        hours, remainder = divmod(remainder, 3600)  # 3600 seconds in an hour
        minutes, seconds = divmod(remainder, 60)  # 60 seconds in a minute

        return int(days), int(hours), int(minutes), int(seconds)

    def seconds_to_formatted_time(self, seconds: int) -> str:
        """
        Converts seconds into a formatted string using timedelta (HH:MM:SS.ssssss).

        Args:
            seconds (int): The number of seconds to convert.

        Returns:
            str: The formatted time string in the format HH:MM:SS.
        """
        """Converts seconds into a formatted string using timedelta (HH:MM:SS.ssssss)."""
        time_delta = timedelta(seconds=seconds)
        formatted_time = str(time_delta).split(".")[0]  # Extract HH:MM:SS portion
        return formatted_time

    def parse_youtube_video_duration(
        self, duration_str: str
    ) -> Tuple[Optional[Dict[str, int]], int]:
        """
        Parse the YouTube video duration string and return the duration as a dictionary and the total number of seconds.

        Args:
            duration_str (str): The YouTube video duration string.

        Returns:
            Tuple[Optional[Dict[str, int]], int]: A tuple containing the duration as a dictionary and the total number of seconds.
                - The duration dictionary contains keys 'hours', 'minutes', and 'seconds' with integer values.
                - The total number of seconds as an integer.
        """

        # Define a regular expression pattern to match the duration format
        pattern = r"PT((?P<hours>\d+)H)?((?P<minutes>\d+)M)?((?P<seconds>\d+)S)?"

        # Use the re.match function to match the pattern in the duration string
        match = re.match(pattern, duration_str)

        # If a match is found
        if match:
            # Get the matched groups as a dictionary
            duration_dict = match.groupdict()

            # Convert the values in the dictionary to integers
            for key in duration_dict:
                if duration_dict[key] is not None:
                    duration_dict[key] = int(duration_dict[key])
                if duration_dict[key] == None:
                    duration_dict[key] = 0
            seconds = (
                int(duration_dict["hours"]) * 3600
                + int(duration_dict["minutes"]) * 60
                + int(duration_dict["seconds"])
            )
            return duration_dict, seconds
        else:
            return None, 0

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
        self.video_counts = self.response["items"][0]["statistics"]["videoCount"]
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
            # "channel_name": self.response["items"][0]["snippet"]["title"],
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
        self.published_at = self.response["items"][0]["snippet"]["publishedAt"]
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
            # print(len(self.video_ids), len(self.video_ids) < int(self.video_counts))
            # checking if the total videos lis is less than the video count
            if len(self.video_ids) < int(self.video_counts):
                self.video_ids.extend(
                    [item["contentDetails"]["videoId"] for item in response["items"]]
                )
            else:
                return self.video_ids

            request = self.youtube.playlistItems().list_next(request, response)
            # print(response)
            time.sleep(1)  # Add a delay to avoid hitting rate limits

        return self.video_ids

    def get_videos_statistics(self):
        # print(self.video_ids)

        self.video_details = []
        video_count = 0
        view_count = 0
        like_count = 0
        comment_count = 0
        total_seconds = 0
        for i in range(0, len(self.video_ids), 50):  # Process in batches of 50
            request = self.youtube.videos().list(
                part="contentDetails,statistics, snippet",
                id=",".join(self.video_ids[i : i + 50]),
            )
            response = request.execute()
            # print(response)
            for item in response["items"]:
                self.video_stats = {
                    "videoId": item["id"],
                    "duration": item["contentDetails"].get("duration", "N/A"),
                    "viewCount": int(item["statistics"].get("viewCount", 0)),
                    "likeCount": int(item["statistics"].get("likeCount", 0)),
                    "commentCount": int(item["statistics"].get("commentCount", 0)),
                    "title": item["snippet"].get("title", "N/A"),
                }
                video_count += 1
                view_count += int(item["statistics"].get("viewCount", 0))
                like_count += int(item["statistics"].get("likeCount", 0))
                comment_count += int(item["statistics"].get("commentCount", 0))

                video_duration, video_duration_seconds = (
                    self.parse_youtube_video_duration(
                        item["contentDetails"].get("duration", "N/A")
                    )
                )
                total_seconds += video_duration_seconds
                # /# duration += int(item["contentDetails"].get("duration", 0))
                self.video_details.append(self.video_stats)

        channel_statistics = {
            "video_count": video_count,
            "view_count": view_count,
            "like_count": like_count,
            "comment_count": comment_count,
            "total_seconds": total_seconds,
            "channel_duration": self.seconds_to_formatted_time(total_seconds),
        }
        return self.video_details, channel_statistics

    def get_most_popular_videos(self, number_of_videos=4):
        self.popular_videos_urls = []
        self.popular_videos = sorted(
            self.video_details, key=lambda x: x["viewCount"], reverse=True
        )
        for video in self.popular_videos[0:number_of_videos]:
            # print(video)
            video_link = f"https://www.youtube.com/embed/{video['videoId']}"
            video_duration_formatted, video_duration_seconds = (
                self.parse_youtube_video_duration(video["duration"])
            )
            hours, minutes, seconds = (
                video_duration_formatted["hours"],
                video_duration_formatted["minutes"],
                video_duration_formatted["seconds"],
            )
            video_inf = {
                "url": video_link,
                "title": video["title"],
                "viewCount": video["viewCount"],
                "likeCount": video["likeCount"],
                "commentCount": video["commentCount"],
                "duration": f"{hours}:{minutes}:{seconds}",
            }

            self.popular_videos_urls.append(video_inf)
        return self.popular_videos_urls

    def recent_videos_links(self, number_of_videos=4):
        recent_videos = []
        for video in self.video_details[0:number_of_videos]:
            video_link = f"https://www.youtube.com/embed/{video['videoId']}"
            video_duration_formated, video_duration_seconds = (
                self.parse_youtube_video_duration(video["duration"])
            )
            hours, minutes, seconds = (
                video_duration_formated["hours"],
                video_duration_formated["minutes"],
                video_duration_formated["seconds"],
            )
            video_inf = {
                "url": video_link,
                "title": video["title"],
                "viewCount": video["viewCount"],
                "likeCount": video["likeCount"],
                "commentCount": video["commentCount"],
                "duration": f"{hours}:{minutes}:{seconds}",
            }

            recent_videos.append(video_inf)

        return recent_videos

    def calculate_content_gap(self):
        # Convert published_at to datetime if it is not already
        if isinstance(self.published_at, str):
            timestamp = datetime.strptime(self.published_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            timestamp = self.published_at
        print(self.published_at)
        # Get the current time (in UTC)
        now = datetime.utcnow()

        # Calculate the time difference
        time_difference = now - timestamp

        # Calculate the total time difference in seconds
        total_seconds = time_difference.total_seconds()

        # Calculate gap in seconds per video (if needed)
        gap_in_seconds = (
            total_seconds / int(self.video_counts) if int(self.video_counts) > 0 else 0
        )

        # Convert total_seconds back to days, hours, minutes, and seconds
        days = int(gap_in_seconds // 86400)  # 86400 seconds in a day
        hours = int((gap_in_seconds % 86400) // 3600)  # 3600 seconds in an hour
        minutes = int((gap_in_seconds % 3600) // 60)  # 60 seconds in a minute
        seconds = int(gap_in_seconds % 60)  # remaining seconds

        # Format the result as a string
        formatted_gap = f"{days} days {hours}:{minutes}:{seconds}"

        return formatted_gap
