# 🎲 Enhanced Dice Roller

A beautiful and interactive dice rolling application built with Streamlit. This application allows you to roll custom dice with even values (0, 2, 4, 6, 8, 10) and track your rolling history with comprehensive statistics.

## Features

- **Visual Dice Display**: Dice faces with dots representing the values
- **Multiple Dice Rolling**: Roll 1-5 dice simultaneously
- **Roll History**: Track your last 10 rolls
- **Statistics Dashboard**: View total rolls, sum, and average
- **Interactive UI**: Hover effects and smooth animations
- **Clear History**: Reset your rolling history anytime

## Installation

1. Clone this repository:
```bash
git clone https://github.com/TomThemeles/dice.git
cd dice
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application with:
```bash
streamlit run dice_image_button_app.py
```

The application will open in your default web browser. If it doesn't open automatically, navigate to `http://localhost:8501` in your browser.

## How to Use

1. **Set Number of Dice**: Use the slider in the sidebar to select how many dice to roll (1-5)
2. **Roll Dice**: Click the "Roll" button or the dice image to roll
3. **View Results**: See the dice faces with dots and the total sum
4. **Check Statistics**: View rolling statistics in the sidebar
5. **View History**: Scroll down to see your last 10 rolls
6. **Clear History**: Click "Clear History" in the sidebar to reset

## Dice Values

The dice use custom even values:
- 0 (blank)
- 2 (two dots)
- 4 (four dots)
- 6 (six dots)
- 8 (eight dots)
- 10 (ten dots)

## Requirements

- Python 3.7+
- Streamlit 1.51.0+
- Pillow 12.0.0+

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
