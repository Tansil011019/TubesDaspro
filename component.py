from msilib.schema import Component
import Parser
# import F03

#Mengecek Data Unik
def check_unique(x, kolum, y):
    username_valid = True
    # password_valid = True 
    for i in range (row_matrix(y)):
        if(y[i][kolum]==x):
            username_valid = False
    return (username_valid)

#Mengecek Data Invalid
def check_datainput(x):
    for i in x :
        if((i>="0" and i<="9") or (i>="A" and i<="Z") or (i>="a" and i<="z") or i=="-" or i=="_"):
            x_valid = True
        else:
            x_valid = False
            break
    return x_valid

#Mengecek apakah sudah terdaftar
def check_validation(x, kolumx, y, kolumy, z):
    for i in range (row_matrix(z)):
        if(x == z[i][kolumx] and y == z[i][kolumy]):
            return True
    return False

#Mengecek Lokasi
def check_location(x, kolum, z):
    sum = 0
    for i in range (row_matrix(z)):
        if(x == z[i][kolum]):
            break
        else:
            sum+=1
    return sum

#Mengecek admin dan user
# def check_admin():
#     matrix = Parser.fill("user.csv")
#     if log_activity():
#         username = Parser.fill("data_user_login.csv")
#         if(matrix[check_location(username[0][0],2)][4]=="admin"):
#             return True
#         else:
#             return False
#     else:
#         F03.mencobasesuatu()
def check_admin(matrix, username):
    if (matrix[check_location(username, 2, matrix)][4] == "admin"):
        return True
    return False

#Mengecek login activity
# def log_activity():
#     if(Parser.row("data_user_login.csv")==0):
#         return False
#     else:
#         return True

#Mengecek Panjang String 
def strlen(x):
    len = 0
    for i in x:
        if (i!=""):
            len +=1
    return len

#Mengecek baris di dalam matrix
def row_matrix(x):
    row = 0
    for i in x:
        row += 1
    return row

#Mengetahui indeks pada matriks
def indeks(str,kolum,matrix):
    indeks = 0
    for i in range(row_matrix(matrix)):
        if(str == matrix[i][kolum]):
            break
        else:
            indeks+=1
    return indeks

#Mendapatkan user_id dari username
def get_user_id(username,user_file):
    row = row_matrix(user_file)
    for i in range(row):
        if user_file[i][2] == username:
            return user_file[i][0]