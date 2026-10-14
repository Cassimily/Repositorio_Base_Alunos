
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Brasileirão", layout="wide")

df = pd.read_csv("Tabela_Clubes.csv")

df["Gols_Feitos"] = df["GolsF/S"].apply(lambda x: int(x.split(":")[0]))
df["Gols_Sofridos"] = df["GolsF/S"].apply(lambda x: int(x.split(":")[1]))

# CORES E ESTILO
st.markdown("""
<style>
.stApp {
    background-color: #101820;
    color: white;
}
h1, h2, h3 {
    color: #00E676;
}
div[data-testid="stMetric"] {
    background-color: #1C2A35;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #00E676;
}
</style>
""", unsafe_allow_html=True)

st.title("⚽ BRASILEIRÃO")
st.caption("Painel de desempenho dos clubes")

# FILTROS
anos = sorted(df["Ano"].unique())
ano = st.sidebar.multiselect("Temporadas", anos, default=anos)

clubes = sorted(df["Clubes"].unique())
clube = st.sidebar.multiselect("Clubes", clubes, default=clubes)

df = df[df["Ano"].isin(ano) & df["Clubes"].isin(clube)]

if df.empty:
    st.warning("Selecione um ano e pelo menos um clube.")
else:
    # CARTÕES
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🏆 Vitórias", int(df["Vitorias"].sum()))
    c2.metric("⚽ Gols feitos", int(df["Gols_Feitos"].sum()))
    c3.metric("🧤 Gols sofridos", int(df["Gols_Sofridos"].sum()))
    c4.metric("🤝 Empates", int(df["Empates"].sum()))

    st.divider()

    # GRÁFICO DE VITÓRIAS
    vitorias = df.groupby("Clubes", as_index=False)["Vitorias"].sum()
    vitorias = vitorias.sort_values("Vitorias", ascending=False)

    g1 = px.bar(
        vitorias, x="Clubes", y="Vitorias",
        title="🏆 Vitórias por clube",
        color="Vitorias",
        color_continuous_scale=["#1C2A35", "#00E676"]
    )
    st.plotly_chart(g1, use_container_width=True)

    # GRÁFICO DE GOLS
    g2 = px.bar(
        df, x="Clubes",
        y=["Gols_Feitos", "Gols_Sofridos"],
        title="⚽ Gols feitos e sofridos",
        barmode="group",
        color_discrete_sequence=["#00E676", "#FF5252"]
    )
    st.plotly_chart(g2, use_container_width=True)

    # TABELA
    st.subheader("📋 Dados dos clubes")
    st.dataframe(df, use_container_width=True)