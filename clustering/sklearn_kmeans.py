#!/usr/bin/env python
# encoding: utf-8

"""
@author: puyangsky
@file: sklearn_kmeans.py
@time: 2018/3/18 下午3:00
"""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


def official():
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])
    plt.figure(figsize=(8, 5))
    plt.title('Scatter Plot')
    kmeans = KMeans(n_clusters=2, random_state=0, verbose=False).fit(X)
    # # print(kmeans.labels_)
    # kmeans.predict([[0, 0], [4, 4]])
    # print(kmeans.cluster_centers_)

    plt.scatter(X[:, 0], X[:, 1])
    plt.show()


if __name__ == '__main__':
    official()