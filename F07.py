import Parser

def list_game_toko():
# Menampilkan list game dengan skema sorting sesuai input user.
# KAMUS LOKAl
# skema_sort : str    {skema sorting inputan user}
# sort_by : str       {atribut yang di sorting}
# order : char        { + untuk ascending, - untuk descending}
# index_urut : list   {array indeks game yang telah diurutkan}
# game : list         {array yang menampung "game.csv"}
# n : int             {nomor game}

    skema_sort = input("Skema sorting : ")

    if not (isValid_skema_sort(skema_sort)):
        print("Skema sorting tidak valid")

    else :
        sort_by = ""
        order = ''
        for i in (skema_sort + '+'):
            if i == '+' or i == '-':
                order = i
                break
            sort_by += i
        game = Parser.fill("game.csv")
        index_urut = index_urutgame(sort_by, order)
        n = 1
        # mencetak daftar game yang terurut dilayar
        for i in index_urut:
            print("{n}. {id_game} | {nama_game:35} | {harga:9} | {tahun} | {stok:5}".format(n=n,id_game = game[i][0],nama_game = game[i][1], harga = game[i][4], tahun = game[i][3], stok = game[i][5]))
            n += 1

def index_urutgame(sort_by, order):
# mengembalikan array yang berisi indeks urutan game yang diurutkan sesuai sort_by dan order.
# KAMUS LOKAL
# game : str
# len : int
# sort_by : str
# order : char
# column : int
# T : list
# Pass : int
# IMax : int
# Temp : int
     
    game = Parser.fill("game.csv")
    len = Parser.row("game.csv")

    if sort_by == "tahun":
        column = 3
    elif sort_by == "harga":
        column = 4
    else:
        column = 0

    # menginisiasi T dengan [0...len-1] (T berisi indeks game)
    T = [i for i in range(len)]

    # mengurutkan T berdasarkan atribut column secara descending
    for Pass in range(len-1):
        IMax = Pass
        for i in range(Pass+1, len):
            if str_to_int(game[T[IMax]][column]) < str_to_int(game[T[i]][column]):
                IMax = i
        Temp = T[IMax]
        T[IMax] = T[Pass]
        T[Pass] = Temp
    
    # mengembalikan T jika descending, reverse dari T jika ascending
    if order == '-':
        return T
    else:
        Treverse = [T[i] for i in range(len-1,-1,-1)]
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
