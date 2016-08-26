# -*- coding: utf-8 -*-
'''
Created on 26 авг. 2016 г.
Визуализирует набор Iris
@author: igor
'''
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

fig,axes = plt.subplots(2, 3)
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

# Set up 3 different pairs of (color, marker)
color_markers = [
        ('r', '>'),
        ('g', 'o'),
        ('b', 'x'),
        ]
for i, (p0, p1) in enumerate(pairs):
    ax = axes.flat[i]

    for t in xrange(3):
        # Use a different color/marker for each class `t`
        c,marker = color_markers[t]
        ax.scatter(features[target == t, p0], features[
                    target == t, p1], marker=marker, c=c)
    ax.set_xlabel(feature_names[p0])
    ax.set_ylabel(feature_names[p1])
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
plt.show()
labels = target_names[target]
plength = features[:,2]
is_setosa = (labels == 'setosa')
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print u'Максимальная длинна лепестка у сорта Setosa %f' % max_setosa
print u'Минимальная длинна лепестков у других сортов %f' % min_non_setosa
features = features[~is_setosa]
labels = labels[~is_setosa]
is_virginica = (labels == 'virginica')
best_acc = -1.0
for fi in xrange(features.shape[1]):
    thresh = features[:,fi]
    for t in thresh:
        feature_i = features[:,fi]
        pred = (feature_i > t)
        acc = (pred == is_virginica).mean()
        rev_acc = (pred == ~is_virginica).mean()
        if rev_acc > acc:
            reverse = True
            acc = rev_acc
        else:
            reverse = False
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t
            best_reverse = reverse
print u'Лучшая верность %f на основе признака %s, делительный порог %f' % (best_acc, feature_names[fi], best_t), best_reverse

def classifier(feature):
    if feature[2] < 2.0:
        return 0
    else:
        if feature[3] > 1.6:
            return 2
        else:
            return 1


result = (np.apply_along_axis(classifier, 1, data.data) == data.target)
print u'Верных ответов %d, неверных %d' % (result.sum(), len(result) - result.sum())
print u'Верность на всем наборе %f' % result.mean()
    
              
        

