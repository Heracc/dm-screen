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
stat_header = st.container(border=True, horizontal=True)
left, middle, right = stat_header.columns(3)

if is_valid(search):
    with stat_header:
        st.header(monsters[search]['name'], width="stretch")
        st.space('stretch')
        st.write(f"Challenge Rating: {monsters[search]['challenge']['rating']}")
else: stat_header.header(f"{search} is not a valid monster.")


with left:
    pass
with middle:
    pass

with right:
    pass
    #st.image()
