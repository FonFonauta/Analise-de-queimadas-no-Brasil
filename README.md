# Projeto G1 — Tema 3: Análise de Queimadas no Brasil
 ```LINGUAGENS DE PROGRAMAÇÃO
 Professor: Alexandre Neves Louzada
 Aluno: Luis Fernando Dantas Carvalho
```
Projeto de análise e visualização de dados desenvolvido com **Python, Pandas, Plotly e Streamlit**, conforme as exigências do enunciado.

> **Importante:** o dataset fornecido é simulado. As conclusões servem para fins acadêmicos e não representam estatísticas oficiais de queimadas.

## 1. Estrutura

```text
projeto-queimadas-brasil/
├── app.py
├── requirements.txt
├── README.md
├── index.html
├── .gitignore
├── dados/
│   └── simulacao_queimadas_brasil.csv
├── notebooks/
│   └── analise_queimadas.ipynb
├── database/
│   └── README.md
└── imagens/
    └── README.md
```

## 2. Requisitos

- Python 3.10 ou superior
- Pandas
- Plotly
- Streamlit
- Git
- GitHub

## 3. Executar localmente

Abra o terminal dentro da pasta do projeto.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

O navegador abrirá o dashboard local.

## 4. Executar o notebook

Com o ambiente virtual ativado:

```bash
pip install jupyter
jupyter notebook
```

Depois abra:

```text
notebooks/analise_queimadas.ipynb
```

Execute as células em ordem.

## 5. O que foi implementado

O projeto contempla:

- KPIs;
- filtros por ano;
- filtros por mês;
- filtros por região;
- filtros por estado;
- filtros por bioma;
- filtros por nível de risco;
- evolução temporal;
- comparação entre regiões;
- ranking de estados;
- análise por bioma;
- sazonalidade;
- heatmap mensal;
- relação entre seca e queimadas;
- correlação;
- tabela dinâmica;
- interpretação ambiental;
- conclusão executiva.

## 6. Resultados principais encontrados na base

Na base completa:

- Total de focos: **61.803**
- Área total atingida: **24.874,64 km²**
- Estado com mais focos: **GO — 3.379**
- Região com mais focos: **Nordeste — 15.078**
- Mês com mais focos: **outubro — 7.843**
- Bioma com mais focos: **Pantanal — 13.225**
- Média anual: **6.180,3 focos**
- Correlação índice de seca × focos: **0,815**
- De 2015 para 2024, os focos aumentaram aproximadamente **30,2%** na base.

## 7. Publicação no GitHub

Crie um repositório público chamado:

```text
projeto-queimadas-brasil
```

Depois:

```bash
git init
git add .
git commit -m "Projeto G1 - análise de queimadas"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/projeto-queimadas-brasil.git
git push -u origin main
```

## 8. GitHub Pages

No GitHub:

**Settings → Pages → Deploy from a branch → main → /root → Save**

O arquivo `index.html` já está preparado para funcionar como página de apresentação do projeto.

## 9. Streamlit Cloud

No Streamlit Community Cloud:

1. Entre com sua conta GitHub.
2. Escolha o repositório `projeto-queimadas-brasil`.
3. Escolha a branch `main`.
4. Informe `app.py` como arquivo principal.
5. Faça o deploy.

O `requirements.txt` informa as bibliotecas necessárias.

## 10. Entrega

Entregue:

1. Link do GitHub;
2. Link do GitHub Pages;
3. Link do Streamlit;
4. `notebooks/analise_queimadas.ipynb`;
5. `app.py`;
6. `dados/simulacao_queimadas_brasil.csv`.

## 11. Roteiro para apresentação

Uma apresentação curta pode seguir esta ordem:

1. Problema ambiental e objetivo;
2. Explicação da base;
3. Tratamento dos dados;
4. KPIs;
5. Evolução temporal;
6. Regiões e estados mais afetados;
7. Biomas e sazonalidade;
8. Relação seca × queimadas;
9. Conclusão;
10. Demonstração dos filtros do dashboard.

