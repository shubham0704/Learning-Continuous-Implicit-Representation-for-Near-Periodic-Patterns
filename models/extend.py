from PIL import Image

# Load the original image
image_path = '/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/temp/gt_img.png'  # Replace with your image path
original_img = Image.open(image_path)

# Define the size of the grey borders
border_size = 120  # This is the height of the top and bottom borders

# Create a new image with grey borders
new_width = original_img.width
new_height = original_img.height + 2 * border_size
new_img = Image.new('RGB', (new_width, new_height), 'grey')  # 'grey' can be replaced with an RGB tuple like (128, 128, 128)

# Paste the original image onto the new image, centered between the top and bottom borders
new_img.paste(original_img, (0, border_size))

# Save or display the new image
new_img.save('/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/image_with_grey_borders.png')  # Save the image
# new_img.show()  # Uncomment to display the image
