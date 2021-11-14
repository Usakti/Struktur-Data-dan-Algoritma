# -*- coding: utf-8 -*-
"""
@Materi: Class dan Object
@Judul: Praktikum 3 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

class Mobil:
    def __init__(self, Nama, Merk, Jenis, Warna, Harga, Bunga):
        self.Nama = Nama
        self.Merk = Merk
        self.Jenis = Jenis
        self.Warna = Warna
        self.Harga = Harga
        self.Bunga = Bunga
    def a(self):
        print('========================')
        print("Nama Mobil: " + self.Nama)
        print('Merk :' + self.Merk)
        print('Jenis :' + self.Jenis)
        print('Warna :' + self.Warna)
        print('Harga : Rp.' , self.Harga)
        print('=========================')
        print('Cicilan perbulan dengan bunga' , self.Bunga , '%% adalah : Rp.', (self.Harga+(self.Harga*self.Bunga/100))/12)

Nama = str(input("Masukkan Nama Mobil: "))
Merk = str(input("Masukkan Merk Mobil: "))
Jenis = str(input("Masukkan Jenis Mobil: "))
Warna = str(input("Masukkan Warna Mobil: "))
Harga = int(input("Masukkan Harga Mobil(Rp.): "))
Bunga = int(input("Masukkan Bunga Mobil(%): "))

M = Mobil(Nama, Merk, Jenis, Warna, Harga, Bunga)

M.a()
