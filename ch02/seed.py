# -*- coding: utf-8 -*-
'''
Created on 28 авг. 2016 г.
Классификатор сортов зерна по набору SEED
@author: igor
'''
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
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


features, labels = load_dataset_seeds()
classifier = KNeighborsClassifier(n_neighbors=1)
classifier = Pipeline([('norm', StandardScaler()), ('knn', classifier)])
kf = KFold(len(features), n_folds=5, shuffle=True)
means=[]
for training, testing in kf:
    classifier.fit(features[training], labels[training])
    prediction = classifier.predict(features[testing])
    curmean = np.mean(prediction == labels[testing])
    means.append(curmean)
print u'Средняя верность: %f' % np.mean(means)

