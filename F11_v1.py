import Parser

def search_game_at_store() :
    # User Input parameter game yang akan dicari
    game_id = input("Masukkan ID game: ")
    name = input("Masukkan Nama game: ")
    harga = input("Masukkan Harga game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    count = 0
    print("Daftar game pada toko yang memenuhi kriteria : ")
    game = Parser.fill("game.csv")
    # Mengecek Validasi
    if game_id != "" and name != "" and harga == "" and kategori == "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game[i][1] == name:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name != "" and harga != "" and kategori == "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game[i][1] == name and game[i][4] == harga :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name != "" and harga != "" and kategori != "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game[i][1] == name and game[i][4] == harga  and game [i][2] == kategori :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name != "" and harga != "" and kategori != "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game[i][1] == name and game[i][4] == harga  and game [i][2]== kategori and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name == "" and harga != "" and kategori == "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game[i][4] == harga :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name == "" and harga != "" and kategori != "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game [i][2] == kategori and game[i][4] == harga  :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name == "" and harga != "" and kategori != "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game [i][2] == kategori and game[i][4] == harga  and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name == "" and harga == "" and kategori != "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game [i]:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name == "" and harga == "" and kategori != "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game [i][2] == kategori and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name == "" and harga == "" and kategori == "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name != "" and harga != "" and kategori == "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == name and game[i][4] == harga :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name != "" and harga != "" and kategori != "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == name and game[i][4] == harga  and game [i]:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name != "" and harga != "" and kategori != "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == name and game[i][4] == harga  and game [i][2] == kategori and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name != "" and harga == "" and kategori != "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == name and game [i]:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name != "" and harga == "" and kategori != "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == name and game [i][2] == kategori and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name != "" and harga == "" and kategori == "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == name and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name == "" and harga != "" and kategori != "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][4] == harga  and game [i]:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name == "" and harga != "" and kategori != "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][4] == harga  and game [i][2] == kategori and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name == "" and harga != "" and kategori == "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][4] == harga  and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name == "" and harga == "" and kategori != "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game [i][2] == kategori and game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name == "" and harga == "" and kategori == "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game [i][3] == tahun_rilis:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id != "" and name == "" and harga == "" and kategori == "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == game_id:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name != "" and harga == "" and kategori == "" and tahun_rilis != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == name:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name == "" and harga != "" and kategori == "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][4] == harga :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")
    elif game_id == "" and name == "" and harga == "" and kategori != "" and tahun_rilis == "":
                for i in range (Parser.row("game.csv")):
                    if game [i][2] == kategori:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        count = count + 1
                if count == 0:
                    print("Game tidak tersedia pada toko")