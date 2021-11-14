# -*- coding: utf-8 -*-
"""
@Materi: Queue
@Judul: Praktikum 6 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

from queue import Queue 

class myQueue:
    def __init__(self):
        self.itemNay = Queue(maxsize = 3)
    
    def isEmpty(self):
        self.itemNay.empty()
    
    def enqueue(self, item):
        self.itemNay.put(item)
    
    def dequeue(self):
        return self.itemNay.get()
    
    def isfull(self):
        return self.itemNay.full()
    
    def mainmenu(self):
        pilih = ""
        while (pilih == ""):
            print()
            print("Menu A ==> Enqueue")
            print("Menu B ==> Dequeue")
            print("Menu C ==> Keluar")
            print("=========================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="A"):
                if self.isfull():
                    print("Queue anda full")
                else:
                    obj = str(input("Enqueue : "))
                    self.enqueue(obj) 
            elif(pilihan=="B"):
                if self.itemNay.empty():
                    print("Queue anda kosong")
                else:
                    print("Nilai yang di dequeue:", self.dequeue())
            
            elif(pilihan== "C"):
                print(self.itemNay.queue)
                break
            
q = myQueue()
q.mainmenu()
