import streamlit as st
import json

with open('data/monsters.json','r') as file:
    global monsters
    monsters = json.load(file)

def is_valid(search):
    if search in monsters:
        return True
    else: 
        return False

st.title("Creature Lookup")

searchbox = st.container()

"---"
stat_header = st.container(border=True)
left, middle, right = stat_header.columns([2,1,1])

def display_result():
    search = st.session_state.creature_search
    if is_valid(search):
        hp = f"{monsters[search]['maxHitPoints']} ({monsters[search]['hitDice']})"
        ac = monsters[search]['ac']
        with left:
            st.header(monsters[search]['name'], width="stretch")
        with middle:
            st.subheader(f"HP: {hp}")
        with right:
            st.subheader(f"AC: {ac}")
            
        with stat_header:
            type_alignment = f"{monsters[search]['size']} {monsters[search]['creatureType']}, {monsters[search]['alignment']}"
            st.write(type_alignment.title())
            st.write(f"Challenge Rating: {monsters[search]['challenge']['rating']} ({monsters[search]['challenge']['xp']} XP)")
            "---"
            with st.expander("Image"):
                st.image(monsters[search]['imageUrl'])
            with st.expander("Stats", expanded=True):
                st.write(f"HP: {hp}")
                st.write(f"AC: {ac}")
                st.write(f"Initiative: {monsters[search]['modifiers']['dex']}")
                " "
                for speed_type, value in monsters[search]['speed'].items():
                    if speed_type != "hover":
                        if value != 0:
                                st.write(f"{speed_type.title()}: {value} ft.")
                    else: st.write(f"Hover: {str(value).title()}")
        

with searchbox:
    creature_search = st.selectbox(
        'Search for a creature',
        monsters.keys(), 
        index=None,
        placeholder="Search for a creature", 
        label_visibility="hidden",
        key="creature_search",
        on_change = display_result,
    )

