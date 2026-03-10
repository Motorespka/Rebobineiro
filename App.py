# app.py
import streamlit as st
import pandas as pd

# --- Configurações da página ---
st.set_page_config(
    page_title="Rebobineiro",
    page_icon="🌐",
    layout="wide"
)

# --- Chave mestre ---
CHAVE_MESTRE = "Pablo123"

# --- Inicializa estado de login ---
if "logado" not in st.session_state:
    st.session_state.logado = False

# --- Cabeçalho ---
st.title("🌐 Bem-vindo ao Rebobineiro")
st.markdown("Este site é feito de Rebobinador para Rebobinador!")

# --- Sidebar: Login / Logout ---
st.sidebar.title("Acesso")

if not st.session_state.logado:
    senha = st.sidebar.text_input("Chave mestre", type="password")
    if st.sidebar.button("Entrar"):
        if senha == CHAVE_MESTRE:
            st.session_state.logado = True
            st.sidebar.success("Chave correta! Acesso liberado.")
        else:
            st.sidebar.error("Chave incorreta!")
else:
    st.sidebar.success("Você está logado como Mestre.")
    if st.sidebar.button("Sair"):
        st.session_state.logado = False
        st.experimental_rerun()  # recarrega a página após logout

# --- Sidebar: Menu ---
st.sidebar.title("Menu")

# Consulta e páginas públicas
page = st.sidebar.radio(
    "",
    ["Consultar Cálculo", "Consultar calculo", "Adicionar motor", "Sobre"]
)

# Menu Mestre só aparece se logado
page_mestre = None
if st.session_state.logado:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Mestre")
    page_mestre = st.sidebar.radio(
        "",
        ["Orçamento", "Cadastrar Motor", "Imagem"]
    )

# Define página ativa
if page_mestre:
    page = page_mestre

# --- Navegação ---
# Páginas restritas (Mestre) só acessíveis se logado
menu_mestre_opcoes = ["Orçamento", "Cadastrar Motor", "Imagem"]
if page in menu_mestre_opcoes and not st.session_state.logado:
    st.warning("🔒 Acesso restrito: faça login como Mestre para acessar esta página.")
    st.stop()  # bloqueia conteúdo

# --- Conteúdo das páginas ---
if page == "Consultar Cálculo":
    st.header("Consultar Cálculo")

elif page == "Orçamento":
    st.header("Cadastro de Orçamento")

elif page == "Cadastrar Motor":
    st.header("Cadastro de Motor")

elif page == "Imagem":
    st.header("Cadastro de Imagem")

# --- Página Consulta ---
elif page == "Consultar Calculos":
    st.header("Página Inicial")
    st.write("Aqui você pode colocar informações sobre seu site, projetos ou serviços.")
    st.image("https://via.placeholder.com/600x200.png?text=Imagem+de+Cabeçalho", width=600)

# --- Página Criar calculo ---
elif page == "Adicionar Motor":
    st.header("Visualização de Dados")
    data = {
        "Nome": ["Alice", "Bob", "Carlos", "Diana"],
        "Idade": [25, 30, 22, 28],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.download_button(
        label="Baixar dados",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='dados.csv',
        mime='text/csv'
    )

# --- Página Sobre ---
elif page == "Sobre":
    st.header("Sobre Este Site")
    st.markdown("""
    - Criado com [Streamlit](https://streamlit.io/)
    - Login Mestre permanente na sessão
    - Menu Mestre protegido com opção de logout
    """)


