
import component
import datetime

def buy_game(user_id,gameM,userM,kepemilikanM,riwayatM):
    id_game = input("Masukkan ID game: ")
    i_game = component.indeks(id_game,0,gameM)

    if i_game == component.row_matrix(gameM): # id_game tidak ada
        print("ID game tidak ditemukan")
    else:
        arrKepemilikan = [id_game,user_id,'','','','']
        owned = False
        for i in range(component.row_matrix(kepemilikanM)):
            if arrKepemilikan == kepemilikanM[i]:
                owned = True
    
        if owned:
            print("Anda sudah memiliki Game tersebut!")
        else:
            i_user = component.indeks(user_id,0,userM)
            saldo_akhir = int(userM[i_user][5])-int(gameM[i_game][4])
            if int(gameM[i_game][5]) == 0:
                print("Stok Game tersebut sedang habis")
            elif saldo_akhir < 0 :
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            else:
                userM[i_user][5] = str(saldo_akhir)
                gameM[i_game][5] = int(gameM[i_game][5])- 1
                kepemilikanM += [arrKepemilikan]
                curr_tahun = datetime.datetime.now().year
                riwayatM += [[id_game,gameM[i_game][1],gameM[i_game][4],user_id,curr_tahun]]
                print("Game", gameM[i_game][1],"berhasil dibeli!")
    return(gameM, userM, kepemilikanM,riwayatM)

    