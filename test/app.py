import streamlit as st

# Set the page title
st.set_page_config(page_title="Most Popular Videos")

# HTML and CSS for embedding YouTube videos with custom styling
html_code = """
    <style>
    .section {
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
    }
    .section-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stats-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .video-item {
        width: calc(33.333% - 20px);
        background-color: #ffffff;
        border-radius: 8px;
        padding: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .video-embed {
        position: relative;
        padding-bottom: 56.25%; /* 16:9 aspect ratio */
        height: 0;
        overflow: hidden;
        border-radius: 8px;
    }
    .video-embed iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
    .video-title {
        font-size: 18px;
        font-weight: 600;
        margin-top: 10px;
    }
    .video-stats {
        font-size: 14px;
        color: #555555;
        margin-top: 5px;
    }
    </style>

    <section class="section">
        <div class="section-title">Most Popular Videos</div>
        <div class="stats-container">
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" allowfullscreen></iframe>
                </div>
                <div class="video-title">Popular Video 1</div>
                <div class="video-stats">Likes: 12 | Comments: 12</div>
            </div>
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" allowfullscreen></iframe>
                </div>
                <div class="video-title">Popular Video 2</div>
            </div>
            <div class="video-item">
                <div class="video-embed">
                    <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" allowfullscreen></iframe>
                </div>
                <div class="video-title">Popular Video 3</div>
            </div>
        </div>
    </section>
"""

# Use st.markdown to render the HTML and CSS
st.markdown(html_code, unsafe_allow_html=True)

# Add other content to your Streamlit app
st.write("Check out the most popular videos!")
