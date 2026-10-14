
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Brasileirão", layout="wide")

df = pd.read_csv("Tabela_Clubes.csv")

df["Gols_Feitos"] = df["GolsF/S"].apply(lambda x: int(x.split(":")[0]))
df["Gols_Sofridos"] = df["GolsF/S"].apply(lambda x: int(x.split(":")[1]))

# ESTILO
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
st.caption("Painel geral de desempenho dos clubes")

# FILTRO DE ANO
anos = sorted(df["Ano"].unique().tolist())
filtro_anos = st.sidebar.multiselect("Temporadas", anos, default=anos)

df = df[df["Ano"].isin(filtro_anos)]

if df.empty:
    st.warning("Selecione pelo menos uma temporada.")
else:
    # CARTÕES
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🌍 Estrangeiros", int(df["Estrangeiros"].sum()))

    with col2:
        idade = df["Idade_Media"].apply(
            lambda x: float(str(x).replace(",", "."))
        ).mean()
        st.metric("👥 Idade média", f"{idade:.1f} anos")

    with col3:
        valor = df["Valor_total"].mean()
        st.metric("💰 Valor médio dos times", f"R$ {valor:,.0f}")

    st.divider()

    # CONTEÚDO EM DUAS COLUNAS
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏆 Pódio das temporadas")

        podio = df[df["Pos."] <= 5][["Ano", "Pos.", "Clubes"]]
        podio = podio.sort_values(["Ano", "Pos."])

        st.dataframe(podio, use_container_width=True, hide_index=True)

    with col2:
        st.subheader("⚽ Total de gols feitos")

        gols = df.groupby("Clubes", as_index=False)["Gols_Feitos"].sum()
        gols = gols.sort_values("Gols_Feitos", ascending=False)

        g1 = px.bar(
            gols,
            x="Clubes",
            y="Gols_Feitos",
            color="Gols_Feitos",
            color_continuous_scale=["#1C2A35", "#00E676"]
        )

        st.plotly_chart(g1, use_container_width=True)

    # GRÁFICO DE VALORES
    st.subheader("📈 Valor dos times ao longo dos anos")

    g2 = px.line(
        df,
        x="Ano",
        y="Valor_total",
        color="Clubes",
        markers=True
    )

    g2.update_layout(
        xaxis_title="Temporada",
        yaxis_title="Valor total do elenco",
        legend_title="Clubes"
    )

    st.plotly_chart(g2, use_container_width=True)

    # TABELA COMPLETA
    st.subheader("📋 Dados completos")
    st.dataframe(df, use_container_width=True, hide_index=True)