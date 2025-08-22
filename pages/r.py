import streamlit as st
from utils.conect_db import get_original_url



try:
    st.markdown(
        f"""
        <meta http-equiv="refresh" content="0; url={get_original_url(st.query_params.to_dict().get('c', ['']))}">
        """,
        unsafe_allow_html=True
    )
except:
    st.error('URL não encontrada ou inválida.', icon=':material/error:')

