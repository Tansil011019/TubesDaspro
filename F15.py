import argparse
import Parser

def load():
    parser = argparse.ArgumentParser(description="Load CSV Folder")
    parser.add_argument("folder", type=str, help="Name of CSV Folder", nargs="?")
    args = parser.parse_args()
    # if(args is None):
    #     print ("kosong")
    folder_name = args.folder
    # print(folder_name)
    if(folder_name is None):
        print("Tidak ada nama folder yang diberikan!")
        exit()
    else:
        try:
            data_user_matrix = Parser.fill(folder_name, "user.csv")
            data_game_matrix = Parser.fill(folder_name, "game.csv")
            data_riwayat_matrix = Parser.fill(folder_name, "riwayat.csv")
            data_kepemilikan_matrix =Parser.fill(folder_name, "kepemilikan.csv")
            matrix= [data_user_matrix, data_game_matrix, data_riwayat_matrix, data_kepemilikan_matrix]
            print("Selamat datang di antar muka \"Binomo\"")
            return(matrix)
        except:
            print("Folder {} tidak ditemukan".format(folder_name))
            exit()
    
    

