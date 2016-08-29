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
from load_seed import load_dataset_seeds

features, labels = load_dataset_seeds()
print u'Классификация по ближайшим соседям (KNeighborsClassifier)'
classifier = KNeighborsClassifier(n_neighbors=1)
kf = KFold(len(features), n_folds=5, shuffle=True)
means = []
for i, (training, testing) in enumerate(kf):
    classifier.fit(features[training], labels[training])
    prediction = classifier.predict(features[testing])
    curmean = np.mean(prediction == labels[testing])
    print u'%d проход, верность: %f' % (i+1, curmean)
    means.append(curmean)
print u'Средняя верность: %f' % np.mean(means)
print
print u'Классификация по ближайшим соседям (KNeighborsClassifier), с нормированием (StandardScaler)'
classifier = KNeighborsClassifier(n_neighbors=1)
classifier = Pipeline([('norm', StandardScaler()), ('knn', classifier)])
kf = KFold(len(features), n_folds=5, shuffle=True)
means = []
for i, (training, testing) in enumerate(kf):
    classifier.fit(features[training], labels[training])
    prediction = classifier.predict(features[testing])
    curmean = np.mean(prediction == labels[testing])
    print u'%d проход верность: %f' % (i+1, curmean)
    means.append(curmean)
print u'Средняя верность: %f' % np.mean(means)

