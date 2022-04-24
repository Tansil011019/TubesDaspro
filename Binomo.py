import component
import F04
import F02
from F03 import mencobasesuatu
from F03 import login
from F03 import hanya_admin
from F03 import hanya_user
from F16 import save
from F06 import ubah_stok
from F07 import list_game_toko
from F08 import buy_game
from F09 import list_game
import F05
import F14
import F15
import F16
import F17
import Parser
import Game_Tic_Tac_Toe

def after():
    pilihan = input("Tekan Tombol Enter Untuk Lanjut")

matrix= F15.load()
user_file = matrix[0]
game_file = matrix[1]
riwayat_file = matrix[2]
kepemilikan_file= matrix[3]
valid = False

x= True
while x :
    print("""
__________.__                              
\______   \__| ____   ____   _____   ____  
 |    |  _/  |/    \ /  _ \ /     \ /  _ \ 
 |    |   \  |   |  (  <_> )  Y Y  (  <_> )
 |______  /__|___|  /\____/|__|_|  /\____/ 
      \/        \/             \/        
Welcome To Binomo
Jika anda tidak mengerti jalan kerja dari mohon panggil fungsi "help"

Masukkan Nama Fungsi: 
    """)
    # print("Masukkan Nama Fungsi: ")
    pilihan = input(">>> ")
    if(pilihan == "Login" or pilihan =="login"):
        data_login= login(user_file) 
        valid = data_login[0]
        username = data_login[1]
        # print(valid)
        after()
    elif(pilihan == "Exit" or pilihan =="exit"):
        if mencobasesuatu(valid):
            F17.exit(user_file, game_file, riwayat_file, kepemilikan_file)
    elif(pilihan == "Help" or pilihan == "help"):
        # if mencobasesuatu(valid):
        F14.help()
        after()
    elif(pilihan == "Register" or pilihan == "register"):
        if mencobasesuatu(valid):
            validasi_admin = component.check_admin(user_file, username)
            if hanya_admin(validasi_admin):
                user_file = F02.register(user_file)
                after()
    elif(pilihan == "tambah_game"):
        if mencobasesuatu(valid):
            validasi_admin = component.check_admin(user_file, username)
            if hanya_admin(validasi_admin):
                game_file = F04.tambahgame(game_file)
                after()
    elif(pilihan == "ubah_game"):
        if mencobasesuatu(valid):
            validasi_admin = component.check_admin(user_file, username)
            if hanya_admin(validasi_admin):
                game_file = F05.ubah_game(game_file)
                after()
    elif (pilihan == "ubah_stok"):
        if mencobasesuatu(valid):
            validasi_admin = component.check_admin(user_file, username)
            if hanya_admin(validasi_admin):
                game_file = ubah_stok(game_file)
                after()
    elif (pilihan == "list_game_toko"):
        if mencobasesuatu(valid):
            list_game_toko(game_file)
    elif pilihan == "buy_game":
        if mencobasesuatu(valid):
            validasi_user = component.check_admin(user_file, username)
            if hanya_user(validasi_user):
                [game_file,user_file,kepemilikan_file,riwayat_file] = buy_game(component.get_user_id(username,user_file),game_file,user_file,kepemilikan_file,riwayat_file)
    elif pilihan == "list_game":
        if mencobasesuatu(valid):
            validasi_user = component.check_admin(user_file, username)
            if hanya_user(validasi_user):
                list_game(component.get_user_id(username, user_file), kepemilikan_file, game_file)
    elif(pilihan == "save"):
        if mencobasesuatu(valid):
            save(user_file, game_file, riwayat_file, kepemilikan_file)
            after()
    else:
        print("Pilihan anda  tidak terdapat pada layanan. Silahkan menuju ke \"help\" untuk mendapatkan informasi pemakaian")



