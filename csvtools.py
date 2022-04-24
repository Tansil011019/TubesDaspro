import arraytools as at
import os


def csvtoarray(namafolder, namafile) :
    # Definisi dan Spesifikasi
    # Mengubah isi file CSV menjadi matrix (array of array) 
   
    # KAMUS LOKAL
    #

    # ALGORITMA
    openedfile = open(f'{namafolder}/{namafile}', 'r')
    string = openedfile.read()
    openedfile.close()

    banyak_baris = 0
    banyak_kolom = 0

    for i in string:
        if i == ';' and banyak_baris == 0:
            banyak_kolom += 1
        elif i == '\n':
            banyak_baris += 1
    banyak_kolom += 1

    matrix = [['' for i in range(banyak_kolom)] for j in range(banyak_baris)]
    indeks_kolom = 0
    indeks_baris = 0

    for i in string :
        if i == '\n':
            indeks_baris += 1
            indeks_kolom = 0
        elif i == ';' :
            indeks_kolom += 1
        else :
            matrix[indeks_baris][indeks_kolom] += i
    return matrix

    # Aplikasi
    # userdata = csvtoarray('user.csv')


def writecsv(matrix, namafolder, namafile) :
    banyak_baris = at.panjang_array(matrix)
    banyak_kolom = at.panjang_array(matrix[0])

    string = ''

    for i in range(banyak_baris) :
        for j in range(banyak_kolom) :
            string += str(matrix[i][j])
            if j != (banyak_kolom - 1) :
                string += ';'
        if i != (banyak_baris - 1) :
            string += '\n'

    if not isfoldervalid(namafolder) :
        os.makedirs(namafolder)

    openedfile = open(f'{namafolder}/{namafile}', 'w')
    openedfile.write(string)
    openedfile.close()

    # Aplikasi
    # writecsv(userdata, 'CSVFiles', 'user.csv')


def isfoldervalid(namafolder) :
    folderpython = os.getcwd()
    foldertujuan = os.path.join(folderpython, rf'{namafolder}')
    if os.path.exists(foldertujuan) :
        return True
    else :
<<<<<<< HEAD
        return False
=======
        return False
>>>>>>> ade5631022edb7529872212d67bb0bd4d79d25d4
