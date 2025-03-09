import base64

def convert_image_to_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")
    return data