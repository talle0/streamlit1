import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")
image=st.file_uploader("Upload your image", type=["jpg", "gif","png"])
info=st.empty()
size=st.empty()
mode=st.empty()
format_=st.empty()

if image:
    img=Image.open(image)
    info.subheader("Information")
    size.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html=True)
    st.subheader("Resize")
    width=st.number_input("Width", value=img.width)
    height=st.number_input("Height", value=img.height)
    st.subheader("Rotate")
    degree=st.number_input("Degree")
    st.subheader("Filer")
    filter=st.selectbox("Filter", options=("None", "Detail", "Blur"))
    s_btn=st.button("Submit")
    if s_btn:
        edited=img.resize((width,height)).rotate(degree)
        fil=edited
        if filter != "None":
            if filter == "Detail":
                fil.filter(DETAIL)
            else:
                fil.filter(BLUR)
        st.image(fil)
