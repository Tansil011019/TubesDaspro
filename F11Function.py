import Parser

def search_game_at_store() :
    # User Input parameter game yang akan dicari
    idgame = input("Masukkan ID game: ")
    gamename = input("Masukkan Nama game: ")
    price = input("Masukkan Harga game: ")
    category = input("Masukkan Kategori Game: ")
    releaseyear = input("Masukkan Tahun Rilis Game: ")
    print("Daftar game pada toko yang memenuhi kriteria : ")
    game = Parser.fill("game.csv")
    # Mengecek Validasi
    if idgame != "" and gamename != "" and price == "" and category == "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][1] == gamename:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename != "" and price != "" and category == "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][1] == gamename and game[i][2] == price:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename != "" and price != "" and category != "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][1] == gamename and game[i][2] == price and game[i][3] == category:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename != "" and price != "" and category != "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][1] == gamename and game[i][2] == price and game[i][3] == category and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename == "" and price != "" and category == "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][2] == price:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename == "" and price != "" and category != "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][3] == category and game[i][2] == price :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename == "" and price != "" and category != "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][3] == category and game[i][2] == price and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename == "" and price == "" and category != "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][3] == category:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename == "" and price == "" and category != "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][3] == category and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename == "" and price == "" and category == "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename != "" and price != "" and category == "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == gamename and game[i][2] == price:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename != "" and price != "" and category != "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == gamename and game[i][2] == price and game[i][3] == category:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename != "" and price != "" and category != "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == gamename and game[i][2] == price and game[i][3] == category and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename != "" and price == "" and category != "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == gamename and game[i][3] == category:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename != "" and price == "" and category != "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == gamename and game[i][3] == category and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename != "" and price == "" and category == "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == gamename and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename == "" and price != "" and category != "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][2] == price and game[i][3] == category:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename == "" and price != "" and category != "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][2] == price and game[i][3] == category and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename == "" and price != "" and category == "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][2] == price and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename == "" and price == "" and category != "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][3] == category and game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename == "" and price == "" and category == "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][4] == releaseyear:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame != "" and gamename == "" and price == "" and category == "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][0] == idgame:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename != "" and price == "" and category == "" and releaseyear != "":
                for i in range (Parser.row("game.csv")):
                    if game[i][1] == gamename:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename == "" and price != "" and category == "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][2] == price:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")
    elif idgame == "" and gamename == "" and price == "" and category != "" and releaseyear == "":
                for i in range (Parser.row("game.csv")):
                    if game[i][3] == category:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][4] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][5])
                        break
                else:
                    print("Game tidak tersedia pada toko")