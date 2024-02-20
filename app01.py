import streamlit as st

h = st.header('My Raindear website eiei')
s = st.subheader('เว็บไซต์ของน้องกวาง')
p = st.write('เว็บไซต์นี้แลกมาด้วยน้ำตา')
banner = st.image('momo.jpg')
text = st.text_input("Prompt: ")
submit = st.button("Render")
if not text:
    st.write("กรุณากรอกข้อมูล")
elif submit or text:
    st.write("กำลังโหลด...")
