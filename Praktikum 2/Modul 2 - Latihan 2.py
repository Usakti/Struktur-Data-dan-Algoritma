# -*- coding: utf-8 -*-
"""
@Materi: Sorting
@Judul: Praktikum 2 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

import random
import time

def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    
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
    insertion_sort(randomSorted)
    print("Waktu prosesnya adalah " , time.time()-start_time)
