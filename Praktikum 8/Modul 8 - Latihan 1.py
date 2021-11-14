# -*- coding: utf-8 -*-
"""
@Materi: Binary Seacrh Tree
@Judul: Praktikum 8 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def search(self, var):
        if var < self.data:
            if self.left is None:
                return print(str(var) + " Tidak Ditemukan")
            return self.left.search(var)
        elif var > self.data:
            if self.right is None:
                return print(str(var) + " Tidak Ditemukan")
            return self.right.search(var)
        else:
            print(str(self.data) + " Ditemukan")
    
    def sort(self):
        if self.left:
            self.left.sort()
        print(self.data),
        if self.right:
            self.right.sort()
            
def main():
    root = Node(None)
    root.insert(18)
    root.insert(1)
    root.insert(2)
    root.insert(7)
    root.insert(5)
    root.insert(9)
    root.insert(16)
    root.insert(14)
    root.insert(11)

    print("============================")
    print(" BINARY SEARCH TREE ")
    print("============================")
    x = int(input("Masukkan Variabel yang dicari: "))
    root.search(x)
    
    print("============================")
    print("Setelah diurutkan menjadi...")
    root.sort()
    print("Terima Kasih telah menggunakan Program Nadiya Amanda, Good bye!")

main()
