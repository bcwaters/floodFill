# README: Flood Fill Oval Interior Script

## Overview

This Python script uses the Pillow library to perform a flood fill operation specifically designed to fill the interior of an oval shape in an image, respecting any transparent areas. The script automatically detects a starting point for the flood fill and ensures that only the solid interior of the oval is filled. It now properly handles command-line arguments for input and output image paths and uses the correct `floodfill` function from the `Image` module.

## Features

- **Automatic Starting Point Detection**: Searches for the first non-transparent pixel from the top of the image.
- **Interior Filling Only**: Ensures that only the interior of the oval is filled, stopping at transparent areas.
- **Error Handling**: Provides feedback if no non-transparent pixels are found or if the command-line arguments are incorrect.
- **Command-Line Argument Handling**: Accepts input and output image paths as command-line arguments.
- **Correct Flood Fill Implementation**: Uses `Image.floodfill()` instead of `ImageDraw.floodfill()`.

## Prerequisites

- Python 3.7+
- Pillow (PIL) library

## Setup Environment with `uv`

To set up your environment using `uv`, follow these steps:

1. **Install `uv`**:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Create a Virtual Environment**:
   ```bash
   uv venv
   ```

3. **Activate the Virtual Environment**:
   - On Unix or MacOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```cmd
     .venv\\\\Scripts\\\\activate
     ```

4. **Install Dependencies**:
   ```bash
   uv pip install Pillow
   ```

## Usage

1. **Place your input image** in the same directory as the script or provide the full path.
2. **Run the script**:
   ```bash
   python flood_fill.py input_image.png output_filled_image.png
   ```

## Code
