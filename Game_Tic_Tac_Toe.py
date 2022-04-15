def tic_tac_toe():
    chance = 9
    array = [["#" for i in range (3)] for j in range (3)]
    valid = True
    while (chance != 0):
        row_input = int(input("Masukkan baris: "))
        col_input = int(input("Masukkan kolum: "))
        row =row_input - 1
        col = col_input - 1
        if(array[row][col]=="#"):
            if(chance%2 == 0):
                array[row][col]="O"
            else:
                array[row][col]="X"
            for i in range(3):
                for j in range (3):
                    print(array[i][j], end= " ")
                print()
            if(((array[0][1]==array[0][0]==array[0][2])and(array[0][1]!="#" and array[0][0]!="#" and array[0][2]!="#")) or ((array[1][1]==array[1][0]==array[1][2])and(array[1][1]!="#" and array[1][0]!="#" and array[1][2]!="#")) or ((array[2][1]==array[2][0]==array[2][2])and(array[2][1]!="#" and array[2][0]!="#" and array[2][2]!="#"))):
                print("{} menang secara horizontal".format(array[row][col]))
                chance = 0
                valid = False
            elif(((array[0][0]==array[1][0]==array[2][0])and(array[0][0]!="#" and array[1][0]!="#" and array[2][0]!="#")) or ((array[0][1]==array[1][1]==array[2][1])and(array[0][1]!="#" and array[1][1]!="#" and array[2][1]!="#")) or ((array[0][2]==array[1][2]==array[2][2])and(array[0][2]!="#" and array[1][2]!="#" and array[2][2]!="#"))):
                print("{} menang secara vertikal".format(array[row][col]))
                chance = 0
                valid = False
            elif(((array[0][0]==array[1][1]==array[2][2])and(array[0][0]!="#" and array[1][1]!="#" and array[2][2]!="#")) or ((array[0][2]==array[1][1]==array[2][0])and(array[0][2]!="#" and array[1][1]!="#" and array[2][1]!="#"))):
                print("{} menang secara diagonal".format(array[row][col]))
                chance = 0
                valid = False
            else:
                chance-=1
        else:
            print("Slot telah terisi, silahkan pilih yang lain")
    if valid :
        print("Game Tie")
    # for i in range(3):
    #     for j in range (3):
    #         print(array[i][j], end= " ")
    #     print()