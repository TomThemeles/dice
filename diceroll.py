import streamlit as st
import random

DICE_FACES = {
    0: "🛡️ Block",
    2: "⚔️ Light Attack",
    4: "🔥 Heavy Attack",
    6: "💀 Critical Hit",
    8: "🩸 Bleed",
    10: "☠️ Fatal Blow"
}

st.title("⚔️ Battle Dice Roller")

if st.button("Roll the Battle Dice"):
    result = random.choice(list(DICE_FACES.keys()))
    st.markdown(f"### You rolled a **{result}**")
    st.markdown(f"## {DICE_FACES[result]}")
