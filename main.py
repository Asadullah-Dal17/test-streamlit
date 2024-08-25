import streamlit as st
import youtubeAPI

st.set_page_config(page_title="Portfolio", page_icon=":home:", layout="wide")

youtube_api_key = st.secrets["YOUTUBE_API_KEY"]
yt_api = youtubeAPI.YoutubeAPI(
    api_key=youtube_api_key, channel_id="UCc8Lx22a5OX4XMxrCykzjbA"
)
yt_api.get_response_from_youtube_api()


def load_css(file_path):
    """Loads CSS from a specified file and injects it into the Streamlit app.

    Args:
      file_path: The path to the CSS file.

    Returns:
      None
    """

    with open(file_path, "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


html_code = """
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap" rel="stylesheet">


    </head>

    <div class="whole_cover">
        <div class="container">
            <div class="profile">
                <div class="profile-image">
                    <img src="https://github.com/user-attachments/assets/8acee0eb-2fe1-49b8-a007-56fdebeb5a9f"
                        alt="Profile Image">
                </div>
                <div class="profile-details">
                    <h2>Asadullah Dal</h2>
                    <p> Computer Vision Developer</p>
                    <p>Educator, YouTuber & Freelancer</p>
                    <div class="social-media">
                        <a href="https://www.youtube.com/c/aiphile" target="_blank" title="YouTube">
                            <i class="fab fa-youtube"></i>
                        </a>
                        <a href="https://www.linkedin.com/in/asadullah-dal/" target="_blank" title="LinkedIn">
                            <i class="fab fa-linkedin"></i>
                        </a>
                        <a href="https://github.com/asadullah-dal17" target="_blank" title="GitHub">
                            <i class="fab fa-github"></i>
                        </a>
                        <a href="https://www.instagram.com/aiphile" target="_blank" title="Instagram">
                            <i class="fab fa-instagram"></i>
                        </a>
                    </div>
                </div>
            </div>
            <div class="introduction">
                <h1>Welcome to My Portfolio</h1>
                <p>I’m a <strong>Computer Vision Developer 📷 </strong> with over five years of experience. Since 2019,
                    I’ve
                    been crafting innovative AI solutions. 💻 I also run a YouTube channel, <strong>AiPhile</strong>
                    🎥,
                    where I share tutorials on computer vision. Looking for expert <strong>freelance services</strong>?
                    Let’s bring
                    your vision to
                    life!
                    🚀</p>
            </div>
        </div>
    </div>
    <div class="whole_cover">
        <section class="skills">
            <h2>Skills</h2>
            <div class="container-skills">
                <div class="skill">
                    <div class="skill-name">Progrmming</div>
                    <div class="progress-bar">
                        <div class="progress" style="width: 90%;">90%</div>
                    </div>
                </div>
                <div class="skill">
                    <div class="skill-name">Computer Vision</div>
                    <div class="progress-bar">
                        <div class="progress" style="width: 85%;">85%</div>
                    </div>
                </div>
                <div class="skill">
                    <div class="skill-name">Machine Learning</div>
                    <div class="progress-bar">
                        <div class="progress" style="width: 80%;">80%</div>
                    </div>
                </div>
                <div class="skill">
                    <div class="skill-name">Teaching</div>
                    <div class="progress-bar">
                        <div class="progress" style="width: 75%;">75%
                        </div>
                    </div>
                </div>
                <div class="skill">
                    <div class="skill-name">Git & GitHub</div>
                    <div class="progress-bar">
                        <div class="progress" style="width: 65%;">65%

                        </div>
                    </div>
                </div>
        </section>
    </div>
    """
st.html(html_code)


def cards():

    html_string = """
    <!-- Project Card Section -->
    <div class="whole_cover">
        <section class="warp">
            <div class="title-container">
                <h2 class="section-title">Projects</h2>
            </div>
            <div class="cards-container">
                <div class="box">
                    <div class="imgbox">
                        <img src="https://github.com/user-attachments/assets/d746d160-c4e2-4f33-8fcc-d61233eadacd"
                            alt="">
                    </div>
                    <div class="content">
                        <h2>Eyes Tracking</h2>
                        <div class="text">Implemented a real-time eye-tracking system leveraging computer vision and
                            Mediapipe's facial landmark detection. Developed algorithms for accurate eye region
                            extraction
                            and position estimation. Demonstrated proficiency in image processing, machine learning, and
                            real-time system development</div>
                        <a href="https://github.com/Asadullah-Dal17/Eyes-Position-Estimator-Mediapipe">More</a>
                    </div>
                </div>
                <div class="box">
                    <div class="imgbox">
                        <img src="https://github.com/user-attachments/assets/b7ce39c0-9e66-4ed6-b4c2-5378390fed1a"
                            alt="">
                    </div>
                    <div class="content">
                        <h2>Interactive 3D Image Display</h2>
                        <div class="text">A project that merges the digital and physical realms, bringing 2D images to
                            life
                            in 3D space through the use of Aruco markers and OpenCV. This interactive experience allows
                            users to witness the illusion of a floating image, creating a captivating and immersive
                            display.</div>
                        <a href="#">More</a>
                    </div>
                </div>
                <div class="box">
                    <div class="imgbox">
                        <img src="https://github.com/user-attachments/assets/4ee98e11-532b-47c0-97ba-414a71ef3f2b"
                            alt="">
                    </div>
                    <div class="content">
                        <h2>Face-Following Robot</h2>
                        <div class="text">Developed a face-following robotic system integrating computer vision and
                            Arduino-based control. The project involved real-time face detection, tracking, and distance
                            estimation to enable autonomous navigation and object following.</div>
                        <a
                            href="https://github.com/Asadullah-Dal17/Face-Following-Robot-using-Distance-Estimation">More</a>
                    </div>
                </div>
                <div class="box">
                    <div class="imgbox">
                        <img src="https://github.com/user-attachments/assets/57182f93-7b1c-486f-bdc3-837e9072f59f"
                            alt="">
                    </div>
                    <div class="content">
                        <h2>Face to Screen Time</h2>
                        <div class="text">This project employs computer vision techniques to accurately calculate face
                            time
                            and session duration. By utilizing Mediapipe's robust face detection model, the system
                            effectively tracks facial presence within a video stream, providing quantitative metrics for
                            screen time analysis.</div>
                        <a
                            href="https://github.com/Asadullah-Dal17/AiPhile-Mediapipe-Course/tree/master/FACE_DETECTION/Face-Time">More</a>
                    </div>
                </div>
            </div>
        </section>
    </div>

    """
    st.html(html_string)


def to_ks(num):
    return num / 1000


def most_popular_videos():
    most_popular_videos_list = yt_api.get_most_popular_videos()

    html_most_popular = f"""
    <div class="whole_cover">
        <section class="section">
            <div class="section-title">Most Popular Videos</div>
            <div class="stats-container">
                <div class="video-item">
                    <div class="video-embed">
                        <iframe src={most_popular_videos_list[0]['url']} allowfullscreen></iframe>
                    </div>
                    <div class="video-title">{most_popular_videos_list[0]['title']}</div>
                    <div class="video-stats">
                        <div class="stat">
                            <i class="fas fa-eye stat-icon"></i>
                            <span>{most_popular_videos_list[0]['viewCount']}</span>
                        </div>
                        <div class="stat">
                            <i class="fas fa-thumbs-up stat-icon"></i>
                            <span>{most_popular_videos_list[0]['likeCount']}</span>
                        </div>
                        <div class="stat">
                            <i class="fas fa-comments stat-icon"></i>
                            <span>{most_popular_videos_list[0]['commentCount']}</span>
                        </div>
                    </div>
                </div>
                <div class="video-item">
                    <div class="video-embed">
                        <iframe src={most_popular_videos_list[1]['url']} allowfullscreen></iframe>
                    </div>
                    <div class="video-title">{most_popular_videos_list[1]['title']}</div>
                    <div class="video-stats">
                        <div class="stat">
                            <i class="fas fa-eye stat-icon"></i>
                            <span>{most_popular_videos_list[1]['viewCount']}</span>
                        </div>
                        <div class="stat">
                            <i class="fas fa-thumbs-up stat-icon"></i>
                            <span>{most_popular_videos_list[1]['likeCount']}</span>
                        </div>
                        <div class="stat">
                            <i class="fas fa-comments stat-icon"></i>
                            <span>{most_popular_videos_list[1]['commentCount']}</span>
                        </div>
                    </div>
                </div>
                <div class="video-item">
                    <div class="video-embed">
                        <iframe src={most_popular_videos_list[2]['url']} allowfullscreen></iframe>
                    </div>
                    <div class="video-title">{most_popular_videos_list[2]['title']}</div>
                    <div class="video-stats">
                        <div class="stat">
                            <i class="fas fa-eye stat-icon"></i>
                            <span>{most_popular_videos_list[2]['viewCount']}</span>
                        </div>
                        <div class="stat">
                            <i class="fas fa-thumbs-up stat-icon"></i>
                            <span>{most_popular_videos_list[2]['likeCount']}</span>
                        </div>
                        <div class="stat">
                            <i class="fas fa-comments stat-icon"></i>
                            <span>{most_popular_videos_list[2]['commentCount']}</span>
                        </div>
                    </div>
                </div>
                <div class="video-item">
                    <div class="video-embed">
                        <iframe src={most_popular_videos_list[3]['url']} allowfullscreen></iframe>
                    </div>
                    <div class="video-title">{most_popular_videos_list[3]['title']}</div>
                    <div class="video-stats">
                        <div class="stat">
                            <i class="fas fa-eye stat-icon"></i>
                            <span>{most_popular_videos_list[3]['viewCount']}</span>
                        </div>
                        <div class="stat">
                            <i class="fas fa-thumbs-up stat-icon"></i>
                            <span>{most_popular_videos_list[3]['likeCount']}</span>
                        </div>
                        <div class="stat">
                            <i class="fas fa-comments stat-icon"></i>
                            <span>{most_popular_videos_list[3]['commentCount']}</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div> 
    <div class="whole_cover">
        <div class="section">
            <h1 class="section-title">Github Stats</h1>
            <div class="git_stats">
                <img src="https://streak-stats.demolab.com?user=Asadullah-Dal17&theme=transparent&border_radius=6"
                    alt="" class="git_stats_image">
                <img src="https://github-readme-stats.vercel.app/api?username=Asadullah-Dal17&show_icons=true&theme=transparent&border_radius=6"
                    alt="" class="git_stats_image">
            </div>
        </div>
    </div>
    """
    st.markdown(html_most_popular, unsafe_allow_html=True)


def recently_uploaded_videos(recent_uploads_list):
    html_recent_upload_videos = f"""
        <!-- Recent Videos Section -->
        <div class="whole_cover">
            <section class="section">
                <div class="section-title">Recent Videos</div>
                <div class="stats-container">
                    <div class="video-item">
                        <div class="video-embed">
                            <iframe src={recent_uploads_list[0]["url"]} allowfullscreen></iframe>
                        </div>
                        <div class="video-title">{recent_uploads_list[0]["title"]}</div>
                        <div class="video-stats">
                            <div class="stat">
                                <i class="fas fa-eye stat-icon"></i>
                                <span>{recent_uploads_list[0]["viewCount"]}</span>
                            </div>
                            <div class="stat">
                                <i class="fas fa-thumbs-up stat-icon"></i>
                                <span>{recent_uploads_list[0]["likeCount"]}</span>
                            </div>
                            <div class="stat">
                                <i class="fas fa-comments stat-icon"></i>
                                <span>{recent_uploads_list[0]["commentCount"]}</span>
                            </div>
                        </div>
                    </div>
                    <div class="video-item">
                        <div class="video-embed">
                            <iframe src={recent_uploads_list[1]['url']} allowfullscreen></iframe>
                        </div>
                        <div class="video-title">{recent_uploads_list[1]['title']}</div>
                        <div class="video-stats">
                            <div class="stat">
                                <i class="fas fa-eye stat-icon"></i>
                                <span>{recent_uploads_list[1]['viewCount']}</span>
                            </div>
                            <div class="stat">
                                <i class="fas fa-thumbs-up stat-icon"></i>
                                <span>{recent_uploads_list[1]['likeCount']}</span>
                            </div>
                            <div class="stat">
                                <i class="fas fa-comments stat-icon"></i>
                                <span>{recent_uploads_list[1]['commentCount']}</span>
                            </div>
                        </div>
                    </div>
                    <div class="video-item">
                        <div class="video-embed">
                            <iframe src={recent_uploads_list[2]['url']} allowfullscreen></iframe>
                        </div>
                        <div class="video-title">{recent_uploads_list[2]['title']}</div>
                        <div class="video-stats">
                            <div class="stat">
                                <i class="fas fa-eye stat-icon"></i>
                                <span>{recent_uploads_list[2]['viewCount']}</span>
                            </div>
                            <div class="stat">
                                <i class="fas fa-thumbs-up stat-icon"></i>
                                <span>{recent_uploads_list[2]['likeCount']}</span>
                            </div>
                            <div class="stat">
                                <i class="fas fa-comments stat-icon"></i>
                                <span>{recent_uploads_list[2]['commentCount']}</span>
                            </div>
                        </div>
                    </div>
                    <div class="video-item">
                        <div class="video-embed">
                            <iframe src={recent_uploads_list[3]['url']} allowfullscreen></iframe>
                        </div>
                        <div class="video-title">{recent_uploads_list[3]['title']}</div>
                        <div class="video-stats">
                            <div class="stat">
                                <i class="fas fa-eye stat-icon"></i>
                                <span>{recent_uploads_list[3]['viewCount']}</span>
                            </div>
                            <div class="stat">
                                <i class="fas fa-thumbs-up stat-icon"></i>
                                <span>{recent_uploads_list[3]['likeCount']}</span>
                            </div>
                            <div class="stat">
                                <i class="fas fa-comments stat-icon"></i>
                                <span>{recent_uploads_list[3]['commentCount']}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    """

    st.markdown(html_recent_upload_videos, unsafe_allow_html=True)


def display_youtube_channel_stats(
    subscriber,
    videos,
    views,
    likes,
    comments,
    channel_duration,
):
    # Ensure numeric values are correctly typed
    subscriber = int(subscriber)
    videos = int(videos)
    views = float(views)
    likes = int(likes)
    comments = int(comments)
    # channel_duration = str(channel_duration)  # Assuming channel_duration is already a string

    # Guard against zero division for averages
    average_likes = f"{(likes / videos):.2f}" if videos > 0 else "N/A"
    average_comments = f"{(comments / videos):.2f}" if videos > 0 else "N/A"
    channel_basic_info = yt_api.basic_information()
    content_gap = yt_api.calculate_content_gap()

    html_channel_stats = f"""

    <div class="whole_cover">
        <!-- Youtube Stats Section -->
        <section class="section">
            <div class="section-title">YouTube Stats</div>
            <div class="stats-container">
                <div class="stat-item">
                    <i class="fas fa-users stat-icon"></i>
                    <div class="stat-value">{subscriber}</div>
                    <div class="stat-label">Total Subscribers</div>
                </div>
                <div class="stat-item">
                    <i class="fas fa-video stat-icon"></i>
                    <div class="stat-value">{videos}</div>
                    <div class="stat-label">Total Videos</div>
                </div>
                <div class="stat-item">
                    <i class="fas fa-eye stat-icon"></i>
                    <div class="stat-value">{to_ks(views):.2f}K</div>
                    <div class="stat-label">Total Views</div>
                </div>
                <div class="stat-item">
                    <i class="fas fa-thumbs-up stat-icon"></i>
                    <div class="stat-value">{to_ks(likes)}K</div>
                    <div class="stat-label">Total Likes</div>
                </div>
                <div class="stat-item">
                    <i class="fas fa-comments stat-icon"></i>
                    <div class="stat-value">{comments}</div>
                    <div class="stat-label">Total Comments</div>
                </div>
                <div class="stat-item">
                    <i class="fas fa-clock stat-icon"></i>
                    <div class="stat-value">{channel_duration}</div>
                    <div class="stat-label">Total Content Duration</div>
                </div>
                <div class="stat-item">
                    <i class="fas fa-calendar-alt stat-icon"></i>
                    <div class="stat-value">{content_gap}</div>
                    <div class="stat-label">Content Gap</div>
                </div>
                <div class="stat-item">
                    <i class="fas fa-thumbs-up stat-icon"></i>
                    <div class="stat-value">{average_likes}</div>
                    <div class="stat-label">Average Likes</div>
                </div>
                <div class="stat-item">
                    <i class="fas fa-comments stat-icon"></i>
                    <div class="stat-value">{average_comments}</div>
                    <div class="stat-label">Average Comments</div>
                </div>
            </div>
        </section>
    </div>
 
 
"""

    st.markdown(html_channel_stats, unsafe_allow_html=True)


def youtube_data_display():
    total_videos, total_subscribers, total_views = (
        yt_api.get_basic_statics()["video_count"],
        yt_api.get_basic_statics()["subscriber_count"],
        yt_api.get_basic_statics()["view_count"],
    )

    # total_views_k = to_ks(total_views)

    yt_api.get_all_video_ids_from_playlist()
    _, channel_stats = yt_api.get_videos_statistics()
    total_views = channel_stats["view_count"]
    likes = channel_stats["like_count"]
    comments = channel_stats["comment_count"]
    channel_duration = channel_stats["channel_duration"]
    total_videos = channel_stats["video_count"]
    content_duration_seconds = channel_stats["total_seconds"]

    # Get recents videos
    recent_videos = yt_api.recent_videos_links()
    # recent_videos[0]['url']
    display_youtube_channel_stats(
        subscriber=total_subscribers,
        views=total_views,
        videos=total_videos,
        likes=likes,
        comments=comments,
        channel_duration=channel_duration,
    )
    recently_uploaded_videos(recent_videos)
    most_popular_videos()


def contact():
    contact_html = """
    <div class="whole_cover">
        <div class="section">
             <div class="section-title">Contact</div>
            <div class="contact">
                <h3 class="email">asadullah92c@gmail.com</h3>
            </div>
        </div>
    </div>
    """
    st.markdown(contact_html, unsafe_allow_html=True)


def main():

    load_css("style_st.css")
    cards()
    youtube_data_display()
    contact()


if __name__ == "__main__":
    main()
