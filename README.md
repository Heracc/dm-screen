# Project Title: 
DM Tools

# Project Description: 
This program uses the Streamlit library to create an interactive webapp with useful tools for people who are running Dungeons and Dragons campaigns. Users use a keyboard to input text into text fields, and a mouse to interact with buttons and dropdowns.

# Concept Application: 
This month, I learned about external libraries and their implementation. I also delved into SQL databases and how to interact with them within a Python program. I applied these skills in my program by using the Streamlit library, which provides lots of elements that help build websites. These are implemented by calling different methods such as st.write() to display text on the page or st.text_input() to display an interactive text box for users to input text. Additionally, I used the SQLAlchemy ORM (an ORM is an Object Relational Mapper and allows for the interaction with SQL from a Python script using OOP code rather than having to write raw SQL queries) library to edit an SQL database hosted on a service called Supabase. I also implemented more of my knowledge of classes that I learned from the last task, albeit in a very different way than I was used to: the ORM allowed me to use classes to represent player stat 'sheets'.

# Development Process: 
<What challenges or bugs did you encounter in your program? How did you address these issues?>

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
* make creature names in the initiative board clickable and use st.page_link and st.query_parameters that sets the seach in the creature page to that creature
* make it so that theres a button on the creature page to add the creature to initiative
* make a button on player card to add to initiative?
