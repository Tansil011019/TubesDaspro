import Parser

print("""
-------------
REGISTER HERE
-------------
""")

#Mengecek Data Unik
def check_unique(username):
    file = Parser.fill()
    username_valid = True
    # password_valid = True 
    for i in range (Parser.row):
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
            


#Input data ke csv
nama = input("Masukan nama: ")
username = input("Masukan username: ")
password = input("Masukan password: ")
num = Parser.row + 1
f = open("user_file.csv", "a")
if(check_datainput(username)):
    if(check_unique(username)):
        f.write(str(num)+";"+nama+";"+username+";"+password+";"+"user"+";"+"0"+"\n")#Saldo = 0 karena belum ada
        print("Username {} telah berhasil register ke dalam “Binomo”.".format(username))
    else:
        print("Username {} sudah terpakai, silakan menggunakan username lain.".format(username))
else:
    print("Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")


f.close()