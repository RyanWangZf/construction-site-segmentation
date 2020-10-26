# -*- coding: utf-8 -*-

import os
import shutil
import pdb

path = "./mask"  # path为json文件存放的路径
save_path = "./labels"
# path = "./label"
json_file = os.listdir(path)
for file in json_file:
    new_path = os.path.join(save_path, file.split(".")[0])
    if os.path.exists(new_path):
        print("Find existing", new_path)
        continue
    os.system("labelme_json_to_dataset.exe %s"%(path + '/' + file))
    old_path = os.path.join(path, file.split(".")[0] + "_json")
    shutil.move(old_path, new_path)



