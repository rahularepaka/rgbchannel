import streamlit as st
import os

from PIL import Image
import numpy as np
import cv2
import time

def spilt():


    def file_selector(folder_path='img'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select a Image file', filenames)
        return os.path.join(folder_path, selected_filename)


    st.title("RGB Channel Splitter - Image")

    filename = file_selector()
    st.write('You selected `%s`' % filename)

    st.subheader("Image Preview")
    st.success("Image loaded successfully")
    st.image(filename, caption='RGB Channel Merged Image', use_column_width=True)


    def red():
        im = np.array(Image.open(filename))
        im_R = im.copy()
        im_R[:, :, (1, 2)] = 0
        st.image(im_R, caption='Red Channel Split Image', use_column_width=True)


    def blue():
        im = np.array(Image.open(filename))
        im_B = im.copy()
        im_B[:, :, (0, 1)] = 0
        st.image(im_B, caption='Blue Channel Split Image.', use_column_width=True)


    def green():
        im = np.array(Image.open(filename))
        im_G = im.copy()
        im_G[:, :, (0, 2)] = 0
        st.image(im_G, caption='Green Channel Split Image', use_column_width=True)


    st.subheader("Splitting into RGB")
    with st.spinner():
        time.sleep(2)
    st.success("Successfully Splitted")

    col1, col2, col3 = st.columns(3)


    with col1:
        st.header("Red")
        red()

    with col2:
        st.header("Green")
        green()

    with col3:
        st.header("Blue")
        blue()

    st.warning("Made using Python, Streamlit and OpenCV")
    st.info("Enigma CS Club - LiveStream Session Demo")
