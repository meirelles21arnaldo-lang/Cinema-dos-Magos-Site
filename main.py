import streamlit as st
import database as db


st.title("Cinema do Mago", text_alignment="center")
st.header("Painel de Gestão de Títulos em Exibição", text_alignment="center")

colunas_superior = st.columns(2)

with colunas_superior[0]:
    st.markdown("##### --- Cadastro de Filmes ---", text_alignment="center")

    with st.form("form_cadastro_filmes", width="stretch"):
        nome_filme = st.text_input("Nome do Filme")
        genero_filme = st.selectbox("Classificação Etária", ("Ação","Comédia","Terror"))
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
            db.cadastrar_filme(nome_filme, genero_filme, clasf_etaria, duracao_filme, data_capa)

with colunas_superior[1]:
    st.subheader("coluna 2")

#colunas de baixo
colunas_inferior = st.columns(2)

with colunas_inferior [0]:
    st.markdown("##### --- Alteração de Filmes ---", text_alignment="center")

    opcao_vote = st.radio("Busca por:" , ["ID do Filme" , "Nome do Filme"] , horizontal=True)

    if opcao_vote == "ID do Filme":
        with st.form ("formUpdateFilmeByID" , height="stretch"):

            id_filme = st.number_input("Digite o ID do filme:" , step= 1, min_value=0)

            genero_filme = st.selectbox("Classificação Etária", ("Ação","Comédia","Terror"))
            clasf_etaria = st.selectbox ("Classificação Etária" , ("Livre" , "6 anos", "10 anos", "12 anos", "14 anos", "16 anos", "18 anos"))
            duracao_filme = st.number_input ("Duração (em minutos)", min_value=0, max_value=500, value=0)
            capa_filmes = st.file_uploader("Capa do Filme", type="image")

            if capa_filmes != None:
                capa_filmes = capa_filmes.read()

            btn_update = st.form_submit_button("Enviar")
            if btn_update:
                db.update_filme_by_id(id_filme , genero_filme , clasf_etaria , duracao_filme , capa_filmes)

    if opcao_vote == "Nome do Filme":
            with st.form ("formUpdateFilmeByName" , height="stretch"):
                st.text_input("Digite o Nome do filme:")
                genero_filme = st.selectbox("Classificação Etária", ("Ação","Comédia","Terror"))
                clasf_etaria = st.selectbox ("Classificação Etária" , ("Livre" , "6 anos", "10 anos", "12 anos", "14 anos", "16 anos", "18 anos"))
                duracao_filme = st.number_input ("Duração (em minutos)", min_value=0, max_value=500, value=0)
                capa_filmes = st.file_uploader("Capa do Filme", type="image")

                if capa_filmes != None:
                    capa_filmes = capa_filmes.read()

                btn_update = st.form_submit_button("Enviar")

            if btn_update:
                id_filme = db.get_ID_filme_by_name(nome_filme)
                db.update_filme_by_id(id_filme , genero_filme , clasf_etaria , duracao_filme , capa_filmes)




with colunas_inferior [1]:
    st.markdown("##### --- Remoção de Filmes ---", text_alignment="center")

    with st.form("Deletar Filme" , width="stretch"):
        id_deletar = st.number_input("Insira o ID" , min_value=0 , step=1)
        btn_deletar = st.form_submit_button ("Deletar")
    if btn_deletar:
        db.deletar_filme(id_deletar)
