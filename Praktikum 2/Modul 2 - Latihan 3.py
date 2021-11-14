# -*- coding: utf-8 -*-
"""
@Materi: Sorting
@Judul: Praktikum 2 Latihan 3
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
 
nilai = int(input("Masukkan rentang nilai yang diinginkan : "))
a = nilai//2

for i in range(1):
    randomSorted = random.sample(range(0, a + 1), a)
    print(("Random : "), randomSorted)
    randomNotSorted = random.sample(range(a+1,nilai + 1), a)
    print("Random Not Sorted : " , randomNotSorted)
    list.sort(randomSorted)
    randomSorted = randomSorted + randomNotSorted
    start_time=time.time()
    bubbleSort(randomSorted)
    print("Waktu prosesnya adalah " , time.time()-start_time)
