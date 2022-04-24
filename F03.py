import Parser
import component
# from Binomo import home

#Login
def login(matrix):
    print("""
  _              _        ___               
 | |   ___  __ _(_)_ _   | _ \__ _ __ _ ___ 
 | |__/ _ \/ _` | | ' \  |  _/ _` / _` / -_)
 |____\___/\__, |_|_||_| |_| \__,_\__, \___|
           |___/                  |___/  
    """)

    #Mengambil input dari pengguna
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    # f= open("data_user_login.csv", "a")
    #Konfirmasi User
    
    if component.check_validation(username, 2, password, 3, matrix):
        # f.write(username+";")
        print("Halo {}! Selamat datang di \"Binomo\"". format(matrix[component.check_location(username, 2, matrix)][1]))
        return(True, username)
    else :
        print("Password dan username salah atau tidak ditemukan.")
        # Binomo.page()
        return(False, "")

#Mencoba Sesuatu
def mencobasesuatu(valid):
    if valid:
#         print("""
#  _  _  ___  __  __ ___ 
# | || |/ _ \|  \/  | __|
# | __ | (_) | |\/| | _| 
# |_||_|\___/|_|  |_|___|

# Welcome To Binomo
# Jika anda tidak mengerti jalan kerja dari mohon panggil fungsi "help"
#         """)#Terserah mau buat apa
        return True
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”")
        # home()
        return False

#Hanya User
def hanya_user(valid):
    if (valid):
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        return False
        # home()
    else:
        return True

#Hanya Admin
def hanya_admin(valid):
    if not valid:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        return False
        # home()
    else:
        return True
# login()