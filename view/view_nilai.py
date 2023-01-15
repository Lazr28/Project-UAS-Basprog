from model.daftar_nilai import *
from view.input_nilai import *


def head_tbl():
    print("=========================================================================")
    print("| No |        NIM      |       NAMA      |  TUGAS  | UTS | UAS |  AKHR  |")
    print("=========================================================================")

def foot_tbl():
    print("=========================================================================")

def cetak_daftar_nilai():
    x = 1
    head_tbl()
    for i,j in database.items():
        print("|{0:^3} | {1:11} | {2:<20} | {3:7} | {4:4} | {5:3} | {6:7.2f} |".format
        (x ,i, database[i]["nama"],database[i]["tugas"],database[i]["uts"],database[i]["uas"],database[i]["akhir"]))
        x+= 1
    foot_tbl()

def cetak_hasil_pencarian(cari,nim):
    head_tbl()
    cari_data(cari,nim)
    foot_tbl()