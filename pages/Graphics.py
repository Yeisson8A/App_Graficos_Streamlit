import time
import streamlit as st
import pandas as pd
from components.lottie_loading import create_lotti_loading
from utils.pandas import preprocess_data
from views.graphics_view import show_graphics

# Configuración de página
st.set_page_config(layout="wide")

# Leer archivos
base_path = "data"
contract = pd.read_csv(f"{base_path}/contract.csv")
internet = pd.read_csv(f"{base_path}/internet.csv")
personal = pd.read_csv(f"{base_path}/personal.csv")
phone = pd.read_csv(f"{base_path}/phone.csv")

# Crear un nuevo dataset con la unión de las tres tablas
dataset = preprocess_data(contract, internet, personal, phone)

# Loading
with create_lotti_loading():
    time.sleep(1)
    st.title("Gráficos")
    show_graphics(dataset)