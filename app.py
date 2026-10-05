import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análise de Queimadas no Brasil",
    page_icon="🔥",
    layout="wide"
)

@st.cache_data
def carregar_dados():
    caminho = "dados/simulacao_queimadas_brasil.csv"
    df = pd.read_csv(caminho)
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df["ano"] = df["ano"].astype(int)
    df["mes"] = df["mes"].astype(int)
    return df

df = carregar_dados()

st.title("🔥 Análise de Queimadas no Brasil")
st.markdown(
    "Dashboard analítico dos focos de queimadas no período de **2015 a 2024**, "
    "com análise temporal, regional, estadual, por bioma, sazonalidade e risco."
)
st.markdown(
    "Linguagens de Programação "
    )
    st.markdown(
    "Professor: Alexandre Neves Louzada "
        )
    st.markdown(
    "Aluno: Luis Fernando Dantas Carvalho "
)
)
with st.sidebar:
    st.header("Filtros")
    anos = st.multiselect("Ano", sorted(df["ano"].unique()), default=sorted(df["ano"].unique()))
    meses = st.multiselect("Mês", list(range(1, 13)), default=list(range(1, 13)))
    regioes = st.multiselect("Região", sorted(df["regiao"].unique()), default=sorted(df["regiao"].unique()))
    estados = st.multiselect("Estado (UF)", sorted(df["uf"].unique()), default=sorted(df["uf"].unique()))
    biomas = st.multiselect("Bioma", sorted(df["bioma"].unique()), default=sorted(df["bioma"].unique()))
    riscos = st.multiselect(
        "Nível de risco",
        ["Baixo", "Médio", "Alto", "Crítico"],
        default=["Baixo", "Médio", "Alto", "Crítico"]
    )

    st.divider()
    st.caption("Base: simulacao_queimadas_brasil.csv")

filtrado = df[
    df["ano"].isin(anos)
    & df["mes"].isin(meses)
    & df["regiao"].isin(regioes)
    & df["uf"].isin(estados)
    & df["bioma"].isin(biomas)
    & df["nivel_risco"].isin(riscos)
].copy()

if filtrado.empty:
    st.warning("Nenhum registro corresponde aos filtros selecionados.")
    st.stop()

total_focos = int(filtrado["focos_queimada"].sum())
area_total = filtrado["area_atingida_km2"].sum()
estado_top = filtrado.groupby("uf")["focos_queimada"].sum().idxmax()
regiao_top = filtrado.groupby("regiao")["focos_queimada"].sum().idxmax()
mes_top = int(filtrado.groupby("mes")["focos_queimada"].sum().idxmax())
media_anual = filtrado.groupby("ano")["focos_queimada"].sum().mean()

k1, k2, k3, k4, k5, k6 = st.columns(6)
k1.metric("Total de focos", f"{total_focos:,}".replace(",", "."))
k2.metric("Área atingida", f"{area_total:,.2f} km²".replace(",", "X").replace(".", ",").replace("X", "."))
k3.metric("Estado mais afetado", estado_top)
k4.metric("Região mais crítica", regiao_top)
k5.metric("Mês mais crítico", mes_top)
k6.metric("Média anual", f"{media_anual:,.1f}".replace(",", "X").replace(".", ",").replace("X", "."))

st.subheader("Evolução temporal")
temporal = filtrado.groupby("data", as_index=False)["focos_queimada"].sum()
fig_tempo = px.line(
    temporal, x="data", y="focos_queimada", markers=True,
    title="Evolução mensal dos focos de queimadas"
)
fig_tempo.update_layout(xaxis_title="Data", yaxis_title="Focos")
st.plotly_chart(fig_tempo, use_container_width=True)

c1, c2 = st.columns(2)

with c1:
    reg = filtrado.groupby("regiao", as_index=False)["focos_queimada"].sum().sort_values("focos_queimada", ascending=False)
    fig_reg = px.bar(reg, x="regiao", y="focos_queimada", title="Focos por região", text_auto=True)
    st.plotly_chart(fig_reg, use_container_width=True)

