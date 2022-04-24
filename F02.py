import Parser
import component

def register(matrix):
    print("""
  ___          _    _             ___               
 | _ \___ __ _(_)__| |_ ___ _ _  | _ \__ _ __ _ ___ 
 |   / -_) _` | (_-<  _/ -_) '_| |  _/ _` / _` / -_)
 |_|_\___\__, |_/__/\__\___|_|   |_| \__,_\__, \___|
         |___/                            |___/     
    """)          

    #Input data ke csv
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    num = component.row_matrix(matrix) + 1
    # f = open("user.csv", "a")
    if(component.check_datainput(username)):
        if(component.check_unique(username, 2, matrix)):
            matrix += [[str(num), nama, username, password, "user", "0"]]#Saldo = 0 karena belum ada
            print("Username {} telah berhasil register ke dalam “Binomo”.".format(username))
            return matrix
        else:
            print("Username {} sudah terpakai, silakan menggunakan username lain.".format(username))
            register(matrix)
    else:
        print("Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")
        register(matrix)


    # f.close()

# register()