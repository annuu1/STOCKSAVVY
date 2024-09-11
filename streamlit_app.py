import streamlit as st
import threading
import time

def fetch_data():
    while True:
        # Fetch data and check for alerts
        time.sleep(60)  # Fetch every minute

st.title('Background Task Example')

if st.button('Start Background Task'):
    thread = threading.Thread(target=fetch_data)
    thread.start()
