
import streamlit as st
import random
from PIL import Image
import os

# Dice values and corresponding image paths
DICE_VALUES = [0, 2, 4, 6, 8, 10]
IMAGE_PATHS = {val: f"dice_faces/dice_{val}.png" for val in DICE_VALUES}

st.title("🎲 Custom Dice Roller with Visuals")
st.subheader("Dice faces: 0, 2, 4, 6, 8, 10")

if st.button("Roll the Dice"):
    result = random.choice(DICE_VALUES)
    st.success(f"You rolled a **{result}**!")
    
    img_path = IMAGE_PATHS[result]
    st.image(img_path, caption=f"Face showing: {result}", width=150)
