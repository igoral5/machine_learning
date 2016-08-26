# -*- coding: utf-8 -*-
'''
Created on 24 авг. 2016 г.
Работа с NumPy
@author: igor
'''
import numpy as np

a = np.array([0, 
              np.pi / 6, 
              np.pi / 4, 
              np.pi / 3, 
              np.pi / 2, 
              2 * np.pi / 3, 
              3 * np.pi / 4, 
              5 * np.pi / 6, 
              np.pi, 
              7 * np.pi / 6, 
              5 * np.pi / 4, 
              4 * np.pi / 3, 
              3 * np.pi / 2, 
              5 * np.pi / 3, 
              7 * np.pi / 4, 
              11 * np.pi / 6, 2 * np.pi])

b = np.array([ x * np.pi / 180 for x in [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]])

if np.all(np.abs(a - b) < 1e-10):
    print u'Массивы равны'
