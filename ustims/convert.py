from PIL import Image

# Load the image
image_path = '/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/ustims/segmentation/input/newsample/valid_mask.png'  # Assuming there is a sample image at this path
image = Image.open(image_path)

# Rotate the image by 90 degrees
rotated_image = image.rotate(90, expand=True)

# Save the rotated image
#rotated_image_path = '/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/ustims/segmentation/input/newsample/unknown_mask.png'
rotated_image_path = '/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/ustims/segmentation/input/newsample/valid_mask.png'
rotated_image.save(rotated_image_path)

rotated_image_path