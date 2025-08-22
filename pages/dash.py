import streamlit as st
from utils.conect_db import get_statistics
from utils.config import url_base
from utils.menu import menu
from utils.config import app_name, app_icon

st.set_page_config(page_title=f'{app_name} | Dashboard',page_icon=app_icon,layout='centered')
st.title(':material/dashboard: Dashboard',anchor=False)
menu()


urls=st.text_area('URLs encurtadas (separadas por vírgula)*', height=100, help='Cole as URLs encurtadas que você deseja obter estatísticas. Separe múltiplas URLs com vírgulas.')
user_secret_key = st.text_input('Chave secreta*', autocomplete='off',type='password')

disabled = True
if urls != '' and user_secret_key != '':
    disabled = False


if st.button('Gerar Estatísticas',use_container_width=True,type='primary',disabled=disabled):
    links = [link.strip() for link in urls.split(',')]
    valid_links = get_statistics(links, user_secret_key)
    if valid_links:
        st.write('### URLs Encurtadas:')
        n_cols=2
        cols_results = st.columns(n_cols,gap='medium')
        for i, link in enumerate(valid_links):
            with cols_results[i % n_cols]:
                with st.container(border=True):
                    st.markdown(f'##### {link[0]}')
                    st.markdown(f'**URL Curta:** {url_base}{link[1]}')
                    st.markdown(f'**Criada em:** {link[2]}')
                    st.markdown(f'**Acessos:** {link[3]}')
                    st.markdown(f'**Ultimo Acesso:** {link[4]}')
                    st.link_button(label=f'**:material/line_axis: Tempo Real**',url=f'/real_time/?c={link[1]}',use_container_width=True)

    else:
        st.warning('Nenhuma URL válida encontrada.')

