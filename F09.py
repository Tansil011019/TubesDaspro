import Parser
import component

def list_game(user_id,kepemilikanM,gameM):
    # kepemilikan = Parser.fill("kepemilikan.csv")
    # game = Parser.fill("game.csv")
    # len = Parser.row("kepemilikan.csv")
    len = component.row_matrix(kepemilikanM)
    found = component.indeks(user_id,1,kepemilikanM) != len
    if not found :
        print("Maaf, kamu belum memiliki game apapun")
    else:
        no = 1
        for i in range(len):
            if kepemilikanM[i][1] == user_id :
                i_game = component.indeks(kepemilikanM[i][0],0,gameM)
                print("{no}. {id_game} | {nama_game:30} | {kategori:9} | {tahun} | {harga:9}".format(no= no,id_game = gameM[i_game][0],nama_game = gameM[i_game][1], kategori = gameM[i_game][2], tahun = gameM[i_game][3], harga = gameM[i_game][4]))
                no+=1