import Parser
import component

def search_my_game():
    # Input parameter game yang akan dicari
    # Asumsi user sudah mempunyai userid dan tersimpan dalam variabel userid
    if not component.check_admin() :
        idgameinput = input("Masukkan ID game: ")
        releaseyearinput = input("Masukkan Tahun Rilis Game: ")
        game = Parser.fill("game.csv")
        kepemilikan = Parser.fill("kepemilikan.csv")
        print("Daftar game pada inventory yang memenuhi kriteria:")
        # Mengecek role user
        # Mengecek Validasi
        if (idgameinput != "" and releaseyearinput != "") or (idgameinput != "" and releaseyearinput == "") :
            for i in range (Parser.row("kepemilikan.csv")):
                if kepemilikan [i][1] == userid and kepemilikan [i][0] == idgameinput :
                    for i in range (Parser.row("game.csv")) :
                        if game[i][0] == idgameinput :
                            print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
                            count = count + 1                
            if count == 0 :
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
        elif idgameinput == "" and releaseyearinput != "":
            for i in range (Parser.row("kepemilikan.csv")) :
                if kepemilikan [i][1] == userid :
                    gameid = kepemilikan [i][0]
                    for i in range (Parser.row("game.csv")) :
                        if game [i][0] == gameid and game [i][3] == releaseyearinput :
                            print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4]) 
                            count = count + 1      
            if count == 0 :
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
        elif idgameinput == "" and releaseyearinput == "":
            for i in range (Parser.row("kepemilikan.csv")) :
                if kepemilikan [i][1] == userid :
                    gameid = kepemilikan [i][0]   
                    for i in range (Parser.row("game.csv")) :
                        if game[i][0] == gameid:
                            print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
                            count = count + 1        
            if count == 0 :
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    else:
        print("Hanya user yang bisa masuk ke menu ini.")
