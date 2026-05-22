import streamlit as st

account_page = st.Page("pages/00account.py", title="Account")
initiative_page = st.Page("pages/01initiative.py", title="Initative Tracker")
players_page = st.Page("pages/02players.py", title="Players")
bestiary_page = st.Page("pages/03bestiary.py", title="Bestiary")

pg = st.navigation([account_page, initiative_page, players_page, bestiary_page])
pg.run()
