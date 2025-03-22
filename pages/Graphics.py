import streamlit as st
import pandas as pd
from charts.charts import distrib_cargos_mensuales_estado, porcentaje_cancelacion_genero, porcentaje_cancelacion_pareja, porcentaje_cancelacion_persona_mayor, porcentaje_cancelacion_seguridad_online, porcentaje_cancelacion_tipo_internet, porcentaje_cancelacion_tv_streaming, tasa_cancelacion_cargos_mensuales
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
    # Porcentaje de churn por TV streaming
    fig_tv_streaming = porcentaje_cancelacion_tv_streaming(dataset)
    st.plotly_chart(fig_tv_streaming)

    # Porcentaje de churn por seguridad online
    fig_security_online = porcentaje_cancelacion_seguridad_online(dataset)
    st.plotly_chart(fig_security_online)

    # Porcentaje de churn por tipo de internet
    fig_internet_service = porcentaje_cancelacion_tipo_internet(dataset)
    st.plotly_chart(fig_internet_service)

    # Tasa de churn por monthly charges
    fig_monthly_charges = tasa_cancelacion_cargos_mensuales(dataset)
    st.plotly_chart(fig_monthly_charges)

    # Distribución de monthly charges por estado churn
    fig_distrib_monthly_charges = distrib_cargos_mensuales_estado(dataset)
    st.plotly_chart(fig_distrib_monthly_charges)