import numpy as np
from operator import itemgetter

class KNN:
    def __init__(self, data, target, test_point, k):
        self.data= data
        self.target= target
        self.test_point = test_point
        self.k = k
        self.distances= list()
        self.categories= list()
        self.indices= list()
        self.counts=list()
        self.category_assigned = None

    
    @staticmethod
    #returns the euclidean distance between the two points
    def distance(x1, x2):
        return np.linalg.norm(np.array(x1)- np.array(x2))
    
    def fit(self):
        self.distances.extend([(self.distance(self.test_point, point), i) for point, i in zip(self.data, [i for i in range(len(self.data))])])
        sorted_li = sorted(self.distances, key=itemgetter(0)) #sorting the distances in ascending order
        self.indices.extend([index for (val, index) in sorted_li[:self.k]]) #fetches the index of k nearest points
        for i in self.indices:
            self.categories.append(self.target[i])
        self.counts.extend([(i, self.categories.count(i)) for i in set(self.categories)])
        self.category_assigned = sorted(self.counts, key=itemgetter(1), reverse=True)[0][0] 
