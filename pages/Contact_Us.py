import streamlit as st
import pandas
from my_functions import send_email

st.title("Contact Us")

df = pandas.read_csv("topics.csv")
topics = []
for index, item in df.iterrows():
    topics.append(item["topic"])
print(f"topics= {topics}")

with st.form(key="form_input"):
    user_email = st.text_input("myemail@gmail...")
    topic_selection = st.selectbox("What topic do you want to discuss?", topics)
    raw_input = st.text_area("Enter your message here...")

    message = f"""\
Subject: {topic_selection} from {user_email}

from: {user_email} 
Topic: {topic_selection}
{raw_input}
"""
    print(message)
    button = st.form_submit_button("Send")

    if button:
        send_email(message)
        st.info("Message sent")
