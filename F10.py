import component

def search_my_game(user_id,game,kepemilikan ):
    # Input parameter game yang akan dicari
    idgameinput = input("Masukkan ID game: ")
    releaseyearinput = input("Masukkan Tahun Rilis Game: ")
    count = 0
    print("Daftar game pada inventory yang memenuhi kriteria:")
    # Mengecek Validasi
    if (idgameinput != "" and releaseyearinput != "")  : # User hanya mengisi kedua parameter atau hanya ID game
        for i in range (component.row_matrix(kepemilikan)):
            if kepemilikan [i][1] == user_id and kepemilikan [i][0] == idgameinput :
                for i in range (component.row_matrix(game)) :
                    if game[i][0] == idgameinput and game [i][3] == releaseyearinput :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
                        count = count + 1                
        if count == 0 : # Tidak ada game yang dimiliki user yang sesuai dengan kriteria
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    elif idgameinput != "" and releaseyearinput == "":
        for i in range (component.row_matrix(kepemilikan)):
            if kepemilikan [i][1] == user_id and kepemilikan [i][0] == idgameinput :
                for i in range (component.row_matrix(game)) :
                    if game[i][0] == idgameinput :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
                        count = count + 1                
        if count == 0 : # Tidak ada game yang dimiliki user yang sesuai dengan kriteria
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    elif idgameinput == "" and releaseyearinput != "": # User hanya menginput tahun rilis
        for i in range (component.row_matrix(kepemilikan)) :
            if kepemilikan [i][1] == user_id :
                gameid = kepemilikan [i][0]
                for i in range (component.row_matrix(game)) :
                    if game [i][0] == gameid and game [i][3] == releaseyearinput :
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4]) 
                        count = count + 1      
        if count == 0 : # Tidak ada game yang dimiliki user yang sesuai dengan kriteria
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
    elif idgameinput == "" and releaseyearinput == "": # user tidak mengisi kedua parameter, akan mengeluarkan semua game yang dimiliki user
        for i in range (component.row_matrix(kepemilikan)) :
            if kepemilikan [i][1] == user_id :
                gameid = kepemilikan [i][0]   
                for i in range (component.row_matrix(game)) :
                    if game[i][0] == gameid:
                        print(game[i][0] + " | " + game[i][1] + " | " + game[i][2] + " | " + game[i][3] + " | " + game[i][4])
                        count = count + 1        
        if count == 0 :# user tidak memiliki game apapun
            print("Inventory-mu kosong.")
