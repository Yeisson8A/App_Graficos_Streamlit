import streamlit as st
import pandas as pd
import plotly.express as px
from utils.pandas import preprocess_data

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
    fig1 = px.bar(dataset, x="gender", y="Churn", title=f"Porcentaje de cancelación por género", 
                labels={"gender": "Género", "Churn": "Porcentaje de cancelación"}, 
                barmode='group')
    st.plotly_chart(fig1)

    fig2 = px.bar(dataset, x="SeniorCitizen", y="Churn", title=f"Porcentaje de cancelación por situación de edad", 
                labels={"SeniorCitizen": "Persona mayor?", "Churn": "Porcentaje de cancelación"}, 
                barmode='group')
    st.plotly_chart(fig2)

    fig3 = px.bar(dataset, x="Partner", y="Churn", title=f"Porcentaje de cancelación por situación de pareja", 
                labels={"Partner": "Tiene pareja?", "Churn": "Porcentaje de cancelación"}, 
                barmode='group')
    st.plotly_chart(fig3)
with tab2:
    st.write("Análisis de servicios")