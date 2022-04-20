import Parser
import F03

#Mengecek Data Unik
def check_unique(x, kolum, y):
    file = Parser.fill(y)
    username_valid = True
    # password_valid = True 
    for i in range (Parser.row(y)):
        if(file[i][kolum]==x):
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
    matrix = Parser.fill(z)
    for i in range (Parser.row(z)):
        if(x == matrix[i][kolumx] and y == matrix[i][kolumy]):
            z = True
            break
        else:
            z = False
    return z

#Mengecek Lokasi
def check_location(x, kolum, z):
    matrix = Parser.fill(z)
    sum = 0
    for i in range (Parser.row(z)):
        if(x == matrix[i][kolum]):
            break
        else:
            sum+=1
    return sum

#Mengecek admin dan user
def check_admin():
    matrix = Parser.fill("user.csv")
    if log_activity():
        username = Parser.fill("data_user_login.csv")
        if(matrix[check_location(username[0][0],2)][4]=="admin"):
            return True
        else:
            return False
    else:
        F03.mencobasesuatu()

#Mengecek login activity
def log_activity():
    if(Parser.row("data_user_login.csv")==0):
        return False
    else:
        return True

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
