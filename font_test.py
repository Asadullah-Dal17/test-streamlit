import streamlit as st

st.set_page_config(page_title="Profile Page", page_icon=":wave:", layout="wide")


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

load_css("fonts_test.css")
