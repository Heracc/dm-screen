# Project Title: 
DM Tools

# Project Description: 
This program uses the Streamlit library to create an interactive webapp with useful tools for people who are running Dungeons and Dragons campaigns. Users use a keyboard to input text into text fields, and a mouse to interact with buttons and dropdowns.

# Concept Application: 
This month, I learned about external libraries and their implementation. I also delved into SQL databases and how to interact with them within a Python program. I applied these skills in my program by using the Streamlit library, which provides lots of elements that help build websites. These are implemented by calling different methods such as st.write() to display text on the page or st.text_input() to display an interactive text box for users to input text. Additionally, I used the SQLAlchemy ORM (an ORM is an Object Relational Mapper and allows for the interaction with SQL from a Python script using OOP code rather than having to write raw SQL queries) library to edit an SQL database hosted on a service called Supabase. I also implemented more of my knowledge of classes that I learned from the last task, albeit in a very different way than I was used to: the ORM allowed me to use classes to represent player stat 'sheets'.
   
## Streamlit Explanation:
   Streamlit is a library that allows you to create websites using elements to build the website modularly. There are elements for everything from text input to dropdown selects to maps, and you can combine these in any way you want to build a site. The library handles the UI design for you (you still have to position the elements where you want them), so you can focus on the actual content of the website. Each page is one Python file that reruns from top to bottom everytime the user interacts with an element (except in an st.form, those don't rerun the page until they're submitted), so to save variables between reruns, you need to use what Streamlit calls "statefulness". You can store things in st.session_state using either dictionary-like syntax:

   ```
   st.session_state['greeting'] = "Hello World!"
   ```

   or attribute based syntax:

   ```
   st.session_state.greeting = "Hello World!"
   ```

   You can then use this like a variable:

   ```
   print(st.session_state.greeting)
   ```

   or

   ```
   print(st.session_state['greeting'])
   ```

   will both output `Hello World!` to the console.

   Statefulness allows you to have variables that will exist on all pages and won't be reset when the app is rerun.

## SQLAlchemy and Supabase Explanation:
   gup

# Development Process: 
The biggest issue I had while writing this program was figuring out how to connect to and interact with the Supabase SQL database using the SQLAlchemy session maker. I had to use Google AI Overview extensively here, as the Supabase official documentation didn't have any instructions for connecting with an ORM like SQLAlchemy. Once the AI got me started though, I was able to go forward on my own. After that, I did struggle with the ORM syntax for interacting with the SQL database, but I was able to figure out with a combination of help from Cooper, Gemini AI, and the SQLAlchemy docs.

# AI Disclosure:
I used AI to help me with the SQL queries. I had to look up a lot of things to do with the ORM querying, and sometimes the best answer I could find was from the AI Overview. The two main sections where I used AI was in the retrieval and deletal of the player sheets. There was some other AI used for the formatting of the pandas dataframe used to display the player sheets, but only for two lines where I didn't know how to use the pandas library fully.

---
# Useful Things

[![Open Website](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dmscreen0.streamlit.app/)

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
