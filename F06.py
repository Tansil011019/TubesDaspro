import component

def ubah_stok(gameM):
# { Mengubah stok game berdasar id game inputan pengguna dan mengembalikan
#   matriks gameM yang telah diubah stok nya }

# KAMUS LOKAL
# type game : <id_game:string, nama:string, tahun:string, harga:string,
#              stok: string>
# gameM : array [0..(component.row_matrix(gameM))-1 ] of game
# id_game : string    {id_game yang akan diubah stoknya}
# i : integer         { indeks id_game di matriks gameM }
# jumlah : integer    { perubahan stok }
# new_stok : integer  { stok baru }

# Algoritma

    id_game = input("Masukkan ID game: ")
    i = component.indeks(id_game,0,gameM)

    if i == component.row_matrix(gameM): # id_game tidak ada
        print("Tidak ada game dengan ID tersebut!")

    else: # id_game ada
        jumlah =  int(input("Masukkan jumlah: "))
        new_stok = int(gameM[i][5]) + jumlah

        if new_stok < 0: # stok baru negatif (invalid)
            print("Stok game",gameM[i][1],"gagal dikurangi karena stok kurang. Stok sekarang",gameM[i][5])

        else: # stok valid
            gameM[i][5] = str(new_stok) 
            if jumlah>=0: # stok ditambah
                x = "ditambahkan"
            else: # stok dikurangi
                x = "dikurangi"
            print(f"Stok game {gameM[i][1]} berhasil {x}. Stok sekarang: {new_stok}")
    return gameM