import random
import numpy as np

class KMeans:
    def __int__(self,n_cluster=2,max_iter=100):
        self.n_cluster = n_cluster
        self.max_iter = max_iter
        self.centroids = None
    def fit_predict(self,X):
        random_index = random.sample(range(0,X.shape[0]),self.n_cluster)
         