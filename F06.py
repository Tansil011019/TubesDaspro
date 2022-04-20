import Parser
import component



def ubah_stok():
# KAMUS LOKAL
# id_game : string          {id game yang akan diubah stok nya}
# i : int                   {indeks game pada file game.csv}
# game : list[list[str]]    {matriks dari tiap elemen pada game.csv}
# jumlah : int              {jumlah stok yang akan ditambah/dikurangi}
# new_stok : int            {stok game setelah ditambah/dikurangi}

    id_game = input("Masukkan ID game: ")
    i = component.check_location(id_game,0,"game.csv")

    if i == Parser.row("game.csv"): # id_game tidak ada
        print("Tidak ada game dengan ID tersebut!")

    else: # id_game ada
        game = Parser.fill("game.csv")
        jumlah =  int(input("Masukkan jumlah: "))
        new_stok = int(game[i][5]) + jumlah

        if new_stok < 0: # stok baru negatif (invalid)
            print("Stok game",game[i][1],"gagal dikurangi karena stok kurang. Stok sekarang",game[i][5])

        else: # stok valid
            game[i][5] = str(new_stok) 
            if jumlah>=0: # stok ditambah
                x = "ditambahkan"
            else: # stok dikurangi
                x = "dikurangi"
            print(f"Stok game {game[i][1]} berhasil {x}. Stok sekarang: {new_stok}")
