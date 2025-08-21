# CRM Dashboard - Análise Interativa de Clientes

![Dashboard Preview](https://img.shields.io/badge/Status-Ativo-brightgreen)
![Python Version](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange)

---

## 🔹 Sobre o Projeto
Este projeto consiste em um **Dashboard Interativo de CRM**, desenvolvido em **Python** usando **Streamlit**, que permite analisar clientes, produtos, vendas e métricas de marketing de forma visual e intuitiva.

Com este dashboard, é possível:
- Visualizar métricas gerais de clientes e vendas.
- Filtrar dados por período e país.
- Analisar o desempenho de produtos e canais de marketing.
- Observar a distribuição do NPS (Net Promoter Score) dos clientes.
- Ter uma visão geral de todos os gráficos em uma única tela.

## 🖥 Funcionalidades
- Filtro de data e país.
- Métricas principais: Clientes ativos, Receita total, Top cliente, Ticket médio, Total de pedidos, Pedidos por cliente.
- Gráficos:
  - Clientes por país
  - Top produtos vendidos
  - Receita por canal de marketing
  - Distribuição do NPS
- Interface interativa e responsiva.

## ⚡ Tecnologias Utilizadas
- Python 3.10+
- Streamlit
- Pandas
- Plotly
- PyMongo

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
├─ requirements.txt    # Dependências do projeto
├─ README.md           # Documentação
└─ images/             # Screenshots do dashboard
```

## 💡 Melhorias Futuras
- Adicionar autenticação de usuários.
- Implementar filtros avançados (por produto, canal ou categoria).
- Integrar com outras fontes de dados (API externa).
- Adicionar gráficos interativos com Plotly.

## 📫 Contato
Desenvolvido por **Seu Nome**
- GitHub: [seu-usuario](https://github.com/murilorodri-co)
- LinkedIn: [Seu LinkedIn](in/murilo-rodrigues-8153292b9)

---

> Esse projeto é open-source e pode ser utilizado como referência ou adaptado para outros dashboards de análise de clientes.