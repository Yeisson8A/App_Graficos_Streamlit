import time
import streamlit as st
from components.lottie_loading import create_lotti_loading
from views.projects_view import show_projects

# Configuración de página
st.set_page_config(layout="wide")

# Loading
with create_lotti_loading():
    time.sleep(1)
    st.title("Proyectos")
    show_projects()