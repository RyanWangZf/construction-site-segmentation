# -*- coding: utf-8 -*-

import os
import pdb
from PIL import Image
import numpy as np

# depth_dir = "Depth"
rgb_dir = "images"
label_dir = "label_npy"

# depth_save_dir = "{}_npy".format(depth_dir)
# rgb_save_dir = "{}_npy".format(rgb_dir)
rgb_save_dir = "./image_npy"

image_name_list = [x.split(".")[0] for x in os.listdir(label_dir)]

for img_name in image_name_list:
    save_name = os.path.join(rgb_save_dir, img_name)
    if os.path.exists(save_name):
        print("find existing:", save_name)
        continue

    rgb = np.array(Image.open(os.path.join(rgb_dir, "{}.jpg".format(img_name))))
    # dep = np.array(Image.open(os.path.join(depth_dir, "{}.jpg".format(img_name))))

    np.save(save_name, rgb)
    # np.save(os.path.join(depth_save_dir, img_name), dep)


