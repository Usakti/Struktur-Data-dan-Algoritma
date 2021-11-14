# -*- coding: utf-8 -*-
"""
@Materi: Dequeue
@Judul: Praktikum 7 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

from collections import deque

class Antrian:
    def __init__ (self):
        self.antrian = deque()
     
    def hasil(self):
        if len(self.antrian) == 0:
            print("Antrian Kosong")
        else:
            print(self.antrian)
    
    def enqueue(self, x):
        self.antrian.append(x)
    
    def dequeue(self):
        if len(self.antrian) == 0:
            print("Antrian Kosong")
        else:
            print("Terima Kasih...", self.antrian.popleft(), "Silahkan Datang Kembali ^^")
    
q = Antrian()
while True:
    print("---------- ANTRIAN TELLER BANK ----------")
    print("========== A -> Masuk Antrian ==========")
    print("========== B -> Proses Antrian ==========")
    print("========== C -> Keluar ==========")
    print("-----------------------------------------")
    Menu = str(input("Masukkan Menu Pilihan: "))
    if (Menu == "A" or Menu == "a"):
        x = str(input("Antri: "))
        q.enqueue(x)
    elif (Menu == "B" or Menu =="b"):
        q.dequeue()
    elif(Menu == "C" or Menu == "c"):
        q.hasil()
        break
