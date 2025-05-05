import streamlit as st
import random

st.set_page_config(page_title="Battle Dice", layout="centered")

DICE_VALUES = [0, 2, 4, 6, 8, 10]

# Dice image button using HTML
with st.form("dice_form", clear_on_submit=True):
    st.markdown(
        """
        <style>
        .roll-btn {
            border: none;
            background: none;
        }
        .roll-img {
            width: 120px;
            cursor: pointer;
        }
        </style>
        <button class="roll-btn" type="submit">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/6sided_dice.svg/120px-6sided_dice.svg.png" class="roll-img" />
        </button>
        """,
        unsafe_allow_html=True
    )
    submitted = st.form_submit_button()

if submitted:
    result = random.choice(DICE_VALUES)
    st.markdown(f"### 🎯 You rolled a **{result}**!")