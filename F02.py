import Parser
import component

def register():
    print("""
    -------------
    REGISTER HERE
    -------------
    """)          

    #Input data ke csv
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    num = Parser.row("user.csv") + 1
    f = open("user.csv", "a")
    if(component.check_datainput(username)):
        if(component.check_unique(username, 2, "user.csv")):
            f.write(str(num)+";"+nama+";"+username+";"+password+";"+"user"+";"+"0"+"\n")#Saldo = 0 karena belum ada
            print("Username {} telah berhasil register ke dalam “Binomo”.".format(username))
        else:
            print("Username {} sudah terpakai, silakan menggunakan username lain.".format(username))
    else:
        print("Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")


    f.close()