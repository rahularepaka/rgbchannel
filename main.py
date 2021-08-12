import streamlit as st
import os

from PIL import Image
import numpy as np
import cv2
import time

from splitter import *
from colorspaces import *


menu = ["RGB-Splitter", "Color-Spaces", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == 'RGB-Splitter':
    st.subheader("RGB-Splitter")
    
    spilt()
    
if choice == 'Color-Spaces':
    st.subheader("Color-Spaces")

    colorspaces()
    
if choice == 'About':
    st.title("About")
    
    with st.expander("License"):

        st.markdown("""
                        
        MIT License
        Copyright (c) 2021 Rahul Arepaka
        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:
        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.
                        """
                    )

    st.subheader("Author")
    st.markdown(
        '''
            I am Rahul Arepaka, II year CompSci student at Ecole School of Engineering, Mahindra University
            '''
        '''
            Linkedin Profile : https://www.linkedin.com/in/rahul-arepaka/
            '''
        '''
            Github account : https://github.com/rahularepaka
            '''
    )

    st.info("Feel free to edit with the source code and enjoy coding")
    st.warning("Enigma CS Club - LiveStream Demo")
