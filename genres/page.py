import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros:')

        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=pd.DataFrame(genres_df),
            reload_data=True,
            key='genres_grid'
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar novo gênero:')
    name = st.text_input('Nome do Gênero')

    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(
            name=name
        )
        if new_genre:
            st.rerun()
            st.success(f'Gênero {new_genre} cadastrado com sucesso.')
        else:
            st.error('Erro ao cadastrar gênero. Verifique os campos')
