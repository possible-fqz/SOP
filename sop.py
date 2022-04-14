from asyncio.windows_events import NULL
from gc import collect
from unittest import result
import numpy as np
import scipy as sp
from scipy.linalg import expm
import math

def lemma27(m,t):
    pass

def SOP1(A,I,G,R,V,n,sigma):
    """
    This is SOP method1.
    
    Parameters:
        A - matrix
        I - invariant
        G - set of gards
        R -
        V - 
        n - t/sigma
        sigma - 常数 
    
    Returns:
        collectedIntersections - collected intersections with the guards
    """
    for k in range(0,n+1):
        if R[k]==NULL:
            break
        for g in G:
            if not np.intersect1d(R[k],g,False).size()==0:
                collectedIntersections+=np.intersect1d(R[k],g,False)
        R[k+1]=np.intersect1d((expm(sigma*A)*R[k]+V),I,False)
    return collectedIntersections
