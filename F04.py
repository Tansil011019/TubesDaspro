import Parser
import component

#Tambah Game
def tambahgame():
    #Mengambil input
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun = int(input("Masukkan tahun rilis: "))
    harga = input("Masukkan harga: ")
    stok = int(input("Masukkan stok awal: "))
    #Cek validasi
    if(nama_game == "" or kategori == "" or tahun == "" or harga == "" or stok == ""):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNM0.")
        tambahgame()
    else:
        id = Parser.row("game.csv")+1
        id = str(id)
        len = component.strlen(id)
        new_id= ["" for i in range(3)]
        for i in range(2, -1, -1):
            if(len==0):
                new_id[i] = "0"
            else:
                new_id[i] = id[len-1]
                len-=1
        id_str= ""
        for i in range(component.strlen(new_id)):
            id_str += new_id[i]
        # print(id_str, id, len, new_id)
        # f= open("game.csv", "a")
        # f.write("Game"+id_str+";"+nama_game+";"+kategori+";"+str(tahun)+";"+harga+";"+str(stok)+"\n")
        # f.close()
        # print("Selamat! Berhasil menambahkan game {}.".format(nama_game))
        string = "Game"+id_str+";"+nama_game+";"+kategori+";"+str(tahun)+";"+harga+";"+str(stok)+"\n"
        return string

#Harga Converter
def harga_int(x):
    harga =""
    for i in x:
        if(i!="."):
            harga+=i
    harga= int(harga)
    return harga