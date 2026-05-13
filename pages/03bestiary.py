import streamlit as st
import json
st.title("bestiary")
search = st.text_input('search for a monster').lower().strip()
with open('data/monsters.json','r') as file:
    monsters = json.load(file)
    if search in monsters:
        st.dataframe(monsters[search])
    else: st.write(f"{search} is not a valid monster!")