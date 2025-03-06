import streamlit as st
import pandas
from streamlit import set_page_config


set_page_config(layout="wide", page_icon="🦥", page_title="Our Company")

st.title("The best company 🖥️💻")

st.write(""""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
 Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
 Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
""")

st.subheader("Our team:")
col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5,0.5,1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=",")
tot_columns = len(df)
print(tot_columns)
print(tot_columns // 3)

for index,  row in df[:tot_columns // 3].iterrows():
    print(index)

for index, row in df[-4:].iterrows():
    print(index)

with col1:
    #iterating only over the first four columns
    for index, row in df[:tot_columns // 3].iterrows():
        st.subheader(f"{row["first name"]} {row["last name"]}")
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    #iterating only over the middle four columns
    for index, row in df[(tot_columns // 3):(tot_columns // 3)*2].iterrows():
        st.subheader(f"{row["first name"]} {row["last name"]}")
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    #iterating only over the last four columns
    for index, row in df[-(tot_columns // 3):].iterrows():
        st.subheader(f"{row["first name"]} {row["last name"]}")
        st.write(row["role"])
        st.image("images/"+row["image"])