# PremierLeague-Predictor 2025

## **Objetivo**  
Criar um aplicativo interativo com **Streamlit** para:  
1. **Exibir os dados atuais** dos 12 primeiros times da tabela da Premier League.  
2. **Mapear visualmente os dados**, incluindo:  
   - Pontuação dos times.  
   - Confrontos diretos restantes.  
   - Histórico de desempenho nos últimos jogos.  
3. **Estimar probabilidades de título** com base em simulações ou modelos matemáticos.  

---

## **Funcionalidades**  

### **1. Carregar e Visualizar Dados**  
- Permitir o upload ou ingestão de dados (ex.: arquivo CSV).  
- Exibir tabela interativa com:  
  - Pontos atuais.  
  - Jogos restantes.  
  - Saldo de gols.  
  - Confrontos diretos entre os times do topo da tabela.  

### **2. Visualizações Gráficas**  
- **Gráfico de barras**: Pontuação atual de cada time.  
- **Mapa de calor**: Confrontos diretos e sua importância para o campeonato.  
- **Gráfico de linha**: Desempenho recente de cada time (ex.: pontos nos últimos 5 jogos).  

### **3. Simulação de Probabilidade**  
- Implementar modelo para estimar as chances de cada time ser campeão considerando:  
  - Pontuação atual.  
  - Confrontos diretos restantes.  
  - Desempenho recente (média de pontos por jogo).  
- Resultados exibidos em:  
  - **Gráfico de pizza** ou **gráfico de barras**.  

### **4. Interface Interativa**  
- Controles para ajustar parâmetros, como:  
  - Fator de peso para desempenho recente.  
  - Probabilidade de vitória em jogos futuros com base em confrontos diretos.  
- Visualização em tempo real das mudanças nas probabilidades.  

---

## **Etapas do Desenvolvimento**  

### **1. Preparar os Dados**  
Criar ou obter um dataset inicial contendo:  
- Nome do time.  
- Pontuação atual.  
- Jogos restantes e adversários.  
- Saldo de gols.  
- Histórico recente de desempenho.  

### **2. Modelo de Probabilidade**  
Usar um modelo estatístico simples, como:  
- **Média de pontos por jogo ajustada**: Estimar a pontuação final com base no desempenho recente.  
- **Simulação Monte Carlo**: Simular resultados dos jogos restantes para calcular a probabilidade de título.  
- Considerar fatores como:  
  - Vantagem em casa.  
  - Histórico de confrontos diretos.  
  - Saldo de gols.  

### **3. Desenvolvimento do App com Streamlit**  
- Criar interface amigável para:  
  - Carregar dados.  
  - Ajustar parâmetros.  
- Visualizações com:  
  - **matplotlib**, **seaborn** ou **plotly**.  

### **4. Implementação do Mapeamento**  
- Utilizar **folium** ou **plotly** para mapas interativos (opcional).  

---

## **Recursos Necessários**  

### **Bibliotecas**  
- `streamlit`: Construção do aplicativo web.  
- `pandas`: Manipulação de dados.  
- `numpy`: Cálculos matemáticos e simulações.  
- `matplotlib`, `seaborn`, `plotly`: Visualizações.  
- `scipy`: Probabilidades e distribuições estatísticas (opcional).  
- `folium`: Para mapas interativos (opcional).  

---

## **Interface do Usuário**  

### **Seção 1: Dados da Tabela**  
- Tabela interativa com times e estatísticas.  

### **Seção 2: Gráficos**  
- Gráfico de barras para pontuação atual.  
- Gráfico de linha para desempenho recente.  

### **Seção 3: Simulação**  
- Probabilidades de título em gráficos interativos.  

### **Seção 4: Configuração**  
- Controles deslizantes para ajustar pesos dos fatores de probabilidade.  

---

## **Desafios e Oportunidades**  

### **Desafios**  
- **Obter dados confiáveis e atualizados.**  
  - **Solução**: Permitir upload de dados personalizados pelo usuário.  

### **Oportunidades**  
- Expandir o aplicativo para incluir análises como:  
  - Probabilidade de rebaixamento.  
  - Qualificação para competições europeias.  
 
