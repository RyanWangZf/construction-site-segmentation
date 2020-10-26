# -*- coding: utf-8 -*-

import numpy as np
import os
import pdb
import json

from collections import defaultdict

def count_instance(name_list=None):

    json_dir = "mask"

    with open("label_list.txt", "r") as f:
        all_labels = [x.split()[0] for x in f.readlines()]

    # instance_stats = dict().fromkeys(all_labels, 0)
    instance_stats = defaultdict(int)

    if name_list is None:
        # count all
        json_list = [os.path.join(json_dir,x) for x in os.listdir(json_dir)]
    else:
        # filter json list
        json_list = [os.path.join(json_dir,"{}.json".format(x)) for x in name_list]

    for idx,file in enumerate(json_list):
        # print(idx+1, file)
        with open(file, "r") as f:
            json_txt = json.load(f)
            num_instances = len(json_txt["shapes"])

        for i in range(num_instances):
            instance_stats[json_txt["shapes"][i]["label"]] += 1

    print(instance_stats)
    return instance_stats

if __name__ == '__main__':
    # get train name list
    with open("train_list.txt","r") as f:
        name_list = f.readlines()

    name_list = [x.split(".")[0] for x in name_list]

    # stats = count_instance(name_list)
    stats = count_instance()
    stats_list = list(stats.values())
    print(stats_list)
    pdb.set_trace()
    pass
    