import numpy as np
from numpy import random

def run_viterbi(emission_scores, trans_scores, start_scores, end_scores):
    """Run the Viterbi algorithm.

    N - number of tokens (length of sentence)
    L - number of labels

    As an input, you are given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    You have to return a tuple (s,y), where:
    - s is the score of the best sequence
    - y is a size N array of integers representing the best sequence.
    """
    L = start_scores.shape[0]
    assert end_scores.shape[0] == L
    assert trans_scores.shape[0] == L
    assert trans_scores.shape[1] == L
    assert emission_scores.shape[1] == L
    N = emission_scores.shape[0]

    y = []
    dp = np.array([[0.0 for j in range(N)] for i in range(L)])
    bp = np.array([[-1 for j in range(N)] for i in range(L)])
    
    for i in xrange(N):
        if i == 0:
            dp[:,0] = np.add(start_scores, emission_scores[i])
        else:
            for j in xrange(L):
                dp[j,i]= np.max(np.add(trans_scores[:,j] , dp[:,i-1])) + emission_scores[i,j]
                bp[j,i] = np.argmax(np.add(trans_scores[:,j] , dp[:,i-1]))
     
    score = np.max(np.add(dp[:,i], end_scores))
    ind = np.argmax(np.add(dp[:,i], end_scores))
    
    while ind != -1:
        y.append(ind)
        ind = bp[ind,i]
        i -= 1
    
    y.reverse()
    return (score, y)
