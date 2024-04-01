import streamlit as st
import requests
from bs4 import BeautifulSoup

#st.image("https://images.unsplash.com/photo-1584036561566-baf8f5f1b144")

st.markdown("<h1 style='text-align: center;'>Image Scrapping</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keywords=st.text_input("Keyeword")
    search=st.form_submit_button("Submit")
    if search:
        page=requests.get(f"https://unsplash.com/ko/s/사진/{keywords}")
        soup=BeautifulSoup(page.content, 'lxml')
        rows=soup.find_all("div", class_="ripi6")
        for row in rows:
            figures=row.find_all("figure")
            for i in range(2):
                img=figures[i].find("img", class_="MorZF")
                print(img)
                print("\n")
        #print(len(rows))
