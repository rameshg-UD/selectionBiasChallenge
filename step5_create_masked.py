import numpy as np

def create_masked_stipple(
    stipple_img: np.ndarray,
    mask_img: np.ndarray,
    threshold: float = 0.5
) -> np.ndarray:

    """
    Apply a block-letter mask to a stippled image.

    Parameters
    ----------
    stipple_img : np.ndarray
        2D array containing the stippled image (values in [0, 1]).
    mask_img : np.ndarray
        2D array of the same shape, containing mask values in [0, 1]
        where 0 = black (mask/remove) and 1 = white (keep).
    threshold : float, optional
        Pixels below this threshold are considered "dark" mask areas
        where stipples will be removed. Default is 0.5.

    Returns
    -------
    np.ndarray
        A masked stippled image. Same shape, values in [0, 1].
    """

    if stipple_img.shape != mask_img.shape:
        raise ValueError("stipple_img and mask_img must have the same shape.")

    # Identify dark mask pixels → remove stipples (set to white)
    mask_dark = mask_img < threshold

    # Apply mask: remove stipples where mask is dark
    masked = np.where(mask_dark, 1.0, stipple_img)

    return masked
