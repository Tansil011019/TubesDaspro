import Parser
import component
def search_my_game():
    # Input parameter game yang akan dicari
    # Asumsi user sudah mempunyai userid dan tersimpan dalam variabel userid
    idgameinput = input("Masukkan ID game: ")
    releaseyearinput = input("Masukkan Tahun Rilis Game: ")
    game = Parser.fill("game.csv")
    kepemilikan = Parser.fill("kepemilikan.csv")
    print("Daftar game pada inventory yang memenuhi kriteria:")
    # Mengecek role user
    if component.check_admin()== False :
        # Mengecek Validasi
        if (idgameinput != "" and releaseyearinput != "") or (idgameinput != "" and releaseyearinput == "") :
            for i in range (Parser.row("kepemilikan.csv")):
                if kepemilikan [i][1] == userid and kepemilikan [i][0] == idgameinput :
                    for i in range (Parser.row("game.csv")) :
                        if game[i][0] == idgameinput :
                                print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
                    break
            else:
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
        elif idgameinput == "" and releaseyearinput != "":
            for i in range (Parser.row("kepemilikan.csv")) :
                if kepemilikan [i][1] == userid :
                    gameid = kepemilikan [i][0]
                    for i in range (Parser.row("game.csv")) :
                        if game [i][0] == gameid and game [i][3] == releaseyearinput :
                            print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])   
                    break
            else:
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
        elif idgameinput == "" and releaseyearinput == "":
            for i in range (Parser.row("kepemilikan.csv")) :
                if kepemilikan [i][1] == userid :
                    gameid = kepemilikan [i][0]   
                    for i in range (Parser.row("game.csv")) :
                        if game[i][0] == gameid:
                            print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
            
                    break
            else:
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    else: print ("Anda tidak memiliki hak akses. Hanya user yang boleh mengakses fitur ini.")