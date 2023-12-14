# Open the image again
from PIL import Image


with Image.open("/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/gt_img.png") as img:
    # Create a white square patch

    grayscale_image = img.convert("RGB")  # "L" mode is for grayscale
    # Save the grayscale image
    grayscale_image_path = "/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/gt_img.png"
    grayscale_image.save(grayscale_image_path)

with Image.open("/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/gt_img.png") as img:
 
    # Define the square's properties
    top_left_x = 200  # X-coordinate of the top-left corner of the square
    top_left_y = 200  # Y-coordinate of the top-left corner of the square
    size = 300       # Size of the square

    # Modify a set of pixels in the shape of a square
    pixels = img.load()
    for x in range(top_left_x, top_left_x + size):
        for y in range(top_left_y, top_left_y + size):
            pixels[x, y] = (255, 255, 255)  # Setting the pixel to white

    modified_image_path = "/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/masked_img.png"
    img.save(modified_image_path)





with Image.open("/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/gt_img.png") as img:
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if top_left_x <= x < top_left_x + size and top_left_y <= y < top_left_y + size:
                pixels[x, y] = (0, 0, 0)  # Set pixel within the square to black
            else:
                pixels[x, y] = (255, 255, 255)  # Set all other pixels to white

    modified_image_path_black_white = "/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/unknown_mask.png"
    img.save(modified_image_path_black_white)



    for x in range(img.width):
        for y in range(img.height):
            pixels[x, y] = (255, 255, 255)  # Setting the pixel to white


    justwhite = "/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph/valid_mask.png"
    img.save(justwhite)



# import os
# from PIL import Image

# # Specify the folder path containing the images
# folder_path = '/workspace/ashwinv/Learning-Continuous-Implicit-Representation-for-Near-Periodic-Patterns/data/completion/input/5ph'  # Replace with your folder path

# # Loop through each file in the folder
# for filename in os.listdir(folder_path):
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):  # Checking file extension
#         image_path = os.path.join(folder_path, filename)
#         with Image.open(image_path) as img:
#             print(f'{filename}: {img.size}')  # img.size is a tuple (width, height)
