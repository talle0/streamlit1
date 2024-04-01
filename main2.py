import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
bar_x = np.array([1,2,3,4,5])

opt=st.sidebar.radio("Select", options=("Line","Bar","H-bar"))
if opt=="Line":
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x),'--')
    st.write(fig)
elif opt == "Bar":
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.bar(bar_x, bar_x*10)
    st.write(fig)
else:
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.barh(bar_x*10, bar_x)
    st.write(fig)
    

st.markdown("<h1 style='text-align: center;'>Registeration</h1>", unsafe_allow_html=True)

form = st.form("Form 1")
form.text_input("Name")
form.form_submit_button("submit")

with st.form("Form 2"):
    col1,col2=st.columns(2)
    c1=col1.text_input("Name")
    c2=col2.text_input("Name1")
    st.text_input("E-mail")
    s_state=st.form_submit_button("submit")
    if s_state:
        if (c1 == "") or (c2 == ""):
            st.warning ("fill the blankx`") 
        else:
            st.success("Good")

