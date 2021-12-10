# IMPORTS
# general
import numpy as np
import streamlit as st
import pandas as pd
import altair as alt

# Video getting and saving
import cv2  # open cvs, image processing
import urllib
import m3u8
import time
import pafy  # needs youtube_dl

# File handling
from pathlib import Path
import os
import pickle
from io import BytesIO
import requests
import sys

# Import mrcnn libraries
# I am using Matterport mask R-CNN modified for tensor flow 2, see source here:
# https://raw.githubusercontent.com/akTwelve/Mask_RCNN/master'

import mrcnn.config
import mrcnn.utils
from mrcnn.model import MaskRCNN

# Preprocessed demo video
DEMO_VIDEO = r"https://github.com/rejexx/Parkingspot_Vacancy/blob/main/src/streamlit_app/demo.avi?raw=true"

######################################
# Functions
######################################


def main():
    ######################################
    # Streamlit
    ######################################
    st.title("Spot Or Not?")
    st.write("Parking Spot Vacancy with Machine Learning")

    # Render the readme as markdown using st.markdown as default
    readme_text = st.markdown(get_file_content_as_string("instructions.md"))

     # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("Settings")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Show instructions", "Preprocessed demo data", "Live data", "Camera viewer","Show the source code"])
    if app_mode == "Show instructions":
        st.sidebar.success('Next, try selecting "Preprocessed demo data".')
    elif app_mode == "Show the source code":
        readme_text.empty()
        st.code(get_file_content_as_string("streamlit_app.py"))
    elif app_mode == "Preprocessed demo data":
        # Add horizontal line to sidebar
        st.sidebar.markdown("___")
        readme_text.empty()
        demo_mode(DEMO_VIDEO)
    elif app_mode == "Live data":
        # Add horizontal line to sidebar
        st.sidebar.markdown("___")
        readme_text.empty()
        live_mode()
    elif app_mode == "Camera viewer":
        # Add horizontal line to sidebar
        st.sidebar.markdown("___")
        readme_text.empty()
        camera_view()

    return None

