import streamlit as st
from pages import home, youtube, memes  # Ensure pages is the correct directory

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "YouTube Analysis", "Random Memes"],
    index=0,  # Default selected page
)

# Load the selected page
if page == "Home":
    home.main()
elif page == "YouTube Analysis":
    youtube.main()
elif page == "Random Memes":
    memes.main()
