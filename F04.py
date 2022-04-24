import Parser
import component

#Tambah Game
def tambahgame(matrix):
    print("""
 ____  ____  __ _   __   _  _  ____   __   _  _   __   __ _     ___   __   _  _  ____       
(  _ \(  __)(  ( \ / _\ ( \/ )(  _ \ / _\ / )( \ / _\ (  ( \   / __) / _\ ( \/ )(  __)      
 ) __/ ) _) /    //    \/ \/ \ ) _ (/    \) __ (/    \/    /  ( (_ \/    \/ \/ \ ) _)       
(__)  (____)\_)__)\_/\_/\_)(_/(____/\_/\_/\_)(_/\_/\_/\_)__)   \___/\_/\_/\_)(_/(____)  

    """)
    #Mengambil input
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok = input("Masukkan stok awal: ")
    #Cek validasi
    if(nama_game == "" or kategori == "" or tahun == "" or harga == "" or stok == ""):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNM0.")
        tambahgame(matrix)
    else:
        id =component.row_matrix(matrix)+1
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
        print("Selamat! Berhasil menambahkan game {}.".format(nama_game))
        matrix += [["GAME"+id_str, nama_game, kategori, tahun, harga, stok]]
        return matrix

#Harga Converter
def harga_int(x):
    harga =""
    for i in x:
        if(i!="."):
            harga+=i
    harga= int(harga)
    return harga