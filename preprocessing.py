
import os
from PIL import Image
import numpy as np
print(os.listdir("./val"))

target_dir = "./ustims/segmentation/input"
for fname in os.listdir("./val"):
    if fname.endswith(".png"):
        dir_name, ext = os.path.splitext(fname)
        target_img_dir = os.path.join(target_dir, dir_name)
        os.makedirs(target_img_dir, exist_ok=True)

        # store 4 images in each folder named
        # gt_img.png
        # masked_img.png
        # unknown_mask.png
        # valid_mask.png
        # gt_img.png = masked_img.png
        # unknown_mask.png = valid_mask.png = np.ones(gt_image.shape)
        im = Image.open(os.path.join("./val", fname))
        im.save(os.path.join(target_img_dir, "gt_img.png"))
        im.save(os.path.join(target_img_dir, "masked_img.png"))
        ar = np.ones(im.size) * 255
        ar = ar.astype(np.uint8)
        mask = Image.fromarray(ar)
        mask.save(os.path.join(target_img_dir, "unknown_mask.png"))
        mask.save(os.path.join(target_img_dir, "valid_mask.png"))

