import streamlit as st
import pandas as pd
import json

bestiary_page = st.Page("bestiary.py", title="Bestiary")
initiative_page = st.Page("initiative.py", title="Initative Tracker)
players_page = st.Page("players.py", title="Players")

pg = st.navigation([bestiary_page, initative_page, players_page])
pg.run()
"""
with open('monsters.json','r') as m:
    global monsters
    monsters = json.load(m)
st.write(monsters['aboleth']['languages'][0])
st.write(monsters['aboleth'])
st.title("test")
"""
