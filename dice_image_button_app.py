
import streamlit as st
import random
from PIL import Image, ImageDraw
import base64
from io import BytesIO

# Dice values and corresponding labels
DICE_VALUES = [0, 2, 4, 6, 8, 10]

# Initialize session state for history
if 'roll_history' not in st.session_state:
    st.session_state.roll_history = []

# Load dice image with dots representing the value
def create_dice_image(value):
    """Create a dice image with dots representing the value"""
    img = Image.new("RGB", (100, 100), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([5, 5, 95, 95], outline="black", width=3, fill="white")
    
    # Define dot positions for each value (scaled for 100x100 image)
    dot_positions = {
        0: [],
        2: [(50, 30), (50, 70)],
        4: [(30, 30), (70, 30), (30, 70), (70, 70)],
        6: [(30, 25), (70, 25), (30, 50), (70, 50), (30, 75), (70, 75)],
        8: [(25, 25), (50, 25), (75, 25), (25, 50), (75, 50), (25, 75), (50, 75), (75, 75)],
        10: [(20, 20), (40, 20), (60, 20), (80, 20), (30, 50), (70, 50), (20, 80), (40, 80), (60, 80), (80, 80)]
    }
    
    # Draw dots for the value
    if value in dot_positions:
        for x, y in dot_positions[value]:
            draw.ellipse([x-6, y-6, x+6, y+6], fill="black")
    
    return img

def load_dice_image():
    """Create a roll button image"""
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

# Page configuration
st.set_page_config(page_title="Dice Roller", page_icon="🎲", layout="wide")

# Generate the base64 image for roll button
img = load_dice_image()
img_url = pil_to_base64(img)

st.title("🎲 Enhanced Dice Roller")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    num_dice = st.slider("Number of dice to roll", min_value=1, max_value=5, value=1)
    
    st.header("Statistics")
    if st.session_state.roll_history:
        total_rolls = len(st.session_state.roll_history)
        all_values = [val for roll in st.session_state.roll_history for val in roll]
        st.metric("Total Rolls", total_rolls)
        st.metric("Total Sum", sum(all_values))
        st.metric("Average", f"{sum(all_values)/len(all_values):.2f}")
    else:
        st.info("No rolls yet. Roll the dice to see statistics!")
    
    if st.button("Clear History", use_container_width=True):
        st.session_state.roll_history = []
        st.rerun()

# Main content
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Roll Controls")
    
    # HTML-based image button
    with st.form("image_form", clear_on_submit=True):
        st.markdown(f'''
            <style>
            .img-button {{
                border: none;
                background: none;
                padding: 0;
                cursor: pointer;
            }}
            .img-button img {{
                width: 100px;
                transition: transform 0.2s;
            }}
            .img-button img:hover {{
                transform: scale(1.1);
            }}
            </style>
            <button type="submit" class="img-button">
                <img src="{img_url}" alt="Roll Dice">
            </button>
        ''', unsafe_allow_html=True)
        submitted = st.form_submit_button("Roll Dice", use_container_width=True)

    if submitted:
        results = [random.choice(DICE_VALUES) for _ in range(num_dice)]
        st.session_state.roll_history.append(results)
        st.rerun()

with col2:
    st.subheader("Latest Roll")
    
    if st.session_state.roll_history:
        latest_roll = st.session_state.roll_history[-1]
        
        # Display dice images
        dice_cols = st.columns(min(len(latest_roll), 5))
        for idx, value in enumerate(latest_roll):
            with dice_cols[idx]:
                dice_img = create_dice_image(value)
                dice_img_url = pil_to_base64(dice_img)
                st.markdown(f'''
                    <div style="text-align: center;">
                        <img src="{dice_img_url}" alt="Dice showing {value}" style="width: 100px; margin: 10px;">
                        <p style="font-size: 20px; font-weight: bold;">{value}</p>
                    </div>
                ''', unsafe_allow_html=True)
        
        # Show sum if multiple dice
        if len(latest_roll) > 1:
            st.success(f"🎲 Total: **{sum(latest_roll)}**")
        else:
            st.success(f"🎲 You rolled: **{latest_roll[0]}**")
    else:
        st.info("👆 Click the 'Roll' button to start!")

# Roll history section
if st.session_state.roll_history:
    st.subheader("Roll History")
    
    # Display last 10 rolls
    history_to_show = st.session_state.roll_history[-10:][::-1]  # Last 10, reversed
    
    for idx, roll in enumerate(history_to_show):
        roll_number = len(st.session_state.roll_history) - idx
        roll_sum = sum(roll)
        roll_str = " + ".join(map(str, roll)) if len(roll) > 1 else str(roll[0])
        
        if len(roll) > 1:
            st.text(f"Roll #{roll_number}: {roll_str} = {roll_sum}")
        else:
            st.text(f"Roll #{roll_number}: {roll_str}")
