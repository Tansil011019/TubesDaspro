import component

def topup (user) :
    len = component.row_matrix(user)
    username = input("Masukkan username: ") # Masukkan username yang akan diisi saldonya
    topupsaldo = input("Masukkan saldo: ") # Masukkan jumlah saldo yang akan diisi
    for i in range (len) :
            if user[i][1] == username: # username ditemukan
                user[i][5] = int(user[i][5]) + int(topupsaldo)
                if user[i][5] >= 0 : # saldo user valid(lebih dari atau sama dengan 0)
                    user[i][5] = str(user[i][5])
                    print('Top up berhasil. Saldo ' + username + ' bertambah menjadi ' + user[i][5] + '.')
                    return user
                else : # Saldo user tidak valid(kurang dari 0)
                    user[i][5] = int(user[i][5]) - int(topupsaldo)
                    user[i][5] = str(user[i][5])
                    print("Masukkan tidak valid, saldo harus lebih atau sama dengan 0.")
                    return user
    else: # Username tidak ditemukan di databse
        print("Tidak ada user pada database yang memenuhi kriteria.")
 
            