import Parser
import component
def riwayat(user_id):
    if component.check_admin():
        riwayat = Parser.fill("riwayat.csv")
        count = 0
        print("Daftar game: ")
        for i in range (Parser.row("riwayat.csv")) :
            if user_id == riwayat [i][3] :
                print(riwayat[i][0] + " " + riwayat[i][1] + " " + riwayat[i][2] + " "  + riwayat[i][4])
                count = count + 1
        if count == 0
            print("Tidak ada riwayat pembelian game")
    else :
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
