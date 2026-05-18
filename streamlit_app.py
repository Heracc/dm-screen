import streamlit as st


if "encounter" not in st.session_state:
    st.session_state.encounter = []

initiative_page = st.Page("pages/01initiative.py", title="Initative Tracker")
players_page = st.Page("pages/02players.py", title="Players")
bestiary_page = st.Page("pages/03bestiary.py", title="Bestiary")

pg = st.navigation([initiative_page, players_page, bestiary_page])
pg.run()
