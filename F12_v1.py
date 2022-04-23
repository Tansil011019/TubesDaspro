import Parser
import component

def topup () :
    if component.check_admin():
        user = Parser.fill("user.csv")
        len = Parser.row("user.csv")
        username = input("Masukkan username: ")
        topupsaldo = input("Masukkan saldo: ")
        for i in range (len) :
                if user[i][1] == username:
                    user[i][5] = int(user[i][5]) + int(topupsaldo)
                    if user[i][5] >= 0 :
                        print('Top up berhasil. Saldo ' + username + ' bertambah menjadi ' + str(user[i][5]) + '.')
                        Parser.delete("user.csv")
                        f = open('user.csv', 'a')
                        for i in range(len) :
                            f.write(user[i][0]+";"+user[i][1]+";"+user[i][2]+";"+user[i][3]+";"+user[i][4]+";"+str(user[i][5]))
                        f.close()
                    else :
                        user[i][5] = int(user[i][5]) - int(topupsaldo)
                        print("Masukkan tidak valid")
                    break
        else:
            print("Tidak ada user pada database yang memenuhi kriteria.")
    else :
        print("Hanya admin yang bisa masuk ke menu ini.")
            