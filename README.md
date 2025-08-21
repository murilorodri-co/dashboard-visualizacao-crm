# CRM Dashboard - Análise Interativa de Clientes

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.26-orange)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen)

## Sobre o Projeto
Este projeto consiste em um **Dashboard Interativo de CRM** desenvolvido com **Python** e **Streamlit**, permitindo análise explorativa de clientes e métricas de vendas. O diferencial deste projeto é a **integração com o MongoDB Atlas**, que armazena todos os dados de clientes, produtos, pedidos e métricas de marketing, possibilitando consultas dinâmicas e atualizações em tempo real.

## Funcionalidades
- Visualização de **métricas gerais**: clientes ativos, receita total, top cliente, ticket médio e total de pedidos.
- Análise de **clientes por país**.
- Ranking dos **top produtos mais vendidos**.
- Receita por **canais de marketing**.
- Distribuição de **NPS (Net Promoter Score)**.
- Filtro por **data** e por **país**.
- Visualização compacta de todos os gráficos para rápida análise.

## Tecnologias Utilizadas
- **Python 3.12**
- **Streamlit** para visualização interativa
- **MongoDB Atlas** para armazenamento e consulta de dados
- **Pandas** para manipulação de dados
- **Plotly** para gráficos customizados

## 🚀 Como Executar Localmente
1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/dashboard-visualizacao-crm.git
cd crm-dashboard
```

2. Crie e ative um ambiente virtual (opcional, recomendado):
```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o app:
```bash
streamlit run app.py
```

## 🌐 Deploy
Você pode disponibilizar seu dashboard online usando **[Streamlit Cloud](https://streamlit.io/cloud)** ou outro serviço de hospedagem Python.

Exemplo de link público: [Clique aqui para acessar](https://share.streamlit.io/seu-usuario/crm-dashboard/main/app.py)

## 📝 Estrutura do Repositório
```
crm-dashboard/
│
├─ app.py              # Arquivo principal do Streamlit
├─ Digital Sales - Customer Data.csv           # Dataset
├─ requirements.txt    # Dependências do projeto
├─ README.md           # Documentação
```

## 📫 Contato
Desenvolvido por **Murilo Rodrigues**
- GitHub: https://github.com/murilorodri-co
- LinkedIn: [in/murilo-rodrigues-8153292b9](https://www.linkedin.com/in/murilo-rodrigues-8153292b9)

---
