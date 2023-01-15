from model.daftar_nilai import *
from view.input_nilai import *
from view.view_nilai import *


print("---------------------------------------------------")
print("--------PROJECT UAS | DAFTAR NILAI MAHASISWA-------")
print("---------------------------------------------------")

while True:
    menu = input("Menu :\n(T) Tambah Data\n(L) Lihat Data\n(U) Ubah Data\n(H) Hapus Data\n(C) Cari Data\n(X) Keluar\n\nPilh Menu : ").capitalize()

    if(menu == "T"):
        input_data("Tambah")
    elif(menu == "L"):
        cetak_daftar_nilai()
    elif(menu == "U"):
        input_data("Ubah")
    elif(menu == "H"):
        input_data("Hapus")
    elif(menu == "C"):
        input_data("Cari")
    elif(menu == "X"):
        print("Keluar dari program..")
        break