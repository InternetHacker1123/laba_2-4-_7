#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    sp = list(map(int, input().split()))
    zeroCounter = 0
    if not sp:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    for i, item in enumerate(sp):
        if item == 0:
            zeroCounter += 1
            print(i)