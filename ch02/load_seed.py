# -*- coding: utf-8 -*-
'''
Created on 29 авг. 2016 г.
Загружает из файла набор seed
@author: igor
'''
import numpy as np

def load_dataset_seeds():
    name_file = '../BuildingMachineLearningSystemsWithPython/ch02/data/seeds.tsv'
    data =[]
    labels=[]
    with open(name_file) as f:
        for line in f:
            tokens = line.strip().split('\t')
            data.append([float(tk) for tk in tokens[:-1]])
            labels.append(tokens[-1])
    data = np.array(data)
    labels = np.array(labels)
    return data, labels

