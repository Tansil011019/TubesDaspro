import Parser
import component

#Login

print("""
>>>>>>>>>>
LOGIN PAGE
>>>>>>>>>>
""")

#Mengambil input dari pengguna
username = input("Masukan username: ")
password = input("Masukan password: ")

matrix = Parser.fill("user_file.csv")

f= open("data_user_login.csv", "a")
#Konfirmasi User
if component.check_validation(username, password):
    f.write(username+";"+"\n")
    print("Halo {}! Selamat datang di \"Binomo\"". format(matrix[component.check_location(username)][1]))
else :
    print("Password dan username salah atau tidak ditemukan.")
