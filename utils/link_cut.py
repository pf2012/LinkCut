import streamlit as st
import hashlib
from utils.config import url_base


def linkcut(url,user_secret_key=''):
    return (url_base, hashlib.md5((url + st.secrets['secret_key'] + user_secret_key).encode('utf-8')).hexdigest()[0:7])
