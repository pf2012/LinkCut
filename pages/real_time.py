import streamlit as st
from utils.menu import menu
from utils.config import app_name, app_icon
from utils.conect_db import get_access_count


st.set_page_config(page_title=f'{app_name} | Real Time Dashboard',page_icon=app_icon,layout='centered')

seconds = 10

st.title(':material/line_axis: Real Time Dashboard',anchor=False, help=f'Atualização a cada {seconds} segundos')
menu()

user_secret_key = st.text_input('Chave secreta*', autocomplete='off',type='password')

if 'actual' not in st.session_state:
    st.session_state['actual'] = 0



@st.fragment(run_every=f'{seconds}s')
def render():
    if user_secret_key != '':
        access = get_access_count(st.query_params.to_dict().get('c', ['']),user_secret_key)
        with st.container(border=True):
            st.markdown(f'## {access[0]}')
            ultimo=st.session_state['actual']
            diference = access[1] - ultimo
            if diference > 0:
                st.toast(f'{diference} novo(s) acesso(s) registrado(s)!',icon="✅")
                st.session_state['actual'] = access[1]
            st.markdown(f'# Acessos: :green[{access[1]}]')
            st.markdown(f'#### Ultimo Acesso: {access[2]}')





render()