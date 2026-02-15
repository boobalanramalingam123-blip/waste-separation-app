import streamlit as st
from PIL import Image
import geocoder

st.title("♻ Waste Separation App")

st.write("Upload an image to detect waste type")

# Upload Image
uploaded_file = st.file_uploader("Upload Waste Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Example Detection Logic
    file_name = uploaded_file.name.lower()

    if "iron" in file_name:
        waste_type = "Metal - Iron"
    elif "copper" in file_name:
        waste_type = "Metal - Copper"
    elif "plastic" in file_name:
        waste_type = "Plastic"
    elif "glass" in file_name:
        waste_type = "Glass"
    else:
        waste_type = "Unknown Waste Type"

    st.success(f"Detected Waste Type: {waste_type}")

# Location Detection
st.write("Click below to detect your location")

if st.button("Detect My Location"):
    g = geocoder.ip('me')

    if g.ok:
        city = g.city

        st.success("📍 Your Location Details:")
        st.info(f"City: {city}")
    else:
        st.error("Unable to detect location")
