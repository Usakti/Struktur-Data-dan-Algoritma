# -*- coding: utf-8 -*-
"""
@Materi: Stack
@Judul: Praktikum 5 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

class Stack():
    def __init__(self):
        self.itemsNay = []
    def push(self, itemsNay):
        self.itemsNay.append(itemsNay)
    def pop(self):
        return self.itemsNay.pop()
    def get_stack(self):
        return self.itemsNay

s = Stack()
f = ''
while (f != "C"):
    print("Menu A -> Push")
    print("Menu B -> Pop")
    print("Menu C -> Exit")
    f = str(input("Silahkan Pilih Menu: "))
    if (f == "A"):
        a = str(input("Nilai yang di Push: "))
        s.push(a)
    elif (f == "B"):
        if s == []:
            print("Stacknya Kosong")
        else:
            print("Nilai yang di Pop(): ", s.pop())
 
print(s.get_stack())
