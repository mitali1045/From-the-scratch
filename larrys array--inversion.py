# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:09:58 2021

@author: Mitali.Tavildar
"""

def larrysArray(A):
    inversion = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] > A[j]):
                inversion += 1

    if inversion % 2 == 0:
        return 'YES'
    else:
        return 'NO'