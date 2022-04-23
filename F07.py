import component


def list_game_toko(gameM):
# { I.S matriks game M terdefinisi }
# { F.S menampilkan matriks game yang terurut berdasarkan skema sorting inputan user}

# KAMUS LOKAL
# type game : <id_game:string, nama:string, tahun:integer, harga:integer,
#              stok:integer>
# gameM : array [1...N] of game
# skema_sort : string
# sort_by : string
# order : char
# index_urut : array [1..N] of integer
# i : integer

# ALGORITMA
    skema_sort = input("Skema sorting : ")

    if not (isValid_skema_sort(skema_sort)):
        print("Skema sorting tidak valid")

    else :
        # memisahkan skema_sort menjadi sort_by dan order
        sort_by = ""
        order = ''
        for i in (skema_sort + '+'):
            if i == '+' or i == '-':
                order = i
                break
            sort_by += i
        
        index_urut = idx_urut_game(sort_by, order, gameM)

        # mencetak daftar game yang terurut dilayar
        n=1
        print("{n:2}.| {id_game} | {nama_game:30} | {harga:9} | {tahun} | {stok:5}".format(n="No",id_game = "ID game",nama_game = "Nama Game", harga = "Harga", tahun = "Tahun", stok = "Stok"))
        for i in index_urut:
            print("{n:2}.| {id_game} | {nama_game:30} | {harga:9} | {tahun}  | {stok:5}".format(n=n,id_game = gameM[i][0],nama_game = gameM[i][1], harga = gameM[i][4], tahun = gameM[i][3], stok = gameM[i][5]))
            n += 1



def idx_urut_game(sort_by, order,gameM):
# Fungsi mengembalikan array of integer yang berisi indeks dari game yang terurut berdasarkan atribut sort_by 
# dan terurut secara order (+ membesar, - mengecil. 

# KAMUS LOKAL
# row : int      { panjang matriks gameM }
# column : int   { kolom matriks yang menjadi dasar sorting}
# T, Treverse : array [1..row] of integer  { menampung urutan indeks matriks gameM }
# Pass, IMax,Temp : int
     
# ALGORITMA
    row = component.row_matrix(gameM)

    if sort_by == "tahun":
        column = 3
    elif sort_by == "harga":
        column = 4
    else:
        column = 0

    # menginisiasi T dengan [0...len-1] (T berisi indeks game)
    T = [i for i in range(row)]

    # mengurutkan T berdasarkan atribut column secara descending
    for Pass in range(row-1):
        IMax = Pass
        for i in range(Pass+1, row):
            if str_to_int(gameM[T[IMax]][column]) < str_to_int(gameM[T[i]][column]):
                IMax = i
        Temp = T[IMax]
        T[IMax] = T[Pass]
        T[Pass] = Temp
    
    # mengembalikan T jika descending, reverse dari T jika ascending
    if order == '-':
        return T
    else:
        Treverse = [T[i] for i in range(row-1,-1,-1)]
        return Treverse
    
def isValid_skema_sort(x):
# mengembalikan true jika skema sort valid, false jika salah
    return x =="tahun+"or x=="tahun-"or x=="harga+" or x=="harga-" or x==""

def str_to_int(x):
# mengembalikan hanya nilai integer dari string.
    integer = ""
    for i in x:
        if 48 <= ord(i) <= 57:
            integer += i
    return int(integer)
