import streamlit as st
import json

with open('data/monsters.json','r') as file:
    global monsters
    monsters = json.load(file)

def is_valid(search):
    if search in monsters:
        return True
        st.write("test")
    else: return False

st.title("bestiary")

search = st.text_input('search for a monster').lower().strip()

col1, col2, col3 = st.columns(3)
with col1:
    is_valid(search)

with col3:
    is_valid(search)
    #st.image()

if search in monsters:
    st.dataframe(monsters[search])
else: st.write(f"{search} is not a valid monster!")