import streamlit as st

st.title("Camera Tracking Interface")

if st.button("Open Camera"):
    st.image("http://localhost:8000/video_feed", caption="Video Feed")
