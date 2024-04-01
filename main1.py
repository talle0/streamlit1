# pip install streamlit
# pip install panda

import streamlit as st
import pandas as pd
import time as ts
from datetime import time

st.title("Uploading Files")
st.markdown("---")
image=st.file_uploader("Upload here", type=("jpg","gif"))
if image is not None:
    st.image(image)

val=st.slider("Slider", min_value=0, max_value=100, value=50)
st.write(val)

text=st.text_input("Write something", max_chars=10)
st.write(text)

text2=st.text_area("Write Something")
st.write(text2)

def converter(value):
    m,s,ms=value.split(":")
    t_s=int(m)*60+int(s)+int(ms)/1000
    return t_s

date=st.date_input("Birthday")
st.write(date)

time1=st.time_input("set time", value=time(0,0,0))
st.write(time1)

if str(time1) == "00:00:00":
    st.write("Please set timer")
else:
    sec=converter(str(time1))
    bar=st.progress(0)
    per=sec/100
    status=st.empty()
    for i in range(100):
        bar.progress((i+1))
        status.write(str(i+1) + "%")
        ts.sleep(per)