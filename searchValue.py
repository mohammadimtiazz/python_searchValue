# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:34:46 2017

@author: Mohammad Imtiaz
"""
import numpy as np

def searchValue(inputArray, value):
    tupleArray = np.where(inputArray == value)
    outputArray = np.transpose(tupleArray)
    return outputArray
    
