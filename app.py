import streamlit as st
import pandas as pd
from pymongo import MongoClient
from datetime import datetime

st.set_page_config(
    page_title="Análise Interativa de CRM",
    page_icon="📅",
    layout="wide"
)

# Criando conexão com MongoDB Atlas
client = MongoClient("mongodb+srv://Murilo-Rodrigues:jvgJ2HWi4LGadTsb@projeto-crm.61mpa2x.mongodb.net/?retryWrites=true&w=majority&appName=Projeto-CRM")
db = client.crm
clientes = db.clientes

# Carregando dados do MongoDB
cursor = clientes.find({})
data = list(cursor)
df = pd.DataFrame(data)

# Identificando a coluna de data
possible_date_cols = ['date', 'Date', 'DATE', 'purchase_date']
date_col = None
for col in possible_date_cols:
    if col in df.columns:
        date_col = col
        break

if date_col is None:
    st.warning("Não foi encontrada coluna de data. Usando datas fictícias.")
    df['date_dummy'] = pd.to_datetime('2025-01-01')
    date_col = 'date_dummy'
else:
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

# Criando sidebar interativa
st.sidebar.header("Filtros")
data_min = df[date_col].min()
data_max = df[date_col].max()
data_corte = st.sidebar.date_input(
    "Mostrar clientes ativos a partir de:",
    value=data_min,
    min_value=data_min,
    max_value=data_max
)

if 'customer_country' in df.columns:
    with st.sidebar.expander("Filtrar por país"):
        pais = st.multiselect(
            "Selecione os países:",
            options=df['customer_country'].unique(),
            default=df['customer_country'].unique()
        )
else:
    pais = None

df_filtrado = df[df[date_col] >= pd.to_datetime(data_corte)]
if pais is not None:
    df_filtrado = df_filtrado[df_filtrado['customer_country'].isin(pais)]

st.title("Dashboard da análise explorativa dos clientes 📊")

tabs = st.tabs([
    "Métricas gerais",
    "Clientes por país",
    "Top produtos",
    "Receita por canal",
    "Distribuição NPS",
])

# Criando aba de métricas gerais
with tabs[0]:
    st.subheader("Métricas gerais")
    st.write("Número total de clientes ativos, receita total e cliente que mais gastou.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Clientes ativos", df_filtrado['first_name'].nunique() if 'first_name' in df_filtrado.columns else 0)
    col2.metric("Receita total", f"${df_filtrado['revenue'].sum():,.2f}" if 'revenue' in df_filtrado.columns else "$0.00")
    if 'first_name' in df_filtrado.columns and 'revenue' in df_filtrado.columns and not df_filtrado.empty:
        top_cliente = df_filtrado.groupby('first_name')['revenue'].sum().sort_values(ascending=False).head(1)
        col3.metric("Top cliente", f"{top_cliente.index[0]} (${top_cliente.values[0]:,.2f})")
    else:
        col3.metric("Top cliente", "N/A")

# Criando aba de clientes ativos por país
with tabs[1]:
    st.subheader("Clientes ativos por país")
    st.write("Quantidade de clientes ativos distribuídos por país.")
    
    if 'customer_country' in df_filtrado.columns:
        ativos_por_pais = df_filtrado['customer_country'].value_counts()
        st.bar_chart(ativos_por_pais)
    else:
        st.write("Coluna 'customer_country' não encontrada.")

# Criando aba com Top 5 produtos mais vendidos
with tabs[2]:
    st.subheader("Top 5 produtos mais vendidos")
    st.write("Os cinco produtos com maior quantidade de vendas.")
    
    if 'product_name' in df_filtrado.columns and 'quantity' in df_filtrado.columns:
        top_produtos = df_filtrado.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(5)
        st.bar_chart(top_produtos)
    else:
        st.write("Colunas 'product_name' ou 'quantity' não encontradas.")

# Criando aba de receita por canal de marketing
with tabs[3]:
    st.subheader("Receita por canal de marketing")
    st.write("Receita total gerada por cada canal de marketing.")
    
    if 'marketing_channel' in df_filtrado.columns and 'revenue' in df_filtrado.columns:
        receita_canal = df_filtrado.groupby('marketing_channel')['revenue'].sum().sort_values(ascending=False)
        st.bar_chart(receita_canal)
    else:
        st.write("Colunas 'marketing_channel' ou 'revenue' não encontradas.")

# Criando aba de distribuição de NPS
with tabs[4]:
    st.subheader("Distribuição do NPS")
    st.write("Distribuição das pontuações NPS (Net Promoter Score) dos clientes.")
    
    if 'nps_score' in df_filtrado.columns:
        st.bar_chart(df_filtrado['nps_score'].value_counts().sort_index())
    else:
        st.write("Coluna 'nps_score' não encontrada.")