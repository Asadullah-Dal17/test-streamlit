import streamlit as st

st.set_page_config(layout="wide")


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
    </head>
    <div class="container">
        <div class="profile">
            <div class="profile-image">
                <img src="https://github.com/user-attachments/assets/8acee0eb-2fe1-49b8-a007-56fdebeb5a9f" alt="Profile Image">
            </div>
            <div class="profile-details">
                <h2>Asadullah Dal</h2>
                <p>Educator, YouTuber, Freelancer</p>
                <p>Computer Vision & Robotics Specialist</p>
                <div class="social-media">
                    <a href="https://twitter.com/yourprofile" target="_blank"><i class="fab fa-twitter"></i></a>
                    <a href="https://github.com/yourprofile" target="_blank"><i class="fab fa-github"></i></a>
                    <a href="https://linkedin.com/in/yourprofile" target="_blank"><i class="fab fa-linkedin"></i></a>
                </div>
            </div>
        </div>
        <div class="introduction">
            <h1>Welcome to My Portfolio</h1>
            <p>Hi! I'm Asadullah Dal, an educator, YouTuber, and freelancer specializing in Computer Vision and
                Robotics. Explore my projects and skills, and feel free to reach out!</p>
            <button class="view-more">View More</button>
        </div>
    </div>

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

    """
st.html(html_code)


def cards():

    html_string = """
        <section class="warp">
        <div class="title-container">
            <h2 class="section-title">Projects</h2>
        </div>
        <div class="cards-container">
            <div class="box">
                <div class="imgbox">
                    <img src="https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg?auto=compress&cs=tinysrgb&w=600" alt="">
                </div>
                <div class="content">
                    <h2>Floating Image Viewer</h2>
                    <div class="text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut iste qui, quibusdam, voluptatibus quas ipsa architecto aliquid maxime itaque a impedit harum, omnis alias consequuntur. Aliquid, suscipit! Ratione, quod necessitatibus.</div>
                    <a href="#">Eyes Tracking</a>
                </div>
            </div>
            <div class="box">
                <div class="imgbox">
                    <img src="https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg?auto=compress&cs=tinysrgb&w=600" alt="">
                </div>
                <div class="content">
                    <h2>Floating Image Viewer</h2>
                    <div class="text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut iste qui, quibusdam, voluptatibus quas ipsa architecto aliquid maxime itaque a impedit harum, omnis alias consequuntur. Aliquid, suscipit! Ratione, quod necessitatibus.</div>
                    <a href="#">Eyes Tracking</a>
                </div>
            </div>
            <div class="box">
                <div class="imgbox">
                    <img src="https://images.pexels.com/photos/67857/daisy-flower-spring-marguerite-67857.jpeg?auto=compress&cs=tinysrgb&w=600" alt="">
                </div>
                <div class="content">
                    <h2>Eyes Position Estimation</h2>
                    <div class="text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut iste qui, quibusdam, voluptatibus quas ipsa architecto aliquid maxime itaque a impedit harum, omnis alias consequuntur. Aliquid, suscipit! Ratione, quod necessitatibus.</div>
                    <a href="#">Eyes Tracking</a>
                </div>
            </div>
            <div class="box">
                <div class="imgbox">
                    <img src="https://images.pexels.com/photos/67857/daisy-flower-spring-marguerite-67857.jpeg?auto=compress&cs=tinysrgb&w=600" alt="">
                </div>
                <div class="content">
                    <h2>Screen Time with CV</h2>
                    <div class="text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut iste qui, quibusdam, voluptatibus quas ipsa architecto aliquid maxime itaque a impedit harum, omnis alias consequuntur. Aliquid, suscipit! Ratione, quod necessitatibus.</div>
                    <a href="#">Eyes Tracking</a>
                </div>
            </div>
        </div>
    </section>
    """
    st.html(html_string)


def youtube_data_display():

    html_string = """ <section class="section">
        <div class="section-title">YouTube Stats</div>
        <div class="stats-container">
            <div class="stat-item">
                <i class="fas fa-video stat-icon"></i>
                <div class="stat-value">120</div>
                <div class="stat-label">Total Videos</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-users stat-icon"></i>
                <div class="stat-value">5k</div>
                <div class="stat-label">Total Subscribers</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-thumbs-up stat-icon"></i>
                <div class="stat-value">50k</div>
                <div class="stat-label">Total Likes</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-comments stat-icon"></i>
                <div class="stat-value">10k</div>
                <div class="stat-label">Total Comments</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-clock stat-icon"></i>
                <div class="stat-value">50h</div>
                <div class="stat-label">Total Content Duration</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-calendar-alt stat-icon"></i>
                <div class="stat-value">5d</div>
                <div class="stat-label">Content Gap</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-thumbs-up stat-icon"></i>
                <div class="stat-value">500</div>
                <div class="stat-label">Average Likes</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-comments stat-icon"></i>
                <div class="stat-value">20</div>
                <div class="stat-label">Average Comments</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-eye stat-icon"></i>
                <div class="stat-value">1M</div>
                <div class="stat-label">Total Views</div>
            </div>
            <div class="stat-item">
                <i class="fas fa-chart-line stat-icon"></i>
                <div class="stat-value">10%</div>
                <div class="stat-label">Engagement Rate</div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="section-title">Recent Videos</div>
        <div class="stats-container">
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/VIDEO_ID_1" allowfullscreen></iframe>
                </div>
                <div class="video-title">Recent Video 1</div>
            </div>
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/VIDEO_ID_1" allowfullscreen></iframe>
                </div>
                <div class="video-title">Recent Video 1</div>
            </div>
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/VIDEO_ID_2" allowfullscreen></iframe>
                </div>
                <div class="video-title">Recent Video 2</div>
            </div>
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/VIDEO_ID_3" allowfullscreen></iframe>
                </div>
                <div class="video-title">Recent Video 3</div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="section-title">Most Popular Videos</div>
        <div class="stats-container">
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/VIDEO_ID_4" allowfullscreen></iframe>
                </div>
                <div class="video-title">Popular Video 1</div>
            </div>
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/VIDEO_ID_4" allowfullscreen></iframe>
                </div>
                <div class="video-title">Popular Video 1</div>
            </div>
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/VIDEO_ID_5" allowfullscreen></iframe>
                </div>
                <div class="video-title">Popular Video 2</div>
            </div>
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/VIDEO_ID_6" allowfullscreen></iframe>
                </div>
                <div class="video-title">Popular Video 3</div>
            </div>
        </div>
    </section> 
    """
    st.html(html_string)


def main():
    # st.set_page_config(layout="wide")
    load_css("style_st.css")
    cards()
    youtube_data_display()


if __name__ == "__main__":
    main()
