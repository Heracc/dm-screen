import streamlit as st
st.title("Initiative")

left, right = st.columns([2,1])
with left:
    st.text_input("Add a monster or player", label_visibility="hidden", placeholder="Add a monster or player")

with right:
    st.space()
    st.button("Add Combatant")