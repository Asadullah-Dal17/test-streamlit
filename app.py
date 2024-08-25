import streamlit as st
from streamlit_navigation_bar import st_navbar


def home():
    st.title("Home")
    st.write("Welcome to the Home page!")


def about():
    st.title("About")
    st.write("This is the About page.")


def contact():
    st.title("Contact")
    st.write("Here is the Contact page.")


def main():
    # Create a list of page names and link them to their respective functions
    pages = {"Home": home, "About": about, "Contact": contact}

    # Create the navigation bar
    page = st_navbar(list(pages.keys()))

    # Display the selected page
    pages[page]()


if __name__ == "__main__":
    main()
