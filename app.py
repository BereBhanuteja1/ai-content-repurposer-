import streamlit as st
import requests

st.title("🎬 AttentionX AI")

uploaded_file = st.file_uploader("Upload a video", type=["mp4"])

if uploaded_file is not None:
    st.video(uploaded_file)

    if st.button("Upload to Backend"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/upload-video/", files={"file": uploaded_file})
        
        st.success("Uploaded Successfully 🚀")
        st.json(response.json())