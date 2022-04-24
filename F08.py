from F04 import harga_int
import component
import datetime

def buy_game(user_id,gameM,userM,kepemilikanM,riwayatM):
# { Fungsi mengembalikan (gameM, userM, kepemilikanM, riwayatM) yang berubah
#   ketika user membeli game }

# KAMUS LOKAL
# type game : <id_game: string, nama: string, tahun: integer, harga: integer,
#              stok:integer>
# type user : <user_id: string, username: string, password: string,
#              saldo:integer>
# type kepemilikan : < id_game: string, user_id: string>
# type Riwayat : <id_game: string, nama_game: string, harga: integer,
#                user_id: string, tahun: int>
# gameM : array [1..N] of game
# userM : array [1..N] of user
# kepemilikanM : array [1..N] of kepemilikan
# riwayatM : array [1..N] of riwayat
# user_id : string
# id_game : string
# i_game : integer  { indeks game yang dibeli pada matrix gameM }
# i_user : integer  { indeks user pada matrix userM }
# kepemilikan : kepemilikan
# owned : boolean
# saldo_akhir : integer  { saldo user apabila berhasil membeli game }

# ALGORITMA UTAMA
    id_game = input("Masukkan ID game: ")
    i_game = component.indeks(id_game,0,gameM)

    if i_game == component.row_matrix(gameM): # id_game tidak ada
        print("ID game tidak ditemukan")
    else:
        # mengecek apakah game sudah dimiliki user
        kepemilikan = [id_game,user_id,'','','','']
        owned = False
        for i in range(component.row_matrix(kepemilikanM)):
            if kepemilikan == kepemilikanM[i]:
                owned = True
    
        if owned:   # game sudah dimiliki user
            print("Anda sudah memiliki Game tersebut!")

        else:    # user belum memiliki game 
            # Mengecek apakah saldo user cukup dan stok game ada
            i_user = component.indeks(user_id,0,userM)
            saldo_akhir = int(userM[i_user][5])-harga_int(gameM[i_game][4])  
            if int(gameM[i_game][5]) == 0:  #stok game = 0
                print("Stok Game tersebut sedang habis")
            elif saldo_akhir < 0 : # saldo user kurang untuk membeli game
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            else: # game berhasil dibeli
                # mengganti data userM, gameM, kepemilikanM, riwayatM
                userM[i_user][5] = str(saldo_akhir)
                gameM[i_game][5] = str(int(gameM[i_game][5])- 1)
                kepemilikanM += [kepemilikan]
                curr_tahun = datetime.datetime.now().year
                riwayatM += [[id_game,gameM[i_game][1],gameM[i_game][4],user_id,str(curr_tahun)]]
                print("Game", gameM[i_game][1],"berhasil dibeli!")
    return(gameM, userM, kepemilikanM,riwayatM)
