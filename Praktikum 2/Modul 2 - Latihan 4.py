# -*- coding: utf-8 -*-
"""
@Materi: Sorting
@Judul: Praktikum 2 Latihan 4
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

import random
import time

def bubbleSort(x):
    n = len(x)
    for i in range(n):
        for j in range(0, n-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
                
print("Waktu yang dibutuhkan bubble sort 10000 var : ")
for i in range(1):
    randomSorted = random.sample(range(0,10001),10000)
    start_time=time.time()
    bubbleSort(randomSorted)
    print(time.time()-start_time)
