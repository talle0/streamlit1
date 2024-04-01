# pip install streamlit
# pip install panda

import streamlit as st
import pandas as pd
table=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})
st.title("I am King!")
st.subheader("You are my slave. ㅎㅎㅎㅎ")
st.header("안녕하세요. 주인님")
st.text("무엇이든 말씀만 하세요. 무엇을 도와드릴까요?")
st.markdown("**Hello** *World*")
st.markdown("[Naver](https://naver.com)")
st.markdown("---")
st.caption("Small characters")
st.latex(" \sqrt[3]{x^3+y^3 \over 2}")
jj={"a":"1,2,3","b":"4,5,6"}
st.json(jj)
cc="""
print("Hello World")
def func():
    return o;"""
st.code(cc)

st.table(table)
st.dataframe(table)
st.image("portal-logo.gif", caption="UNIST logo")
st.video("https://youtu.be/E85Y4_DDAW8")
def change():
    print(st.session_state.checker)
state = st.checkbox("check", value=True, on_change=change, key="checker")
if state:
    st.write("Hi")
else:
    st.write("bye")
    pass
radiob = st.radio("Select one", options=("a","b","c"))
print(radiob)
def btn_click():
    print("Clicked")
btn=st.button("Click!", on_click=btn_click)
sel=st.selectbox("select one", options=("aa","bb","cc"))

ms=st.multiselect("select multiple", options=("1","2","3","4"))
st.write(ms)