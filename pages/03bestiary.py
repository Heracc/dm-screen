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

st.title("test page")

search = st.text_input('search for a monster', value="Search here...").lower().strip()
"---"
stat_header = st.container(border=True)
left, right = stat_header.columns([3,1])

if is_valid(search):
    hp = f"{monsters[search]['maxHitPoints']} ({monsters[search]['hitDice']})"
    ac = monsters[search]['ac']
    with left:
        st.header(monsters[search]['name'], width="stretch")
        type_alignment = f"{monsters[search]['size']} {monsters[search]['creatureType']}, {monsters[search]['alignment']}"
        st.write(type_alignment.title())
        st.write(f"HP: {hp}")
    with stat_header:
        "---"
        with st.expander("Image"):
            st.image(monsters[search]['imageUrl'])
        with st.expander("Stats"):
            st.write(f"HP: {hp}")
            st.write(f"AC: {ac}")
            st.write(f"Initiative: {monsters[search]['modifiers']['dex']}")
            st.write(" ")
            for speed_type, value in monsters[search]['speed'].items():
                if speed_type != "hover":
                    if value is not 0:
                        if speed_type == "hover":
                            pass
                        else:
                            st.write(f"{speed_type.title()}: {value} ft.")
                else: st.write(f"Hover: {str(value.title())}")
    with right:
        st.write(f"Challenge Rating: {monsters[search]['challenge']['rating']} ({monsters[search]['challenge']['xp']} XP)")
        st.write(f"AC: {ac}")
        

else: 
    with stat_header:
        st.header(f"{search} is not a valid monster.")

