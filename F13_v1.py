import component
def riwayat(user_id,riwayat):
    count = 0
    print("Daftar game: ")
    for i in range (component.row_matrix(riwayat)) :
        if user_id == riwayat [i][3] :
            print(riwayat[i][0] + " " + riwayat[i][1] + " " + riwayat[i][2] + " "  + riwayat[i][4])
            count = count + 1
    if count == 0 :
        print("Tidak ada riwayat pembelian game")
