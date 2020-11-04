from __future__ import division
from functools import partial

import numpy as np
from numba import jit
from numpy.random import randint
from numpy.random import seed as set_np_seed

@jit
def num_hash(num, end):
    """
    hash function that maps an integer form [0, end-1] to [0, end-1] 
    (approximation of random permutation/shuffling)    

    :type: num: int
    :type: end: int
    :rtype: int
    """
    rand_a, rand_b = randint(low=1, high=end, size=2)
    return (num * rand_a + rand_b) % end


def matrix_hash(matrix, end):
    """
    random projection of a matrix (into a vector)

    :type: matrix: np.array
    :type: end: int
    :rtype: np.array
    """
    n_rows, n_bands = matrix.shape
    rand_matrix = randint(low=1, high=end, size=(n_rows, n_bands))
    rand_vector = randint(low=1, high=end, size=(1, n_bands))
    return np.sum(matrix * rand_matrix + rand_vector, axis=1) % end


class min_hash_fact(object):
    """min hash function factory class"""
    
    def __init__(self, num_hash, matrix_hash, n_rows, n_bands):
        self.num_hash = np.vectorize(num_hash)
        self.matrix_hash = matrix_hash
        self.n_rows, self.n_bands = n_rows, n_bands


    def _min_hash(self, arr):
        return self.num_hash(arr).min() # select the minimum index after random permutation

    
    def __call__(self, arr, seed=2020, raw=False):
        # perpare the same random number sequence for differernt input `arr`
        set_np_seed(seed)

        # generate signature matrix for `arr`
        signature_matrix = np.array([[self._min_hash(arr) for _ in range(self.n_rows)] \
                                                          for _ in range(self.n_bands)])
        if raw:
             return signature_matrix
        
        # hash the signature matrix into signature buckets
        return self.matrix_hash(signature_matrix)
    

def jaccard_similarity(arr1, arr2):
    s1, s2 = set(arr1), set(arr2)
    return len(s1 & s2) / len(s1 | s2)


if __name__ == '__main__':
    import random
    from numpy import mean

    num_hash = partial(num_hash, end=97)
    matrix_hash = partial(matrix_hash, end=47)
    min_hash = min_hash_fact(num_hash, matrix_hash, 11, 80)

    arr1 = [1, 3, 5, 7, 8, 10, 12, 19]
    arr2 = [1, 3, 7, 8, 19]

    print(f'arr1 = {arr1}')
    print(f'arr2 = {arr2}')
    print(f'Jaccard Similarity = {jaccard_similarity(arr1, arr2)}', end='\n\n')
    
    print('Signature Buckets: ')
    print(min_hash(arr1))
    print(min_hash(arr2), end='\n...\n\n')
    
    seeds = (random.randint(1, 100) for _ in range(100))
    hits = [any(h1 == h2 for (h1, h2) in zip(min_hash(arr1, seed), min_hash(arr2, seed))) for seed in seeds]
    print(f'Average Hits Prob in {len(hits)} runs: {mean(hits)}')