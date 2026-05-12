import streamlit as st
import pandas as pd
import json
with open('monsters.json','r') as m:
    global monsters
    monsters = json.load(m)
st.write(monsters['aboleth']['languages'][0])
st.write(monsters['aboleth'])
st.title("test")
