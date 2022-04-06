#ReadME
#Parcell mengconvert elemen csv menjadi matriks
#Hasil yang dapat di pake adalah dimensi row dan col serta file yang digunakan adalah user_file.csv
#Fungsi fill dapat digunakan untuk mengconvert komponen csv menjadi matriks

#Menentukan dimensi csv
f = open("user_file.csv", "r")

col = 1 #kolom
row = 0 #baris
x = True

for i in f: 
    for j in i:
        if x :
            if (j == ";"):
                col += 1 
    x = False
    row+=1

f.close()

#Mengisi file dengan csv
def fill ():
    f = open("user_file.csv", "r")
    l=0
    m=0
    file = [["" for j in range (col)]for i in range (row)]


    for i in f:
        for j in i:
            if(j != ";"):
                file[l][m] += j
            else :
                m+=1
        l+=1
        m=0

    f.close()
    return(file)