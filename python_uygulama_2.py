# -*- coding: utf-8 -*-
"""python_uygulama_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u4C3t-CnGQDYR13N9y7jpgrMnU9Vv3dJ
"""

import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 2D uzaydaki noktaları içeren bir liste
points = [(1, 2), (4, 6), (7, 1), (3, 3)]

# Mesafeleri saklamak için bir liste oluşturuyoruz
distances = []

# Her nokta çifti arasındaki mesafeleri hesaplayıp distances listesine ekleme
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Mesafeleri yazdırma
print("Mesafeler:", distances)

# Minimum mesafeyi bulma
min_distance = min(distances)
print("Minimum mesafe:", min_distance)