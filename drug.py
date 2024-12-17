import streamlit as st
import numpy as np

st.title('Drug Discovery')

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
with st.chat_message("user"):
    st.write("Hello 👋")

# Display a chat input widget inline.
with st.container():
    st.chat_input("Say something")