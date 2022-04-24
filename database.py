import os
def loadCSV(folderName):
    global game_data, kepemilikan_data, riwayat_data, user_data, game_data_row, kepemilikan_data_row, riwayat_data_row, user_data_row
    csvType = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
    for i in range(4):
        csvFile = open("./{}/{}".format(folderName, csvType[i]), 'r')
        file = csvFile.readlines()
        row = 0
        for line in file:
            row += 1
        if i == 0:
            game_data_row = row
        if i == 1:
            kepemilikan_data_row = row
        if i == 2:
            riwayat_data_row = row
        if i == 3:
            user_data_row = row

        if i == 0 or i == 3:
            col = 6
        elif i == 1:
            col = 2
        else:
            col = 5
        
        matrixData = [['' for _ in range(col)] for _ in range(row)]
        currentRow = 0
        for line in file:
            data = ""
            currentCol = 0
            for chara in line:
                if chara == ';':
                    matrixData[currentRow][currentCol] = data
                    data = ""
                    currentCol += 1
                elif chara == "\n":
                    matrixData[currentRow][currentCol] = data
                else:
                    data += chara
            currentRow += 1
        matrixData[currentRow-1][currentCol] = data
        if i == 0:
            game_data = matrixData
        elif i == 1:
            kepemilikan_data = matrixData
        elif i == 2:
            riwayat_data = matrixData
        else:
            user_data = matrixData
    csvFile.close()