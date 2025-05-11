# coding=utf-8
"""
生成随机数组
"""

import random


def generate_array(n=10, min=0, max=100, sort=False):
    arr = [random.randint(min, max) for _ in range(n)]

    if sort:
        arr.sort()

    return arr
