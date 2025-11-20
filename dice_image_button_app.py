
import streamlit as st
import random
from PIL import Image, ImageDraw
import base64
from io import BytesIO

# Dice values and corresponding labels
DICE_VALUES = [0, 2, 4, 6, 8, 10]

# Load dice image and encode to base64
def load_dice_image():
    img = Image.new("RGB", (100, 100), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, 90, 90], outline="black", width=3)
    draw.text((30, 40), "Roll", fill="black")
    return img

def pil_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode()
    return f"data:image/png;base64,{img_base64}"

# Generate the base64 image
img = load_dice_image()
img_url = pil_to_base64(img)

st.title("🎲 Custom Dice Roller (Image Button)")

# Display the roll button image
st.markdown(f'<div style="text-align: center;"><img src="{img_url}" alt="Roll Dice" style="width: 100px; margin-bottom: 10px;"></div>', unsafe_allow_html=True)

# Use a regular button instead of form
if st.button("🎲 Roll Dice", use_container_width=True, type="primary"):
    result = random.choice(DICE_VALUES)
    st.success(f"You rolled a **{result}**!")
