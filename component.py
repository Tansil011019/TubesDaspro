import Parser

#Komponen F02

#Mengecek Data Unik
def check_unique(username):
    file = Parser.fill("user_file.csv")
    username_valid = True
    # password_valid = True 
    for i in range (Parser.row("user_file.csv")):
        if(file[i][2]==username):
            username_valid = False
    return (username_valid)

#Mengecek Data Invalid
def check_datainput(username):
    for i in username :
        if((i>="0" and i<="9") or (i>="A" and i<="Z") or (i>="a" and i<="z") or i=="-" or i=="_"):
            username_valid = True
        else:
            username_valid = False
            break
    return (username_valid)

#Komponen F03

#Mengecek apakah sudah terdaftar
def check_validation(username, password):
    matrix = Parser.fill("user_file.csv")
    for i in range (Parser.row("user_file.csv")):
        if(username == matrix[i][2] and password == matrix[i][3]):
            x = True
            break
        else:
            x = False
    return x

#Mengecek Lokasi
def check_location(username):
    matrix = Parser.fill("user_file.csv")
    sum = 0
    for i in range (Parser.row("user_file.csv")):
        if(username == matrix[i][2]):
            break
        else:
            sum+=1
    return sum

#Mengecek admin dan user
def check_admin():
    matrix = Parser.fill("user_file.csv")
    if log_activity():
        username = Parser.fill("data_user_login.csv")
        if(matrix[check_location(username[0][0])][4]=="admin"):
            return True
        else:
            return False
    else:
        mencobasesuatu()

#Mengecek login activity
def log_activity():
    if(Parser.row("data_user_login.csv")==0):
        return False
    else:
        return True

#Mencoba Sesuatu
def mencobasesuatu():
    if log_activity():
        print("Sudah Login")#Terserah mau buat apa
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”")

#Hanya User
def hanya_user():
    if check_admin():
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    else :
        print("Silahkan")#Terserh mau ngapain

#Hanya Admin
def hanya_admin():
        if check_admin():
            print("Silahkan")#Terserh mau ngapain
        else :
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")

#Komponen Komplementer
# def logout():
#     f= open("data_user_login.csv", "a")
#     f.write("")