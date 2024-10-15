import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="Meu Site Streamlit")

# Define a function to load the data
@st.cache_data
def carregar_dados():
    try:
        # Load the data from the Excel file
        tabela = pd.read_excel("Merged_4.xlsx")
        return tabela
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load the data
df = carregar_dados()

# Header section
with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")
    st.write("Quer aprender Python? [Clique aqui](https://www.hashtagtreinamentos.com/curso-python)")

# Check if the data is loaded
if df is not None:
    st.write("Data columns:", df.columns)
    
    with st.container():
        st.subheader("Vamos Começar Com Algumas Perguntas Básicas")
        st.title("Ao Final Desse Programa Você Vai Poder Saber Todas As Informações Econômicas E Financeiras Do Seu Empreendimento!")
        st.write("E Melhor, Terá Um Dashboard Completo Com Todas As Avaliações \n [Ou se quiser pode saber mais sobre o melhor empreendimento de Alta Floresta](https://jardimsantacecilia.com.br/) ")
    
    # Area chart section
    with st.container():
        st.write("---")
        
        # Check if the required columns are present
        required_columns = ["key", "df_sum_columns_Entrada", "df_sum_columns_Parcela", "df_sum_columns_Comissao", 
                            "Receita_Distribuivel", "df_Pos_Obra_Mensal", "df_Pre_Obra_Mensal"]
        
        if all(col in df.columns for col in required_columns):
            # Set the 'key' column as the index and plot the area chart
            df.set_index("key", inplace=True)
            st.area_chart(df[["df_sum_columns_Entrada", "df_sum_columns_Parcela", "df_sum_columns_Comissao", 
                              "Receita_Distribuivel", "df_Pos_Obra_Mensal", "df_Pre_Obra_Mensal"]])
        else:
            st.error("One or more required columns are missing from the DataFrame.")
    
    # Form section
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
    
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Slider value:", slider_val, "Checkbox value:", checkbox_val)
    
    st.write("Outside the form")
else:
    st.error("No data available.")
