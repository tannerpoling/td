#!/usr/bin/env python3

from pyClient import *
import numpy as np

if __name__ == "__main__":
    client = pyClient()

    # just generate oscillating numbers forever
    test = np.array([1])
    val = 1
    upper_cap = 100
    lower_cap = 0
    inc = True
    dec = False
    while True:
        if inc: val+=1
        if dec: val-=1
        if (val >= upper_cap):
            inc = False
            dec = True
        if (val <= lower_cap):
            inc = True
            dec = False
        test[0] = val
        client.sendData(test)