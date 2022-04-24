import component

def topup (user) :
    #if component.check_admin():
    len = component.row_matrix(user)
    username = input("Masukkan username: ")
    topupsaldo = input("Masukkan saldo: ")
    for i in range (len) :
            if user[i][1] == username:
                user[i][5] = int(user[i][5]) + int(topupsaldo)
                if user[i][5] >= 0 :
                    user[i][5] = str(user[i][5])
                    print('Top up berhasil. Saldo ' + username + ' bertambah menjadi ' + user[i][5] + '.')
                    return user
                else :
                    user[i][5] = int(user[i][5]) - int(topupsaldo)
                    user[i][5] = str(user[i][5])
                    print("Masukkan tidak valid")
                    return user
    else:
        print("Tidak ada user pada database yang memenuhi kriteria.")
            
