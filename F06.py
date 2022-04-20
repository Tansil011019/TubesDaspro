import Parser
import component



def ubah_stok(gameM):
# KAMUS LOKAL
# id_game : string          {id game yang akan diubah stok nya}
# i : int                   {indeks game pada file game.csv}
# gameM : list[list[str]]   {matriks}
# jumlah : int              {jumlah stok yang akan ditambah/dikurangi}
# new_stok : int            {stok game setelah ditambah/dikurangi}

    id_game = input("Masukkan ID game: ")
    i = component.indeks(id_game,0,gameM)
    # i = component.check_location(id_game,0,"game.csv")

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