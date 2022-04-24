def panjang_array(array):
    length = 0
    for i in array:
        length += 1
    return length


def append(array1, array2):
    return array1 + array2


def printmatrix(matrix) :
    baris = panjang_array(matrix)
    kolom = panjang_array(matrix[0])
    maxlencolumn = [0 for i in range(kolom+1)]
    maxlencolumn[0] = panjang_array(str(baris-1))
    for i in range(kolom) :
        maks = panjang_array(matrix[1][i])
        for j in range(2, baris) :
            if maks < panjang_array(matrix[j][i]) :
                maks = panjang_array(matrix[j][i])
        maxlencolumn[i+1] = maks

    for i in range(1, baris) :
        print(str(i) + "." + (" " * (maxlencolumn[0] - panjang_array(str(i)))), end=" ")
        for j in range(kolom) :
            data = matrix[i][j]
            if (j+1) != kolom :
                print(data + (" " * (maxlencolumn[j + 1] - panjang_array(data))), end=" | ")
            else :
<<<<<<< HEAD
                print(data + (" " * (maxlencolumn[j + 1] - panjang_array(data))))
=======
                print(data + (" " * (maxlencolumn[j + 1] - panjang_array(data))))
>>>>>>> ade5631022edb7529872212d67bb0bd4d79d25d4
