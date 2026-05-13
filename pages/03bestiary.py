import streamlit as st
import json


with open('data/monsters.json','r') as file:
    global monsters
    monsters = json.load(file)

def is_valid(search):
    if search in monsters:
        return True
    else: 
        return False

st.title("test page")

search = st.text_input('search for a monster', value="Search here...").lower().strip()
"---"
stat_header = st.container(border=True)
left, right = stat_header.columns([4,1])

if is_valid(search):
    with left:
        st.header(monsters[search]['name'], width="stretch")
    with right:
        st.markdown(f"Challenge Rating: {monsters[search]['challenge']['rating']}", text_alignment='right')
else: 
    with stat_header:
        st.header(f"{search} is not a valid monster.")

