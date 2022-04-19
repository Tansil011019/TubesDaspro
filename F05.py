import component
import Parser

#Mengubah Game Pada Toko
def ubah_game():
    #Mengambil input
    id = input("Masukkan ID game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    #Menentukan validasi 
    if id == "" :
        print("Mohon input ID.")
    else :
        loc= component.check_location(id,0,"game.csv")
        matrix = Parser.fill("game.csv")
        len = Parser.row("game.csv")
        if(nama_game!=""):
            matrix[loc][1]= nama_game
        if(kategori != ""):
            matrix[loc][2]= kategori
        if(tahun != ""):
            matrix[loc][3]= tahun
        if(harga != ""):
            matrix[loc][4]= harga
        Parser.delete("game.csv")
        f= open("game.csv", "a")
        for i in range(len):
            f.write(matrix[i][0]+";"+matrix[i][1]+";"+matrix[i][2]+";"+matrix[i][3]+";"+matrix[i][4]+";"+matrix[i][5]+"\n")
        f.close()
        # for i in range (Parser.row("game.csv")):
        #     print(matrix[i][0])
