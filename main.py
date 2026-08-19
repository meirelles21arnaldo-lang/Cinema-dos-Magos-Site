import streamlit as st
import database as db


st.title("Cinema do Mago", text_alignment="center")
st.header("Painel de Gestão de Títulos em Exibição", text_alignment="center")

colunas = st.columns(2)

with colunas[0]:
    st.markdown("##### --- Cadastro de Filmes ---", text_alignment="center")

    with st.form("form_cadastro_filmes", width="stretch"):
        nome_filme = st.text_input("Nome do Filme")
        genero_filme = st.selectbox("Classificação Etária", ("Ação","Comédia","Terror", "Romance"))
        clasf_etaria = st.selectbox ("Classificação Etária" , ("Livre" , "6 anos", "10 anos", "12 anos", "14 anos", "16 anos", "18 anos"))
        duracao_filme = st.number_input ("Duração (em minutos)", min_value=0, max_value=500, value=0)
        capa_filmes = st.file_uploader("Capa do Filme", type="image")

        #pega o arquivo mandado e transforma em binário
        if capa_filmes != None:
            data_capa = capa_filmes.read()
#        else:
#            st.write("Insira a capa do filme")

        btn_cadastro_filme = st.form_submit_button("Salvar")

        if btn_cadastro_filme:
            db.cadastrar_filme (nome_filme, genero_filme, clasf_etaria, duracao_filme, data_capa)

with colunas[1]:
    st.subheader("coluna 2")
