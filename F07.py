import component

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

def str_to_int(x):
# mengembalikan hanya nilai integer dari string.
    integer = ""
    for i in x:
        if 48 <= ord(i) <= 57:
            integer += i
    return int(integer)
