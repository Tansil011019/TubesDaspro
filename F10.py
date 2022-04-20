import csv
user_input = input()
userid = input()
if user_input == ("search_my_game") :
    idgameinput = input("Masukkan ID game: ")
    releaseyearinput = input("Masukkan Tahun Rilis Game: ")
    print("Daftar game pada inventory yang memenuhi kriteria:")
    if (idgameinput != "" and releaseyearinput != "") or (idgameinput != "" and releaseyearinput == "") :
        with open("kepemilikan.csv") as kepemilikan:
            with open("game.csv") as game:
                kepemilikan_reader = csv.reader(kepemilikan, delimiter=";")
                game_reader = csv.reader(game, delimiter=";")
                for row in kepemilikan_reader:
                    if row[0] == idgameinput and row[1] == userid:
                        for row in game_reader:
                            if row[0] == idgameinput :
                                print(row[0] + " | " + row[1] + " | " + row[4] + " | " + row [2] + " | " + row[3])
                        break
                else:
                    print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    elif idgameinput == "" and releaseyearinput != "":
        with open("kepemilikan.csv") as kepemilikan:
            with open("game.csv") as game:
                kepemilikan_reader = csv.reader(kepemilikan, delimiter=";")
                game_reader = csv.reader(game, delimiter=";")
                exist = False
                for row in kepemilikan_reader:
                    if row[1] == userid:
                        gameid = row[0]
                        for row in game_reader:
                            if row[0] == gameid and row[3] == releaseyearinput:
                                print(row[0] + " | " + row[1] + " | " + row[4] + " | " + row [2] + " | " + row[3])
                        break
                else:
                    print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    elif idgameinput == "" and releaseyearinput == "":
         with open("kepemilikan.csv") as kepemilikan:
            with open("game.csv") as game:
                kepemilikan_reader = csv.reader(kepemilikan, delimiter=";")
                game_reader = csv.reader(game, delimiter=";")
                exist = False
                for row in kepemilikan_reader:
                    if row[1] == userid:
                        gameid = row[0]
                        for row in game_reader:
                            if row[0] == gameid:
                                print(row[0] + " | " + row[1] + " | " + row[4] + " | " + row [2] + " | " + row[3])
                        break
                else:
                    print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
else:
    print("Invalid command")