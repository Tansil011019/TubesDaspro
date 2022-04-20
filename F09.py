import Parser
import component

def list_game(user_id):
    kepemilikan = Parser.fill("kepemilikan.csv")
    game = Parser.fill("game.csv")
    len = Parser.row("kepemilikan.csv")
    found = component.check_location(user_id,1,"kepemilikan.csv") != len
    if not found :
        print("Maaf, kamu belum memiliki game apapun")
    else:
        no = 1
        for i in range(len):
            if kepemilikan[i][1] == user_id :
                i_game = component.check_location(kepemilikan[i][0],0,"game.csv")
                print("{no}. {id_game} | {nama_game:30} | {kategori:9} | {tahun} | {harga:9}".format(no= no,id_game = game[i_game][0],nama_game = game[i_game][1], kategori = game[i_game][2], tahun = game[i_game][3], harga = game[i_game][4]))
                no+=1
list_game("2")