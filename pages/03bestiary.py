import streamlit as st
import pandas as pd

st.title("bestiary")
search = st.text_input('search for a monster').lower().strip()
with open('data/monsters.json','r') as monsters:
    if search in monsters:
        df = pandas.DataFrame(monsters[search])
        st.dataframe(df)
    else: st.write()