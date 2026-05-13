import streamlit as st
import json

with open('data/monsters.json','r') as file:
    global monsters
    monsters = json.load(file)

def test():
    st.write("this is a test")

def is_valid(search):
    if search in monsters:
        st.write("test")
        return True
    else: return False

st.title("test page")

search = st.text_input('search for a ').lower().strip()

col1, col2, col3 = st.columns(3)
with col1:
    test()

with col2:
    if search in monsters:
        st.write("found")
        #st.dataframe(monsters[search])
    else: st.write(f"{search} is not a valid!")

with col3:
    is_valid(search)
    test()
    #st.image()

test()
