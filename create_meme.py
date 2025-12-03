import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize

def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 250,
    background_color: str = "white"
) -> None:
    """
    Assemble a 1x4 statistics meme with four labeled panels:
    Reality, Your Model, Selection Bias, Estimate.

    Saves the meme as a PNG file.
    """

    # Validate shapes
    if not (original_img.ndim == stipple_img.ndim == block_letter_img.ndim == masked_stipple_img.ndim == 2):
        raise ValueError("All input images must be 2D numpy arrays (grayscale).")
    
    # ---- Validate inputs ----
    imgs = [original_img, stipple_img, block_letter_img, masked_stipple_img]

    # ---- Standardize image sizes (resize if necessary) ----
    base_h, base_w = original_img.shape
    processed_imgs = [
        img if img.shape == (base_h, base_w)
        else resize(img, (base_h, base_w), preserve_range=True, anti_aliasing=True)
        for img in imgs
    ]

    if any(img.ndim != 2 for img in imgs):
        raise ValueError("All input images must be 2D numpy arrays (grayscale).")

    # Resize to consistent shape
    h, w = original_img.shape
    processed_imgs = [
        resize(img, (h, w), preserve_range=True, anti_aliasing=True)
        if img.shape != (h, w) else img
        for img in imgs
    ]

    titles = ["Reality", "Your Model", "Selection Bias", "Estimate"]

    # ---- Create figure ----
    fig, axes = plt.subplots(
        1, 4,
        figsize=(6.5, 5),      # wider layout for better panel proportions
        constrained_layout=True,
        dpi=dpi,
        facecolor=background_color
    )

    for ax, img, title in zip(axes, processed_imgs, titles):

        # Display image
        ax.imshow(img, cmap="gray", vmin=0, vmax=1)

        # Remove all axis decorations
        ax.axis('off')

        # Title
        ax.set_title(
            title,
            fontsize=12,
            fontweight="bold",
            pad=6,
        )

    # ---- Save output ----
    fig.savefig(
        output_path,
        bbox_inches="tight",
        dpi=dpi,
        facecolor=background_color,
        pad_inches=0
    )
    plt.close(fig)