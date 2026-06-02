import streamlit as st

account_page = st.Page("pages/00account.py", title="Account")
initiative_page = st.Page("pages/01initiative.py", title="Initative Tracker")
players_page = st.Page("pages/02players.py", title="Players")
creatures_page = st.Page("pages/03creatures.py", title="Creatures")

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user == None:
    pg = st.navigation([account_page, initiative_page, bestiary_page])
elif st.session_state.user == "cbaee7e9-cbd4-4624-b013-af943fd21702":
    creatures_page = st.Page("pages/03creatures.py", title="bestiality (for goonmaster45's eyes only)")
    pg = st.navigation([account_page, initiative_page, players_page, creatures_page])
else:
    pg = st.navigation([account_page, initiative_page, players_page, creatures_page])
pg.run()
