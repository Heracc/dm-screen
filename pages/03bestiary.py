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
left, right = stat_header.columns([3,1])

if is_valid(search):
    with left:
        st.header(monsters[search]['name'], width="stretch")
        type_alignment = f"{monsters[search]['size']} {monsters[search]['creatureType']}, {monsters[search]['alignment']}"
        st.write(type_alignment.title())
        "---"
        st.image(monsters[search]['imageUrl'], width=400)
    with right:
        st.markdown(f"Challenge Rating: {monsters[search]['challenge']['rating']} ({monsters[search]['challenge']['xp']} XP)")
else: 
    with stat_header:
        st.header(f"{search} is not a valid monster.")

