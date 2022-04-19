import Parser
import component

#Login
def login():
    print("""
    >>>>>>>>>>
    LOGIN PAGE
    >>>>>>>>>>
    """)

    #Mengambil input dari pengguna
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    matrix = Parser.fill("user.csv")

    f= open("data_user_login.csv", "a")
    #Konfirmasi User
    if component.check_validation(username, 2, password, 3, "user.csv"):
        f.write(username+";")
        print("Halo {}! Selamat datang di \"Binomo\"". format(matrix[component.check_location(username, 2, "user.csv")][1]))
    else :
        print("Password dan username salah atau tidak ditemukan.")

#Mencoba Sesuatu
def mencobasesuatu():
    if component.log_activity():
        print("Sudah Login")#Terserah mau buat apa
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”")

#Hanya User
def hanya_user():
    if component.check_admin():
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    else :
        print("Silahkan")#Terserh mau ngapain

#Hanya Admin
def hanya_admin():
        if component.check_admin():
            print("Silahkan")#Terserh mau ngapain
        else :
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")

