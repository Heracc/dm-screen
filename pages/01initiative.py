import streamlit as st
st.title("initiative")

with st.container(horizontal=True):
    st.text_input("add a monster or player", label_visibility="hidden", placeholder="Add a monster or player")
    st.space()
    st.button("Add Combatant")