with c2:
    estados_df = filtrado.groupby("uf", as_index=False)["focos_queimada"].sum().sort_values("focos_queimada", ascending=False)
    fig_est = px.bar(estados_df, x="uf", y="focos_queimada", title="Ranking de estados", text_auto=True)
    st.plotly_chart(fig_est, use_container_width=True)

c3, c4 = st.columns(2)

with c3:
    bio = filtrado.groupby("bioma", as_index=False)["focos_queimada"].sum().sort_values("focos_queimada", ascending=False)
    fig_bio = px.bar(bio, x="bioma", y="focos_queimada", title="Focos por bioma", text_auto=True)
    st.plotly_chart(fig_bio, use_container_width=True)

with c4:
    saz = filtrado.groupby("mes", as_index=False)["focos_queimada"].sum()
    fig_saz = px.bar(saz, x="mes", y="focos_queimada", title="Sazonalidade mensal", text_auto=True)
    fig_saz.update_layout(xaxis=dict(dtick=1), xaxis_title="Mês", yaxis_title="Focos")
    st.plotly_chart(fig_saz, use_container_width=True)

st.subheader("Heatmap mensal")
heat = filtrado.pivot_table(
    index="mes", columns="ano", values="focos_queimada",
    aggfunc="sum", fill_value=0
)
fig_heat = px.imshow(
    heat, aspect="auto", text_auto=True,
    labels=dict(x="Ano", y="Mês", color="Focos"),
    title="Heatmap de focos por mês e ano"
)
st.plotly_chart(fig_heat, use_container_width=True)

st.subheader("Relação entre seca e queimadas")
fig_scatter = px.scatter(
    filtrado,
    x="indice_seca",
    y="focos_queimada",
    color="nivel_risco",
    hover_data=["ano", "mes", "uf", "regiao", "bioma"],
    trendline="ols",
    title="Índice de seca × focos de queimadas"
)
fig_scatter.update_layout(xaxis_title="Índice de seca", yaxis_title="Focos")
st.plotly_chart(fig_scatter, use_container_width=True)

corr = filtrado[["indice_seca", "focos_queimada"]].corr().iloc[0, 1]
st.info(
    f"**Interpretação:** na seleção atual, a correlação de Pearson entre índice de seca "
    f"e quantidade de focos é **{corr:.3f}**. Valores positivos indicam que, nesta base, "
    "maiores índices de seca tendem a acompanhar maior quantidade de focos. "
    "Correlação não significa, sozinha, causalidade."
)

st.subheader("Tabela dinâmica")
tabela = pd.pivot_table(
    filtrado,
    index="uf",
    columns="ano",
    values="focos_queimada",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="Total"
)
st.dataframe(tabela, use_container_width=True)

st.subheader("Interpretação ambiental")
total_base = df["focos_queimada"].sum()
top_base_estado = df.groupby("uf")["focos_queimada"].sum().idxmax()
top_base_regiao = df.groupby("regiao")["focos_queimada"].sum().idxmax()
top_base_mes = int(df.groupby("mes")["focos_queimada"].sum().idxmax())
top_base_bioma = df.groupby("bioma")["focos_queimada"].sum().idxmax()
corr_base = df[["indice_seca", "focos_queimada"]].corr().iloc[0, 1]

st.write(
    f"A base completa possui **{total_base:,} focos**. O estado com maior total é "
    f"**{top_base_estado}**, a região líder é o **{top_base_regiao}**, o mês de maior "
    f"ocorrência é **{top_base_mes}** e o bioma com maior número de focos é "
    f"**{top_base_bioma}**. A correlação entre índice de seca e focos é "
    f"**{corr_base:.3f}**, indicando associação positiva forte na base simulada."
)

st.subheader("Conclusão executiva")
st.write(
    "Os resultados indicam concentração relevante das queimadas em determinadas regiões, "
    "estados, biomas e meses. A evolução anual também deve ser acompanhada, pois a série "
    "permite identificar períodos de aumento e redução. O índice de seca apresenta associação "
    "positiva com os focos, reforçando a importância do monitoramento climático e da prevenção "
    "em períodos de maior estiagem. Como os dados são simulados, as conclusões devem ser "
    "interpretadas como exercício analítico, e não como retrato oficial das queimadas no Brasil."
)

st.caption("Projeto G1 — Tema 3 | Python + Pandas + Plotly + Streamlit")
