# -*- coding: utf-8 -*-
'''This code is supporting material for the book
Building Machine Learning Systems with Python
by Willi Richert and Luis Pedro Coelho
published by PACKT Publishing

It is made available under the MIT License
'''


import timeit

normal_py_sec = timeit.timeit('sum(x*x for x in range(10000))',
                              number=10000)
naive_np_sec = timeit.timeit('np.sum(na*na)',
                             setup='import numpy as np; na=np.arange(10000)',
                             number=10000)
good_np_sec = timeit.timeit('na.dot(na)',
                            setup='import numpy as np; na=np.arange(10000)',
                            number=10000)

print u'Normal Python: %f sec' % normal_py_sec
print u'Naive NumPy: %f sec' % naive_np_sec
print u'Good NumPy: %f sec' % good_np_sec
