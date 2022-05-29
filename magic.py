#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    a = [
        [6, 7, 2],
        [1, 5, 9],
        [8, 3, 4]
    ]
    mins = []
    for _ in range(4):
        res = []
        resm = []
        for i in range(3):
            local = []
            localm = []
            for j in range(3):
                local.append(a[2-j][i])
                localm.append(a[j][i])
            res.append(local)
            resm.append(localm)
        minx = 0
        minm = 0
        for i in range(3):
            for j in range(3):
                if res[i][j] != s[i][j]:
                    minx += abs(res[i][j] - s[i][j])
                if resm[i][j] != s[i][j]:
                    minm += abs(resm[i][j] - s[i][j])
        mins.append(min(minx, minm))
        a = res[::1]
        for i in res:
            print(i)
        print()
        for i in resm:
            print(i)
        print()
    return min(mins)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

