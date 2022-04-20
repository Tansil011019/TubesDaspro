import Parser
import component
import datetime

def buy_game(user_id):
    id_game = input("Masukkan ID game: ")
    i_game = component.check_location(id_game,0,"game.csv")

    if i_game == Parser.row("game.csv"): # id_game tidak ada
        print("ID game tidak ditemukan")
    else:
        kepemilikan = Parser.fill("kepemilikan.csv")
        arrKepemilikan = [id_game,user_id]
        for i in range(Parser.row("kepemilikan.csv")):
            if arrKepemilikan == kepemilikan[i]:
                owned = True
            else: owned = False
    
    if owned:
        print("Anda sudah memiliki Game tersebut!")
    else:
        i_user = component.check_location(user_id,0,"user.csv")
        game = Parser.fill("game.csv")
        user = Parser.fill("user.csv")
        riwayat = Parser.fill("riwayat.csv")
        saldo_akhir = int(user[i_user][5])-int(game[i_game][4])
        if int(game[i_game][5]) == 0:
            print("Stok Game tersebut sedang habis")
        elif saldo_akhir < 0 :
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        else:
            user[i_user][5] = str(saldo_akhir)
            game[i_game][5] = int(game[i_game][5])- 1
            kepemilikan += arrKepemilikan
            curr_tahun = datetime.datetime.now().year
            riwayat += [[id_game,game[i_game][1],game[i_game][4],user_id,curr_tahun]]
            print("Game", game[i_game][1],"berhasil dibeli!")

    