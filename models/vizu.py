from PIL import Image

# Open an image file
with Image.open("/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/unknown_mask.png") as img:
    # Get image mode (e.g., RGB, L, etc.)
    mode = img.mode
    # Get image size
    size = img.size
    # Check if the image is RGB
    is_rgb = mode == 'RGB'

    pixel_data = img.getdata()
    # Find the maximum and minimum pixel values
    max_pixel_value = max(pixel_data)
    min_pixel_value = min(pixel_data)
print(size, mode, is_rgb)
print(max_pixel_value,min_pixel_value)

#/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/gt_img.png