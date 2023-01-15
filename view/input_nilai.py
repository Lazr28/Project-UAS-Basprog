from model.daftar_nilai import *
from view.view_nilai import *

def input_data(tipe):
    if(tipe == "Tambah"):
        print("Menambahkan Data     :")
        nim = input("Masukan NIM    :")
        nama = input("Masukan Nama  :")
        nt = input("Masukan Nilai Tugas :")
        nuts = input("Masukan Nilai UTS :")
        nuas = input("Masukan UAS   :")
        tambah_data(nim,nama,nt,nuts,nuas)
    elif(tipe == "Ubah"):
        ubah_by = input("Ubah data berdasarkan : (1) NIM atau (2) Nama :")
        if (ubah_by == "1"):
            nim = input("Masukan NIM :")
            if nim in database.keys() :
                nama = input("Masukan Nama : ")
                nt = input("Masukan Nilai Tugas : ")
                nuts = input("Masukan Nilai UTS : ")
                nuas = input("Masukan UAS : ")
                ubah_data(nim,nama,nt,nuts,nuas)
            else :
                print("Maaf NIM Tidak Ditemukan..")
        
        if (ubah_by == "2" ):
            nama = input("Masukan Nama :")
            for i,j in database.items():
                if(j["nama"] == nama):
                    nim = i
                    nama = input("Masukan Nama : ")
                    nt = input("Masukan Nilai Tugas : ")
                    nuts = input("Masukan Nilai UTS : ")
                    nuas = input("Masukan UAS : ")
                    ubah_data(nim,nama,nt,nuts,nuas)
    elif(tipe =="Hapus"):
                hapus_by = input("Hapus data berdasarkan : (1) NIM atau (2) Nama :")
                if (hapus_by == "1"):
                    nim = input("Masukan NIM :")
                    if nim in database.keys() :
                        hapus_data(nim)
                    else :
                        print("Maaf NIM Tidak Ditemukan..")
        
                if (hapus_by == "2" ):
                    nama = input("Masukan Nama :")
                    found= ""
                    for i,j in database.items():
                        if(j["nama"] == nama):
                            found = i
                    if found == "" :
                        
                        print("Maaf Data dengan NAMA tersebut Tidak Ditemukan..")
                    else :
                        hapus_data(found)
    elif(tipe == "Cari"):
                cari_by = input("Cari data berdasarkan : (1) NIM atau (2) Nama :")
                if (cari_by == "1"):
                    nim = input("Masukan NIM :")
                    cetak_hasil_pencarian(cari_by,nim)
                if (cari_by == "2" ):
                    nama = input("Masukan Nama :")
                    cetak_hasil_pencarian(cari_by,nama)
                    