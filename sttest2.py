import streamlit as st
import pandas as pd 
import numpy as np

st.set_page_config(page_title= "Bem Vindo A Revolução Dos Projetos Imobiliários")

df = pd.read_csv("https://raw.githubusercontent.com/ferrazbenedito/sttest/refs/heads/main/Merged_4_semicolon_separated.csv", sep=';')

with st.container():
    st.subheader("Vamos Começar Com Algumas Perguntas Básicas")

    st.title("Ao Final Desse Programa Voçê Vai Poder Saber Todas As Infomações Econômicas E Financeiras Do Seu Empreendimento!")

    st.write("E Melhor, Tera Um Dashboard Completo Com Todas As Avaliações \n [Ou se quiser pode saber mais sobre o melhor empreendimento de Alta Floresta](https://jardimsantacecilia.com.br/) ")

with st.container():
    st.write("---")

    st.area_chart(data= df, x= "key", y= ["df_sum_columns_Entrada",	"df_sum_columns_Parcela",	"df_sum_columns_Comissao"	,"Receita_Distribuivel",	"df_Pos_Obra_Mensal",	"df_Pre_Obra_Mensal"])


with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")




st.write("Outside the form")
