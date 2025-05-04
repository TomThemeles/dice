
import streamlit as st
import random

# Title and subtitle
st.title("🎲 Custom Dice Roller")
st.subheader("Roll a die with values: 0, 2, 4, 6, 8, 10")

# Button to trigger roll
if st.button("Roll the Dice"):
    result = random.choice([0, 2, 4, 6, 8, 10])
    st.balloons()
    st.success(f"You rolled a **{result}**!")
