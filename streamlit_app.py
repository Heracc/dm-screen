import streamlit as st
import pandas as pd
with open('monsters.json','r') as m:
    global monsters
    monsters = json.load(m)
st.write(monsters['aboleth'])
st.title("test")
