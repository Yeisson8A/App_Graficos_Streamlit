from streamlit_card import card
from utils.utils import convert_image_to_base64

def create_card(title, text, url, key, image_path):
    image_data = None

    if not image_path is None:
        image_data = convert_image_to_base64(image_path)

    card(
        title=title,
        text=text,
        image=image_data,
        url=url,
        key=key,
        styles={
            "card": {
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                "background-color": "white",
                "background-size": "contain"
            },
            "text": {
                "font-family": "serif"
            }
        }
    )