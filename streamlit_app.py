import streamlit as st

# Title of the app
st.title('My First Streamlit App')

# Adding a slider widget
number = st.slider('Select a number:', 1, 100)

# Display the selected number
st.write(f'You selected: {number}')
