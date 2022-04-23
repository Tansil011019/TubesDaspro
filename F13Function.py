import Parser
import component
def riwayat():
    if not component.check_admin() :
        riwayat = Parser.fill("riwayat.csv")
        print("Daftar game: ")
        for i in range (Parser.row("riwayat.csv")) :
            if userid == riwayat [i][3] :
                print(riwayat[i][0] + " " + riwayat[i][1] + " " + riwayat[i][2] + " "  + riwayat[i][4])
    else : print("Anda tidak memiliki hak akses. Hanya user yang boleh mengakses fitur ini.")
