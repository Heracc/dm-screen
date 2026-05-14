import streamlit as st
st.title("initiative")

left, right = st.columns(2)
with left:
    st.text_input("add a monster or player", label_visibility="hidden", placeholder="Add a monster or player")

with right:
    st.button("Add Combatant")