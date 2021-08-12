import streamlit as st
import os

from PIL import Image
import numpy as np
import cv2
import time


def colorspaces():

    def file_selector(folder_path='img'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select a Image file', filenames)
        return os.path.join(folder_path, selected_filename)

    st.title("Color Spaces Conversion - Image")

    filename = file_selector()
    st.write('You selected `%s`' % filename)

    st.subheader("Image Preview")
    st.success("Image loaded successfully")
    st.image(filename, caption='RGB Channel Merged Image',
             use_column_width=True)

    
    option = st.selectbox('Please select the desired color spaces',['Grayscale','Hue Saturation Value','Lab'])
    st.write('Option selected is ' , option)
    
    def hsv():
        im = np.array(Image.open(filename))
        im_R = im.copy()
        im_m = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        st.image(im_m, caption='HSV Converted Image ',
                 use_column_width=True)
        
    def gray():
        im = np.array(Image.open(filename))
        im_R = im.copy()
        im_m = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        st.image(im_m, caption='HSV Converted Image ',
                 use_column_width=True)
        
    def LAB():
        im = np.array(Image.open(filename))
        im_R = im.copy()
        im_m = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
        st.image(im_m, caption='HSV Converted Image ',
                 use_column_width=True)

    st.subheader("Converting into the selected color space ")
    with st.spinner():
        time.sleep(2)
    st.success("Successfully Converted")

    if option == 'Grayscale':
        gray()
    
    if option == 'Hue Saturation Value':
        hsv()
        
    if option == 'Lab':
        LAB()

    st.warning("Made using Python, Streamlit and OpenCV")
    st.info("Enigma CS Club - LiveStream Session Demo")
