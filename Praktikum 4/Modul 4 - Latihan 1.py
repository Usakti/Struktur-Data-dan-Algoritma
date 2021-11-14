# -*- coding: utf-8 -*-
"""
@Materi: Method dalam List
@Judul: Praktikum 4 Latihan 2
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

print("================== 1A ==================")

NayList = []
a = 1
while (a <= 10):
    NayList.append(a)
    a = a + 1

print("Listnya adalah: ", NayList)

print("================== 1B ==================")
b = int(input("Masukkan Tanggal Lahir: "))

NayList.insert(0, b)
print("List dengan Tanggal Lahir: ", NayList)

print("=================== 1C ==================")

AList = [5, 2, 9, 3, 7]

NayList.extend(AList)
print("List dengan Extend: ", NayList)

print("=================== 1D ==================")

print("Jumlah Seluruh List: ", sum(NayList))
print("Banyaknya angka 5 adalah: ", NayList.count(5))
print("Panjang List adalah: ", len(NayList))
print("Index dari angka 3 dalam list adalah: ", NayList.index(3))

print("=================== 1E ==================")

print("Mengambil dan menghapus indeks 5 dengan pop: ", NayList.pop(5))
del NayList[5]
print("Indeks 5 telah dihapus dengan del: ", NayList)
NayList.remove(9)
print("Setelah elemen 9 diremove: ", NayList)
print("Setelah dilakukan operasi, List menjadi: ", NayList)

print("=================== 1F ==================")

print("Nilai Minimal dari List adalah: ", min(NayList))
print("Nilai Maksimal dari List adalah: ", max(NayList))
print("List Utama Saya: ", NayList)
