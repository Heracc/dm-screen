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
left, middle, right = stat_header.columns(3)

if is_valid(search):
    with stat_header:
        st.header(monsters[search]['name'])
        st.space('stretch')
        st.write(f"Challenge Rating: {monsters[search]['challenge']['rating']}")
else: stat_header.header(f"{search} is not a valid monster.")


with col1:
    pass
with col2:
    pass

with col3:
    pass
    #st.image()
