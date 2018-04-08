#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

"""
@author: puyangsky
@file: kmeans.py
@time: 2018/1/24 下午8:45
"""

import numpy as np
from sklearn.cluster import KMeans
import scipy.spatial.distance as sci_dist


def official():
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])

    kmeans = KMeans(n_clusters=2, random_state=0, verbose=False).fit(X)
    # print(kmeans.labels_)
    kmeans.predict([[0, 0], [4, 4]])
    print(kmeans.cluster_centers_)


class MyKMeans:
    def __init__(self, n_clusters=1, max_iter=1, data_set=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.data_set = data_set
        self.centers = self.randCent()

    def fit(self):
        data_size = np.shape(self.data_set)[0]
        # 第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
        cluster_result = np.mat(np.zeros((data_size, 2)))
        cluster_changed = True  # 用来判断聚类是否已经收敛
        iter_cnt = 0
        while cluster_changed and iter_cnt < self.max_iter:
            cluster_changed = False
            for i in range(data_size):  # 把每一个数据点划分到离它最近的中心点
                min_dist = np.inf
                min_index = -1
                for j in range(self.n_clusters):
                    dist = self.euclidean_distance(self.data_set[i], self.centers[j])
                    if dist < min_dist:
                        min_dist = dist
                        min_index = j
                if cluster_result[i, 0] != min_index:
                    cluster_changed = True
                cluster_result[i, :] = min_index, min_dist ** 2
            # 以每个簇的平均值作为新的中心点
            for cent in range(self.n_clusters):
                data = self.data_set[np.nonzero(cluster_result[:, 0].A == cent)[0]]
                self.centers[cent, :] = np.mean(data, axis=0)
            iter_cnt += 1
            print(iter_cnt)
        return self.centers, cluster_result

    def randCent(self):
        n = np.shape(self.data_set)[1]
        centers = np.mat(np.zeros((self.n_clusters, n)))
        for j in range(n):
            minJ = min(self.data_set[:, j])
            maxJ = max(self.data_set[:, j])
            rangeJ = float(maxJ - minJ)
            centers[:, j] = minJ + rangeJ * np.random.rand(self.n_clusters, 1)
        # matrix to ndarray
        return centers.A

    @staticmethod
    def euclidean_distance(vecA, vecB):
        return np.sqrt(sum(np.power(vecA - vecB, 2)))

    @staticmethod
    def jaccard_distance(vecA, vecB):
        mat = np.mat([vecA, vecB])
        result = sci_dist.pdist(mat, 'jaccard')
        print(result)
        return result


def test():
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])
    k_means = MyKMeans(n_clusters=2, max_iter=100, data_set=X)
    a, b = k_means.fit()
    print("center:\n", a)
    print("result:\n", b)


if __name__ == '__main__':
    # test()
    official()
    # data_set = np.array([[1, 1, 0, 1, 0, 1, 0, 0, 1],
    #                      [0, 1, 1, 0, 0, 0, 1, 1, 1]])
    # MyKMeans.jaccard_distance(data_set[0, :], data_set[1, :])
