import streamlit as st
import json

col1, col2, col3 = st.columns(3)

with open('data/monsters.json','r') as file:
    global monsters
    monsters = json.load(file)

def is_valid(search):
    if search in monsters:
        return True
    else: 
        return False

st.title("test page")

search = st.text_input('search for a ').lower().strip()
stat_header = st.container(border=True)
stat_header.border=False
if is_valid(search):
    stat_header.header(monsters[search])
else: stat_header.header(f"{search} is not a valid monster.")

with col1:
    pass
with col2:
    pass

with col3:
    pass
    #st.image()
