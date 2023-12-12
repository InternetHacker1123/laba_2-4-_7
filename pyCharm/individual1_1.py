#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    sp = list(map(int, input().split()))
    if not sp:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    
    zeros = [i for i, item in enumerate(sp) if item == 0]
    zero_counter = len([i for i in sp if i == 0]) 
    print(zeros)