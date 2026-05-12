import streamlit as st
import pandas as pd
monsters = {}
with open('monsters.json','r') as m:
    global monsters
    monsters = m
st.write(monsters['aboleth'])
st.title("test")
