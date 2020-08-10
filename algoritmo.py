#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################################
# Generar posiciones aleatorias en un espacio determinado
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: Created on Thu Sep 28 08:38:15 2017
# Version: 1.0
#######################################################
"""

# libreria
import time
import datetime
import os
import pandas as pd
import numpy as np
import random


def main():
    polygon = [Point(31.14, -112),
               Point(31.20, -110.56),
               Point(31.19, -109.00),
               Point(26.74, -109.06),
               Point(31.55, -113.18)]

    # list of points
    coords = np.array([])

    while len(coords) < 51:
        random_lat = random.uniform(26.74, 31.74)
        random_lon = random.uniform(-113.18, -109)

        p1 = Point(random_lat, random_lon)
        while p1 in coords:
            random_lat = random.uniform(26.74, 31.74)
            random_lon = random.uniform(-113.18, -109)
            p1 = Point(random_lat, random_lon)

        if is_within_polygon(polygon, p1):
            coords = np.append (coords, [random_lat, random_lon])

    file = open("Sonora.csv", "wb")
    print(coords)
    file.close()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_within_polygon(polygon, point):
    A = []
    B = []
    C = []
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]

        # calculate A, B and C
        a = -(p2.y - p1.y)
        b = p2.x - p1.x
        c = -(a * p1.x + b * p1.y)

        A.append(a)
        B.append(b)
        C.append(c)

    D = []
    for i in range(len(A)):
        d = A[i] * point.x + B[i] * point.y + C[i]
        D.append(d)

    t1 = all(d >= 0 for d in D)
    t2 = all(d <= 0 for d in D)
    return t1 or t2

if __name__ == '__main__':
    main()
