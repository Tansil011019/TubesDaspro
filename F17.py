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
