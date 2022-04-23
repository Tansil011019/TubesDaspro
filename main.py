# import component
# import F04
# import F02
# import F03
# import F05
# # import F06
# # import F07
# # import F08
# # import F09
# # import F10Function
# # import F12Function
# # import F13Function
# # import F11Function
# # import f16
# # import f17
# # import f14
# # import F15
# import Parser
# import Game_Tic_Tac_Toe

# def home():
#     print("""
# __________.__                              
# \______   \__| ____   ____   _____   ____  
#  |    |  _/  |/    \ /  _ \ /     \ /  _ \ 
#  |    |   \  |   |  (  <_> )  Y Y  (  <_> )
#  |______  /__|___|  /\____/|__|_|  /\____/ 
#         \/        \/             \/        

# Menu yang dapat dipilih:
# 1. Login
# 2. Exit
# """)
# pilihan = int(input("Masukkan pilihan anda: "))
# if(pilihan == 1):
#     F03.login()
#     print("""
# _  _  ___  __  __ ___ 
# | || |/ _ \|  \/  | __|
# | __ | (_) | |\/| | _| 
# |_||_|\___/|_|  |_|___|
                        
# Menu yang bisa dipilih:
# 1. Menambah Game ke Toko Game
# 2. Mengubah Game pada Toko Game
# 3. Mengubah Stok Game di Toko
# 4. Listing Game di Toko Berdasarkan ID, Tahun Rilis dan Harga
# 5. Membeli Game
# 6. Melihat Game yang dimiliki
# 7. Mencari Game yang dimiliki dari ID dan tahun rilis
# 8. Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis 
# 9. Top Up Saldo 
# 10. Melihat Riwayat Pembelian
# 11. Help
#             """)
#     choice= int(input("Masukkan pilihan anda: "))
#     if(pilihan == 1):
#         str1 = F04. tambahgame()
#         f16.save("game.csv", str1)
# elif(pilihan == 2):
#     exit()
# else:
#     print("Pilihan anda  tidak sesuai.")
#     home()