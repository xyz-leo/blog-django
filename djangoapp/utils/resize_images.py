from pathlib import Path  # For working with filesystem paths in an object-oriented way
from django.conf import settings  # To access Django project settings (like MEDIA_ROOT)
from PIL import Image  # Pillow library for image processing


def resize_image(image_django, new_width=800, optimize=True, quality=60):
    """
    Resize an uploaded Django image to a specified maximum width while maintaining its aspect ratio.

    Args:
        image_django: The Django image object (typically from an ImageField or FileField).
        new_width (int): The maximum width of the image in pixels (default is 800).
        optimize (bool): Whether to optimize the output file size (default is True).
        quality (int): Compression quality for the output image (1–100, default is 60).

    Returns:
        PIL.Image.Image: The resized image object (Pillow Image instance).
    """

    # Build the absolute path to the uploaded image file inside MEDIA_ROOT
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()

    # Open the image file using Pillow
    image_pillow = Image.open(image_path)

    # Get the original dimensions (width, height)
    original_width, original_height = image_pillow.size

    # If the image is already smaller than or equal to the target width, do nothing
    if original_width <= new_width:
        image_pillow.close()  # Close the file handle to free resources
        return image_pillow   # Return the original (unmodified) image

    # Calculate the new height to maintain the original aspect ratio
    new_height = round(new_width * original_height / original_width)

    # Resize the image using the LANCZOS filter (high-quality downsampling)
    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)

    # Save the resized image to the same path, with optimization and compression applied
    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    # Return the resized image object
    return new_image
