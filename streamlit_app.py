import streamlit as st
import pandas as pd
import json

initiative_page = st.Page("pages/01initiative.py", title="Initative Tracker")
players_page = st.Page("pages/02players.py", title="Players")
bestiary_page = st.Page("pages/03bestiary.py", title="Bestiary")

pg = st.navigation([bestiary_page, initiative_page, players_page])
pg.run()
"""
with open('monsters.json','r') as m:
    global monsters
    monsters = json.load(m)
st.write(monsters['aboleth']['languages'][0])
st.write(monsters['aboleth'])
st.title("test")
"""
