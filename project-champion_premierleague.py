import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random

# ---- CONFIGURAÇÃO DA PÁGINA ----
st.set_page_config(page_title="Premier League Predictor 2025", layout="wide")

# ---- CARREGANDO OS DADOS ----
@st.cache_data
def load_data():
    df = pd.read_csv("PremierDB.csv", delimiter=";")
    return df

df = load_data()

# ---- SIDEBAR ----
st.sidebar.header("⚙️ Configurações")
selected_team = st.sidebar.selectbox("📊 Estatísticas Detalhadas do Time:", df["Equipe"].tolist())

# ---- CABEÇALHO ----
st.title("🏆 Premier League Predictor 2025")
st.markdown("Acompanhe a **classificação**, **confrontos diretos** e **histórico de jogos**.(Dados do dia 17/01/2025)")

# ---- VISUALIZAÇÃO DA TABELA ----
st.subheader("📊 Classificação Atual")
st.dataframe(df.style.format({"Pts/PPJ": "{:.2f}", "xGD/90": "{:.2f}"}))

# ---- GRÁFICO DE PONTUAÇÃO ----
st.subheader("🔢 Pontuação dos Times")
fig = px.bar(df.sort_values(by="Pt", ascending=True), x="Pt", y="Equipe", orientation="h", text="Pt",
             color="Pt", color_continuous_scale="blues")
st.plotly_chart(fig, use_container_width=True)

# ---- CONFRONTOS RESTANTES ----
st.subheader("⚽ Confrontos Diretos Restantes")

# Simulação básica de confrontos
teams = df["Equipe"].tolist()
random.shuffle(teams)
confrontos_restantes = [(teams[i], teams[i+1]) for i in range(0, len(teams)-1, 2)]
confrontos_df = pd.DataFrame(confrontos_restantes, columns=["Time A", "Time B"])
st.table(confrontos_df)

# ---- HISTÓRICO DE DESEMPENHO ----
st.subheader("📈 Histórico dos Últimos 5 Jogos")

historico = df[["Equipe", "Últimos 5"]].copy()
historico["Vitórias"] = historico["Últimos 5"].apply(lambda x: x.count("V"))
historico["Empates"] = historico["Últimos 5"].apply(lambda x: x.count("E"))
historico["Derrotas"] = historico["Últimos 5"].apply(lambda x: x.count("D"))

fig_hist = px.bar(historico, x="Equipe", y=["Vitórias", "Empates", "Derrotas"], barmode="group",
                  title="Resultados dos Últimos 5 Jogos", labels={"value": "Jogos", "variable": "Resultado"})
st.plotly_chart(fig_hist, use_container_width=True)

# ---- ESTATÍSTICAS DETALHADAS ----
st.subheader(f"📌 Estatísticas Detalhadas: {selected_team}")

team_stats = df[df["Equipe"] == selected_team].T
st.table(team_stats)

# ---- EXIBIÇÃO DE CONCLUSÕES ----
st.markdown("### 🔎 Conclusões")
st.markdown("- **Os confrontos diretos podem mudar a classificação.**")
st.markdown("- **Últimos jogos são decisivos na projeção do título.**")

# ---- FINALIZAÇÃO ----
st.markdown("⚽ Criado por Matheus Guerra. Dados fictícios com base na temporada 2025.")
