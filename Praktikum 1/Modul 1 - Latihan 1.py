# -*- coding: utf-8 -*-
"""
@Materi: Fungsi Main
@Judul: Praktikum 1 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

def beratbarang(berat):
    while berat<=0 :
        berat=int(input("Masukkan berat barang Anda: "))
        return berat

def main():
    berat=int(input("Masukkan berat barang Anda: "))
    beratbarang(berat)
    print ("Tujuan kotanya adalah", tujuankota())
    print ("Harganya adalah" , berat*10000)

def tujuankota():
    tujuan = str(input("Masukkan nama kota tujuan Anda: "))
    return tujuan

if __name__ == "__main__":
    main()
