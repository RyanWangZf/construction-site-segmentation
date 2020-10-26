# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image

import os
import pdb

save_dir = "label_npy"
read_dir = "labels"

dir_list = [os.path.join(read_dir,x) for x in os.listdir(read_dir)]

with open("label_list.txt", "r") as f:
    label_dict = f.readlines()

label_dict = {x.strip():i for x,i in zip(label_dict,range(len(label_dict)))}

for idx,d in enumerate(dir_list):
    print(idx+1, d)
    label = np.array(Image.open(os.path.join(d,"label.png")))
    with open(os.path.join(d, "label_names.txt"), "r") as f:
        line_data = f.readlines()

    num_class = len(line_data)

    local_dict = {i:x.strip() for x,i in zip(line_data,range(len(line_data)))}
    
    local_map = {}
    for i in range(num_class):
        local_name = local_dict[i]
        if local_name in label_dict:
            local_map[i] = label_dict[local_name]
        else:
            # not used in label_list
            local_map[i] = 0

    new_label = np.zeros_like(label)
    for i in range(num_class):
        new_label[label == i] = local_map[i]


    save_name = os.path.join(save_dir, d.split("\\")[1])
    np.save(save_name, new_label)


print("Done.")


