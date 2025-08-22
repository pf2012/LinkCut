import streamlit as st
from utils.conect_db import save_link
from utils.link_cut import linkcut
from utils.menu import menu
from utils.config import app_name, app_icon

st.set_page_config(page_title=f'{app_name} | Encurtador',page_icon=app_icon,layout='centered')
st.title(':material/link: LinkCut - Encurtador de URLs',anchor=False)
menu()



url = st.text_input('URL que deseja encurtar*')
user_secret_key = st.text_input('Chave secreta*',autocomplete='off',help='A chave secreta é usada para gerenciar suas URLs, de forma que apenas você possa ver as estatísticas das URLs que criou.',type='password')

disabled = True
if url != '' and user_secret_key != '':
    disabled = False

actual_url = st.context.headers['host']


if st.button('Encurtar URL',use_container_width=True,type='primary',disabled=disabled):
    short_url = linkcut(url,user_secret_key)
    cols=st.columns([1,9],vertical_alignment='center')
    cols[0].link_button(':material/link:', short_url[0]+short_url[1],width='stretch')
    cols[1].code(actual_url+'/'+short_url[0]+short_url[1], language='plaintext',width='stretch')
    save_link(url,user_secret_key,short_url[1])