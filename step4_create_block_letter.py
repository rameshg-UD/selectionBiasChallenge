import numpy as np
from PIL import Image, ImageDraw, ImageFont

"""
    Create a block letter image (default: 'A') as a 2D numpy array.

    Parameters
    ----------
    height : int
        Output image height.
    width : int
        Output image width.
    letter : str, optional
        Letter to draw. Default is "A".
    font_size_ratio : float, optional
        Fraction of the smallest image dimension to use as font size.
        Default is 0.9.

    Returns
    -------
    np.ndarray
        A 2D array of shape (height, width) with values in [0, 1].
        1.0 = white background, 0.0 = black letter.
"""

def Create_block_letter(
    height: int, 
    width: int, 
    letter: str = "S", 
    font_size_ratio: 
    float = 0.9) -> np.ndarray:

        # Create blank white image
    top_margin: int =0
    img = Image.new("L", (width, height), color=255)
    draw = ImageDraw.Draw(img)

    # Determine font size based on image dimensions
    font_size = int(min(height, width) * font_size_ratio)

    # Try multiple common font paths (bold fonts preferred)
    possible_fonts = [
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "arialbd.ttf"
    ]

    font = None
    for path in possible_fonts:
        try:
            font = ImageFont.truetype(path, font_size)
            break
        except:
            continue

    # Fallback to PIL default if no font loads
    if font is None:
        font = ImageFont.load_default()

    # Compute text size to center it
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (width - text_w) // 2
   # ----- Vertical top alignment -----
    # bbox[1] is typically negative -> compensates baseline offset
    y = -bbox[1] + top_margin
    # ----------------------------------
    # Draw the letter in black
    draw.text((x, y), letter, fill=0, font=font)

    # Convert to normalized NumPy array in [0, 1]
    arr = np.array(img, dtype=np.float32) / 255.0

    return arr
