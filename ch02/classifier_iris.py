# -*- coding: utf-8 -*-
'''
Created on 26 авг. 2016 г.
Обучение и проверка модели классификатора набора Iris
@author: igor
'''
import numpy as np
from sklearn.datasets import load_iris

def fit_models(features, labels):
    best_acc = -1.0
    for fi in xrange(features.shape[1]):
        thresh = features[:,fi].copy()
        thresh.sort()
        for t in thresh:
            pred = (features[:,fi] > t)
            acc = (pred == labels).mean()
            rev_acc = (pred == ~labels).mean()
            if rev_acc > acc:
                acc = rev_acc
                reverse = True
            else:
                reverse = False
            if acc > best_acc:
                best_acc = acc
                best_fi = fi
                best_t = t
                best_reverse = reverse
    return best_t, best_fi, best_reverse

def predict(model, features):
    t, fi, reverse = model
    if reverse:
        return features[:,fi] <= t
    else:
        return features[:,fi] > t

def accuracy(features, labels, model):
    preds = predict(model, features)
    return (preds == labels).mean()

data = load_iris()
features = data.data
labels = data.target_names[data.target]
is_setosa = (labels == 'setosa')
is_virgnica = (labels == 'virginica')
correct = 0
for ei in xrange(len(features)):
    traning = np.ones(len(features), dtype=bool)
    traning[ei] = False
    testing = ~traning
    model_setosa = fit_models(features[traning], is_setosa[traning])
    model_virginica = fit_models(features[traning], is_virgnica[traning])
    result_setosa = predict(model_setosa, features[testing])
    if result_setosa[0]:
        result = 'setosa'
    else:
        result_virginica = predict(model_virginica, features[testing])
        if result_virginica[0]:
            result = 'virginica'
        else:
            result = 'versicolor'
    if labels[ei] == result:
        correct += 1

print 'Accuracy: %f' % (correct / float(len(features)))



