import streamlit as st
import importlib

# Set up the page title and icon
st.set_page_config(page_title="Recipe Finder", page_icon="🍽️")

# Sidebar navigation to switch between pages
page = st.sidebar.radio("Select a page:", ["Home", "About", "Contact"])

# Dynamically import and run the page based on the selection
if page == "Home":
    # Import home.py and run it
    home_page = importlib.import_module("home")
    home_page.run()

elif page == "About":
    # Import about.py and run it
    about_page = importlib.import_module("about")
    about_page.run()

elif page == "Contact":
    # Import contact.py and run it
    contact_page = importlib.import_module("contact")
    contact_page.run()
