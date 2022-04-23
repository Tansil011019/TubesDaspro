import component

def list_game(user_id,kepemilikanM,gameM):
# Prosedur menampilkan game yang telah dimiliki user

# KAMUS LOKAL
# type game : <id_game: string, nama: string, tahun: integer, harga: integer,
#              stok:integer>
# type user : <user_id: string, username: string, password: string,
#              saldo:integer>
# gameM : array [1..N] of game
# userM : array [1..N] of user

# ALGORITMA
    row = component.row_matrix(kepemilikanM)

    # mengecek apakah user telah memiliki game
    found = component.indeks(user_id,1,kepemilikanM) != row

    if not found : # user belum memiliki game
        print("Maaf, kamu belum memiliki game apapun")

    else: # user sudah punya game
        # menampilkan list game user ke layar
        no = 1
        print("{no:2}.| {id_game} | {nama_game:30} | {kategori:9} | {tahun} | {harga:9}".format(no= "No",id_game = "ID game",nama_game = "Nama Game", kategori = "Kategori", tahun = "Tahun", harga = "Harga"))
        for i in range(row):
            if kepemilikanM[i][1] == user_id :
                i_game = component.indeks(kepemilikanM[i][0],0,gameM)
                print("{no:2}.| {id_game} | {nama_game:30} | {kategori:9} | {tahun}  | {harga:9}".format(no= no,id_game = gameM[i_game][0],nama_game = gameM[i_game][1], kategori = gameM[i_game][2], tahun = gameM[i_game][3], harga = gameM[i_game][4]))
                no+=1