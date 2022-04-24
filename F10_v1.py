mport component

def search_my_game(user_id,game,kepemilikan ):
    # Input parameter game yang akan dicari
    # Asumsi user sudah mempunyai user_id dan tersimpan dalam variabel user_id
    idgameinput = input("Masukkan ID game: ")
    releaseyearinput = input("Masukkan Tahun Rilis Game: ")
    count = 0
    print("Daftar game pada inventory yang memenuhi kriteria:")
    # Mengecek role user
    # Mengecek Validasi
    if (idgameinput != "" and releaseyearinput != "") or (idgameinput != "" and releaseyearinput == "") :
        for i in range (component.row_matrix(kepemilikan)):
            if kepemilikan [i][1] == user_id and kepemilikan [i][0] == idgameinput :
                for i in range (component.row_matrix(game)) :
                    if game[i][0] == idgameinput :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
                        count = count + 1                
        if count == 0 :
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    elif idgameinput == "" and releaseyearinput != "":
        for i in range (component.row_matrix(kepemilikan)) :
            if kepemilikan [i][1] == user_id :
                gameid = kepemilikan [i][0]
                for i in range (component.row_matrix(game)) :
                    if game [i][0] == gameid and game [i][3] == releaseyearinput :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4]) 
                        count = count + 1      
        if count == 0 :
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    elif idgameinput == "" and releaseyearinput == "":
        for i in range (component.row_matrix(kepemilikan)) :
            if kepemilikan [i][1] == user_id :
                gameid = kepemilikan [i][0]   
                for i in range (component.row_matrix(game)) :
                    if game[i][0] == gameid:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
                        count = count + 1        
        if count == 0 :
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
