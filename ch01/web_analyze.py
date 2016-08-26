# -*- coding: utf-8 -*-
'''
Created on 24 авг. 2016 г.
Построение простейшей полиноминальная модель
@author: igor
'''
import scipy as sp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def show_models(x, y, models=[], fx=None, ymax=None, xmin=None):
    plt.scatter(x, y, s=10)
    plt.title('Web traffic over the last month')
    plt.xlabel('Time')
    plt.ylabel('Hits/hour')
    plt.xticks([w*24*7 for w in xrange(12)], ['week %d' % w for w in xrange(12)])
    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    plt.grid(True, linestyle='-', color='0.75')
    if models:
        if fx is None:
            fx = sp.linspace(0, x[-1], 100)
        for f in models:
            plt.plot(fx, f(fx), linewidth=2)
        plt.legend(['d=%d' % f.order for f in models], loc='upper left')
    if ymax:
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    plt.show()
   

def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)

data = sp.genfromtxt('../BuildingMachineLearningSystemsWithPython/ch01/data/web_traffic.tsv', delimiter='\t')
x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
show_models(x, y)
f1 = sp.poly1d(sp.polyfit(x, y, 1))
f2 = sp.poly1d(sp.polyfit(x, y, 2))
f3 = sp.poly1d(sp.polyfit(x, y, 3))
f4 = sp.poly1d(sp.polyfit(x, y, 4))
f5 = sp.poly1d(sp.polyfit(x, y, 5))
f10 = sp.poly1d(sp.polyfit(x, y, 10))
f100 = sp.poly1d(sp.polyfit(x, y, 100))
print u'Ошибка на всем диапазоне'
for f in [f1, f2, f3, f4, f5, f10, f100]:
    models = []
    print u'Error d=%2d: %20f' % (f.order, error(f, x, y))
    models.append(f)
    show_models(x, y, models)
inflection = 3.5 * 7 * 24
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]
fa1 = sp.poly1d(sp.polyfit(xa, ya, 1))
fb1 = sp.poly1d(sp.polyfit(xb, yb, 1))
fa2 = sp.poly1d(sp.polyfit(xa, ya, 2))
fb2 = sp.poly1d(sp.polyfit(xb, yb, 2))
fa3 = sp.poly1d(sp.polyfit(xa, ya, 3))
fb3 = sp.poly1d(sp.polyfit(xb, yb, 3))
fa4 = sp.poly1d(sp.polyfit(xa, ya, 4))
fb4 = sp.poly1d(sp.polyfit(xb, yb, 4))
fa5 = sp.poly1d(sp.polyfit(xa, ya, 5))
fb5 = sp.poly1d(sp.polyfit(xb, yb, 5))
fa10 = sp.poly1d(sp.polyfit(xa, ya, 10))
fb10 = sp.poly1d(sp.polyfit(xb, yb, 10))
fa100 = sp.poly1d(sp.polyfit(xa, ya, 100))
fb100 = sp.poly1d(sp.polyfit(xb, yb, 100))
print u'Ошибка с использованием двух участов'
for fa, fb in [(fa1, fb1), (fa2, fb2), (fa3, fb3), (fa4, fb4), (fa5, fb5), (fa10, fb10), (fa100, fb100)]:
    models = []
    print u'Error d=%2d: %20f' % (fa.order, error(fa, xa, ya) + error(fb, xb, yb))
    models.append(fa)
    models.append(fb)
    show_models(x, y, models)
print u'Ошибка после точки перегиба'
for fb in [fb1, fb2, fb3, fb4, fb5, fb10, fb100]:
    print u'Error d=%2d: %20f' % (fb.order, error(fb, xb, yb))
frac = 0.3
split_idx = int(frac * len(xb))
shuffled = sp.random.permutation(list(range(len(xb))))
test = sorted(shuffled[:split_idx])
train = sorted(shuffled[split_idx:])
fbt1 = sp.poly1d(sp.polyfit(xb[train], yb[train], 1))
fbt2 = sp.poly1d(sp.polyfit(xb[train], yb[train], 2))
fbt3 = sp.poly1d(sp.polyfit(xb[train], yb[train], 3))
fbt4 = sp.poly1d(sp.polyfit(xb[train], yb[train], 4))
fbt5 = sp.poly1d(sp.polyfit(xb[train], yb[train], 5))
fbt10 = sp.poly1d(sp.polyfit(xb[train], yb[train], 10))
fbt100 = sp.poly1d(sp.polyfit(xb[train], yb[train], 100))
print "Ошибка на тестовых данных после точки перегиба:"
for f in [fbt1, fbt2, fbt3, fbt4, fbt5, fbt10, fbt100]:
    print "Error d=%2d: %20f" % (f.order, error(f, xb[test], yb[test]))
    show_models(x, y, [f], xmin=0)
reached_max = fsolve(fbt2 - 100000, x0=800) / (7 * 24)
print u'Количество запросов достигнет 100000 на %f неделе' % reached_max

 





