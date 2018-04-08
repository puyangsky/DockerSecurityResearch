from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([3, 1, 1, 2, 1, 6, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8])
x2 = np.array([5, 4, 5, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3])


def cal_elbow(labels, centroids, X, k):
    # calculate euclidean distance between vectors
    variance = 0
    for i, j in enumerate(X):
        idx = labels[i]
        variance += np.sqrt(np.sum(np.square(j - centroids[idx])))
    print(k, variance)
    return variance


def cluster():
    plt.plot()
    plt.xlim([0, 10])
    plt.ylim([0, 60])
    plt.title('Dataset')
    plt.scatter(x1, x2)
    # plt.show()

    # create new plot and data
    plt.plot()
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
    colors = ['b', 'g', 'r']
    markers = ['o', 'v', 's']

    # k means determine k
    distortions = []
    K = range(1, 10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k).fit(X)
        kmeanModel.fit(X)
        distortions.append(cal_elbow(kmeanModel.labels_,
                                     kmeanModel.cluster_centers_,
                                     X,
                                     k))

    # Plot the elbow
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('The cluster number k')
    plt.ylabel('Variance')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()


if __name__ == '__main__':
    cluster()
