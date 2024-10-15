import pandas as pd
import requests
import io
import streamlit as st

st.set_page_config(page_title="Bem Vindo A Revolução Dos Projetos Imobiliários")

# Use the raw GitHub link to your .xlsx file
url = "https://raw.githubusercontent.com/ferrazbenedito/sttest/main/Merged_4.xlsx"

# Fetch the file using requests
response = requests.get(url)

# Ensure the response is valid before attempting to load the Excel file
if response.status_code == 200:
    # Read the Excel file from the response content, specify the engine
    df = pd.read_excel(io.BytesIO(response.content), engine='openpyxl')
else:
    st.error(f"Failed to load data. Status code: {response.status_code}")

with st.container():
    st.subheader("Vamos Começar Com Algumas Perguntas Básicas")
    st.title("Ao Final Desse Programa Voçê Vai Poder Saber Todas As Infomações Econômicas E Financeiras Do Seu Empreendimento!")
    st.write("E Melhor, Tera Um Dashboard Completo Com Todas As Avaliações \n [Ou se quiser pode saber mais sobre o melhor empreendimento de Alta Floresta](https://jardimsantacecilia.com.br/)")

with st.container():
    st.write("---")
    st.area_chart(data=df, x="key", y=["df_sum_columns_Entrada", "df_sum_columns_Parcela", "df_sum_columns_Comissao", "Receita_Distribuivel", "df_Pos_Obra_Mensal", "df_Pre_Obra_Mensal"])

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
