#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    sp = list(map(float, input().split()))
    sp_1 = []
    sp_2 = []
    sp_3 = []
    final_sp = []
    maks = -1
    for i, item in enumerate(sp):
        if abs(item) > maks:
            maks = abs(item)
        if item != 0:
            sp_1.append(item)
        if item == 0:
            sp_2.append(item)
        if item > 0:
            sp_3.append(i)
    final_sp = sp_1 + sp_2
    sm = sum(sp[sp_3[0]+1:sp_3[1]])
    print(f"{maks}\n{sm}")
    