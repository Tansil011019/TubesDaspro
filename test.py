import F02
import F03
import F04
import F05
import F15
import F16
# import Parser
import component

# F04.tambahgame()
# F02.register()

# F05.ubah_game()
# F15.startsystem()
# F14.help()

# f = open("{}/{}".format("CSV", "user.csv"), "w")
# f.write("loll")
# f.close()

# data_user_matrix = Parser.fill("CSV", "user.csv")
# print(data_user_matrix)

matrix=F15.load()
# print(matrix[0])
user_file= matrix[0]
game_file= matrix[1]
# riwayat_file= matrix[2]
# kepemilikan_file= matrix[3]
# print(component.check_admin(matrix[0], "wilson123"))
# print(user_file)
# 
# print(component.check_validation("wilson13", 2, "1234", 3, matrix[0]))
# matrix=[[1,2],[1,1],[1,3]]
# print(component.row(matrix))
# F03.login(matrix[0])
# game_file= F04.tambahgame(matrix[1])
# print(game_file)
# print(component.row_matrix(game_file))
# F16.save(user_file, game_file, riwayat_file, kepemilikan_file)

# inputan= input()
# user_file = matrix[0]
while input() != "9999":
    game_file = F05.ubah_game(game_file)
    
print(game_file)


