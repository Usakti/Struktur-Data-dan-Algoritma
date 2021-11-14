# -*- coding: utf-8 -*-
"""
@Materi: Sorting
@Judul: Praktikum 2 Latihan 2
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
        
print("Waktu yg dibutuhkan Insertion Sort 1000 var: ")

for i in range(1):
    randomSorted = random.sample(range(0,1001),1000)
    start_time=time.time()
    insertion_sort(randomSorted)
    print(time.time()-start_time)
