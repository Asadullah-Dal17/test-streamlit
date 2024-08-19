import streamlit as st
from pages.home import home
from pages.youtube import youtube
from pages.memes import memes

pg = st.navigation(
    [
        st.Page(
            home,
            title="Home",
            icon=":material/home:",
        ),
        st.Page(
            youtube,
            title="Youtube Analysis",
            icon=":material/analytics:",
        ),
        st.Page(
            memes,
            title="Random Memes",
            icon=":material/ar_on_you:",
        ),
    ]
)
pg.run()
