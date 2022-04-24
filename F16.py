# import os
# import csvtools as csvt
# from time import sleep

# def save(database):
#     namafolder = input("Masukkan nama folder penyimpanan : ")
#     csvt.writecsv(database[0], namafolder, 'user.csv')
#     csvt.writecsv(database[1], namafolder, 'game.csv')
#     csvt.writecsv(database[2], namafolder, 'riwayat.csv')
#     csvt.writecsv(database[3], namafolder, 'kepemilikan.csv')

#     print("Saving...")
#     sleep(2)
#     print("Data telah disimpan pada folder ", namafolder, "!")

import os
import component
import Parser
import time

def save(user_file, game_file, riwayat_file, kepemilikan_file):
    folder_name = input("Masukkan nama folder penyimpanan: ")
    valid= False
    root_folder = os.getcwd()+"\\"+folder_name
    for(root, dirs, files) in os.walk(os.getcwd(), topdown=True):
        if root == root_folder:
            valid = True
    if valid:
        Parser.delete(folder_name, "user.csv")
        Parser.delete(folder_name, "game.csv")
        Parser.delete(folder_name, "riwayat.csv")
        Parser.delete(folder_name, "kepemilikan.csv")
        f= open("{}/{}".format(folder_name, "user.csv"), "a")
        # if(component.row_matrix(user_file)==0):
        #     i=0
        #     f.write(user_file[i][0]+";"+user_file[i][1]+";"+user_file[i][2]+";"+user_file[i][3]+";"+user_file[i][4]+";"+user_file[i][5]+"\n")
        # else:
        for i in range (component.row_matrix(user_file)):
            f.write(user_file[i][0]+";"+user_file[i][1]+";"+user_file[i][2]+";"+user_file[i][3]+";"+user_file[i][4]+";"+user_file[i][5]+"\n")
        f.close()
        f= open("{}/{}".format(folder_name, "game.csv"), "a")
        # if(component.row_matrix(game_file)==0):
        #     i=0                                                 
        #     f.write(game_file[i][0]+";"+game_file[i][1]+ ";"+game_file[i][2]+";"+game_file[i][3]+";"+game_file[i][4]+";"+game_file[i][5]+"\n")
        # else:
        for i in range (component.row_matrix(game_file)):
            f.write(game_file[i][0]+";"+game_file[i][1]+ ";"+game_file[i][2]+";"+game_file[i][3]+";"+game_file[i][4]+";"+game_file[i][5]+"\n")
        f.close()
        f= open("{}/{}".format(folder_name, "riwayat.csv"), "a")
        # if(component.row_matrix(riwayat_file)==0):
        #     i=0
        #     f.write(riwayat_file[i][0]+";"+riwayat_file[i][1]+";"+riwayat_file[i][2]+";"+riwayat_file[i][3]+";",riwayat_file[i][4]+"\n")
        # else:
        for i in range (component.row_matrix(riwayat_file)):
            f.write(riwayat_file[i][0]+";"+riwayat_file[i][1]+";"+riwayat_file[i][2]+";"+riwayat_file[i][3]+";",riwayat_file[i][4]+"\n")
        f.close()
        f= open("{}/{}".format(folder_name, "kepemilikan.csv"), "a")
        # if(component.row_matrix(kepemilikan_file)):
        #     i=0
        #     f.write(kepemilikan_file[i][0]+";"+kepemilikan_file[i][1]+"\n")
        # else:
        for i in range (component.row_matrix(kepemilikan_file)):
            f.write(kepemilikan_file[i][0]+";"+kepemilikan_file[i][1]+"\n")
        f.close()
        print("Saving...")
        time.sleep(2)
        print("Data telah disimpan pada folder ", folder_name, "!")
    else:
        Parser.delete(folder_name, "user.csv")
        Parser.delete(folder_name, "game.csv")
        Parser.delete(folder_name, "riwayat.csv")
        Parser.delete(folder_name, "kepemilikan.csv")
        f= open("{}/{}".format(folder_name, "user.csv"), "a")
        # if(component.row_matrix(user_file)==0):
        #     i=0
        #     f.write(user_file[i][0]+";"+user_file[i][1]+";"+user_file[i][2]+";"+user_file[i][3]+";"+user_file[i][4]+";"+user_file[i][5]+"\n")
        # else:
        for i in range (component.row_matrix(user_file)):
            f.write(user_file[i][0]+";"+user_file[i][1]+";"+user_file[i][2]+";"+user_file[i][3]+";"+user_file[i][4]+";"+user_file[i][5]+"\n")
        f.close()
        f= open("{}/{}".format(folder_name, "game.csv"), "a")
        # if(component.row_matrix(game_file)==0):
        #     i=0                                                 
        #     f.write(game_file[i][0]+";"+game_file[i][1]+ ";"+game_file[i][2]+";"+game_file[i][3]+";"+game_file[i][4]+";"+game_file[i][5]+"\n")
        # else:
        for i in range (component.row_matrix(game_file)):
            f.write(game_file[i][0]+";"+game_file[i][1]+ ";"+game_file[i][2]+";"+game_file[i][3]+";"+game_file[i][4]+";"+game_file[i][5]+"\n")
        f.close()
        f= open("{}/{}".format(folder_name, "riwayat.csv"), "a")
        # if(component.row_matrix(riwayat_file)==0):
        #     i=0
        #     f.write(riwayat_file[i][0]+";"+riwayat_file[i][1]+";"+riwayat_file[i][2]+";"+riwayat_file[i][3]+";",riwayat_file[i][4]+"\n")
        # else:
        for i in range (component.row_matrix(riwayat_file)):
            f.write(riwayat_file[i][0]+";"+riwayat_file[i][1]+";"+riwayat_file[i][2]+";"+riwayat_file[i][3]+";",riwayat_file[i][4]+"\n")
        f.close()
        f= open("{}/{}".format(folder_name, "kepemilikan.csv"), "a")
        # if(component.row_matrix(kepemilikan_file)):
        #     i=0
        #     f.write(kepemilikan_file[i][0]+";"+kepemilikan_file[i][1]+"\n")
        # else:
        for i in range (component.row_matrix(kepemilikan_file)):
            f.write(kepemilikan_file[i][0]+";"+kepemilikan_file[i][1]+"\n")
        f.close()
        print("Saving...")
        time.sleep(2)
        print("Data telah disimpan pada folder ", folder_name, "!")