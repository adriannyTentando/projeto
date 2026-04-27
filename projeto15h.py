import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    data = pd.read_excel('Base.xlsx',sheet_name='Base')
    title = 'Dashboard - Projeto Vendas'
    st.set_page_config(page_title=title, layout ='Wide')
    st.title(title)

    ano = data['Ano'].unique()
    paises = data['país'].unique()

    filtro_Ano = st.sidebar.selectbox("selecione o Ano:", options=['todos'] + sorted(ano), index=0)
    filtro_pais = st.sidebar.selectbox("selecione o País:", options=['todos'] + sorted(paises), index=0)

    data_filtrada = data.copy()
    if filtro_Ano != 'todos':
        data_filtrada = data_filtrada[data_filtrada['Ano'] == filtro_Ano]
    if filtro_pais != 'todos':
        data_filtrada = data_filtrada[data_filtrada['País'] == filtro_pais]

    gf_lucroporsegmento = px.bar(
    data_filtrada.groupby('Segmento')['Lucro'].sum().reset_index(),
    x = 'Segmento', y = 'Lucro',
    title= 'Lucro por Segmento',
    color= "Segmento",
    text_auto=True
    )
    gf_lucroporsegmento.update_layout(showlegend=False)

main()