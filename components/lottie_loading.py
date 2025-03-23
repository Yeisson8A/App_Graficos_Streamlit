import json
from streamlit_lottie import st_lottie_spinner

def create_lotti_loading():
    # Open file by loading
    with open("animations/Lottie-Loading.json", "r",errors='ignore') as f:
        data = json.load(f)

    # Return lottie loading
    return st_lottie_spinner(data, width=600, height=600)