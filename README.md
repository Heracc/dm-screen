# dm screen

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dmscreen0.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

### to do:
* make initiative
* make monster names in the initiative board clickable and use st.page_link and st.query_parameters that sets the seach in the bestiary page to that monster
* make it so that theres a button on the bestiary page to add the monster to initiative

for class character data storage

class Char:
ac ect (initialize as empty or use typing)
def __nit__(dict):
    for (var in locals()) {
        var.value = dict[var.key]
    }