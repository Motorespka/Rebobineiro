import streamlit as st
import pandas as pd

# --- Configurações ---
st.set_page_config(page_title="Rebobineiro", page_icon="🌐", layout="wide")

CHAVE_MESTRE = "Pablo123"

# Inicializa estado de login
if "logado" not in st.session_state:
    st.session_state.logado = False

# Cabeçalho
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
        st.experimental_rerun()

# --- Sidebar: Menu ---
st.sidebar.title("Menu")

# Páginas públicas
pagina_publica = st.sidebar.radio("", ["Consultar Cálculo", "Home", "Dados", "Sobre"])
page = pagina_publica  # valor inicial da página

# Páginas Mestre (só se logado)
pagina_mestre = None
if st.session_state.logado:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Mestre")
    pagina_mestre = st.sidebar.radio("", ["Orçamento", "Cadastrar Motor", "Imagem"])
    if pagina_mestre:
        page = pagina_mestre

# Bloqueio de páginas Mestre se não estiver logado
if page in ["Orçamento", "Cadastrar Motor", "Imagem"] and not st.session_state.logado:
    st.warning("🔒 Acesso restrito: faça login como Mestre para acessar esta página.")
    st.stop()

# --- Conteúdo das páginas ---
if page == "Consultar Cálculo":
    st.header("Consultar Cálculo")

elif page == "Home":
    st.header("Página Inicial")
    st.write("Aqui você pode colocar informações sobre seu site, projetos ou serviços.")
    st.image("https://via.placeholder.com/600x200.png?text=Imagem+de+Cabeçalho", width=600)

elif page == "Dados":
    st.header("Visualização de Dados")
    df = pd.DataFrame({
        "Nome": ["Alice", "Bob", "Carlos", "Diana"],
        "Idade": [25, 30, 22, 28],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
    })
    st.dataframe(df)
    st.download_button(
        label="Baixar dados",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='dados.csv',
        mime='text/csv'
    )

elif page == "Sobre":
    st.header("Sobre Este Site")
    st.markdown("""
    - Criado com [Streamlit](https://streamlit.io/)
    - Login Mestre permanente na sessão
    - Menu Mestre protegido com opção de logout
    """)

# --- Páginas Mestre ---
elif page == "Orçamento":
    st.header("Cadastro de Orçamento")

elif page == "Cadastrar Motor":
    st.header("Cadastro de Motor")

elif page == "Imagem":
    st.header("Cadastro de Imagem")
