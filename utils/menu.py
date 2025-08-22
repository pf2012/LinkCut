import streamlit as st
from utils.config import app_name

def menu():
    with st.sidebar:
        st.title('Menu')
        st.link_button(':material/link: Encurtador', '/',use_container_width=True,type='primary')
        st.link_button(':material/dashboard: Dash', '/dash', use_container_width=True,type='primary')

