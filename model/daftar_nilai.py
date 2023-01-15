

database = {}

def tambah_data(nim,nama,nt,nuts,nuas):
    nakhir = (int(nt)/100*30)  + (int(nuts)/100*35)+ (int(nuas)/100*35)
    database[nim]={"nama" : nama, "tugas":nt, "uts":nuts, "uas":nuas, "akhir" : nakhir }
    print("Data berhasil ditambahkan..")

def ubah_data(nim,nama,nt,nuts,nuas):
    nakhir = (int(nt)/100*30)  + (int(nuts)/100*35)+ (int(nuas)/100*35)
    database[nim]={"nama" : nama, "tugas":nt, "uts":nuts, "uas":nuas, "akhir" : nakhir }
    print("Data berhasil diubah..")

def hapus_data(nim):
    database.pop(nim)
    print("Berhasil menghapus data..")

def cari_data(cari_by,data):
    if cari_by == "1":
        if data in database.keys() :
            print("|{0:^3} | {1:11} | {2:<20} | {3:7} | {4:4} | {5:3} | {6:7.2f} |".format
            (1 ,data, database[data]["nama"],database[data]["tugas"],database[data]["uts"],database[data]["uas"],database[data]["akhir"]))
        else :
            print("Maaf NIM Tidak Ditemukan..")
    elif cari_by == "2" :
        for i,j in database.items():
                        if(j["nama"] == data):
                            print("|{0:^3} | {1:11} | {2:<20} | {3:7} | {4:4} | {5:3} | {6:7.2f} |".format
                            (1 ,i, database[i]["nama"],database[i]["tugas"],database[i]["uts"],database[i]["uas"],database[i]["akhir"]))
                        else :
                            print("Maaf Data dengan NAMA tersebut Tidak Ditemukan..")