<<<<<<< HEAD
import F16
import sys
def exit(user_file, game_file, riwayat_file, kepemilikan_file) :
    simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while simpan != "y" and simpan != "n" and simpan != "Y" and simpan != "N" :
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if simpan == "y" or simpan == "Y" :
        F16.save(user_file, game_file, riwayat_file, kepemilikan_file)
        sys.exit()
    else :
        print()
        print("File yang sudah diubah tidak tersimpan.")
        sys.exit()
=======
def exit() :
    simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while simpan != "y" or simpan != "n" or simpan != "Y" or simpan != "N" :
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if simpan == "y" or simpan == "Y" :
        save()
    else :
        print()
        print("File yang sudah diubah tidak tersimpan.")
        pass
>>>>>>> ade5631022edb7529872212d67bb0bd4d79d25d4
