import streamlit as st
import pandas as pd
from charts.charts import porcentaje_cancelacion_genero, porcentaje_cancelacion_pareja, porcentaje_cancelacion_persona_mayor
from utils.pandas import preprocess_data

# Configuración de página
st.set_page_config(layout="wide")
st.title("Gráficos")

# Leer archivos
base_path = "data"
contract = pd.read_csv(f"{base_path}\\contract.csv")
internet = pd.read_csv(f"{base_path}\\internet.csv")
personal = pd.read_csv(f"{base_path}\\personal.csv")
phone = pd.read_csv(f"{base_path}\\phone.csv")

# Crear un nuevo dataset con la unión de las tres tablas
dataset = preprocess_data(contract, internet, personal, phone)

tab1, tab2 = st.tabs(["Análisis Demográfico", "Análisis de Servicios"])

with tab1:
    # Porcentaje de churn por género
    fig_gender = porcentaje_cancelacion_genero(dataset)
    st.plotly_chart(fig_gender)

    # Porcentaje de churn por senior citizen
    fig_senior_citizen = porcentaje_cancelacion_persona_mayor(dataset)
    st.plotly_chart(fig_senior_citizen)

    # Porcentaje de churn por partner
    fig_partner = porcentaje_cancelacion_pareja(dataset)
    st.plotly_chart(fig_partner)
with tab2:
    st.write("Análisis de servicios")