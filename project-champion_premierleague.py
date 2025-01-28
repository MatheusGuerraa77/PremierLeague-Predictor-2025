import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título e descrição do app

st.title("PremierLeague-Predictor 2025")
st.markdown("""
Um aplicativo interativo para visualizar dados da Premier League e estimar as probabilidades de título dos 12 primeiros times.
""")

# Função para carregar os dados
def load_data(file):
    return pd.read_csv(file)

# Upload de dados
uploaded_file = st.file_uploader("Carregar arquivo CSV com dados da Premier League", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)
    st.write('### Dados Carregados')
    st.dataframe(data)
    
    # Gráfico de barras: Pontuação atual
    st.subheader("Pontuação Atual dos Times")
    fig_bar = px.bar(data, x="Time", y="Pontos", color="Time", title="Pontuação Atual")
    st.plotly_chart(fig_bar)
