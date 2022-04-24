<<<<<<< HEAD
# from msilib.schema import Component


import component
def help() :
        print("""
        Untuk Administrator
=======
def help() :
    role = int(input("Masukkan role (Admin/User): "))
    if role == "Admin" :
        print("""
>>>>>>> ade5631022edb7529872212d67bb0bd4d79d25d4
        ============= HELP =============
        1. register             - Untuk melakukan registrasi user baru
        2. login                - Untuk melakukan login ke dalam sistem
        3. tambah_game          - Untuk menambah game yang dijual pada toko
        4. ubah_game            - Untuk mengubah informasi tentang game
        5. ubah_stok            - Untuk mengubah stok game yang ada di toko
<<<<<<< HEAD
        6. list_game_toko       - Untuk men-sort game berdasarkan atribut tertentu
        7. search_game_at_store - Untuk mencari game di toko
        8. topup                - Untuk men-topup saldo user
        9. help                 - Untuk memberikan panduan penggunaan sistem
        10. save                - Untuk menyimpan data
        11. exit                - Untuk keluar dari aplikasi
        """)
        print("""
        Untuk User
        ============= HELP =============
        1. login                - Untuk melakukan login ke dalam sistem
        2. list_game_toko       - Untuk men-sort game berdasarkan atribut tertentu
        3. buy_game             - Untuk membeli game 
        4. list_game            - Untuk melihat game yang dimiliki
=======
        6. list_game_toko       - Untuk melihat list game yang dijual pada toko
        7. search_game_at_store - Untuk mencari game di toko
        8. topup                - Untuk menambahkan saldo user
        9. help                 - Untuk memberikan panduan penggunaan sistem
        10. save                - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
        11. exit                - Untuk keluar dari aplikasi
        """)
    elif role == "User" :
        print("""
        ============= HELP =============
        1. login                - Untuk melakukan login ke dalam sistem
        2. list_game_toko       - Untuk melihat list game yang dijual pada toko
        3. buy_game             - Untuk membeli game yang dijual pada toko
        4. list_game            - Untuk melihat list game yang dimiliki
>>>>>>> ade5631022edb7529872212d67bb0bd4d79d25d4
        5. search_my_game       - Untuk mencari game yang dimiliki
        6. search_game_at_store - Untuk mencari game di toko
        7. riwayat              - Untuk melihat riwayat pembelian
        8. help                 - Untuk memberikan panduan penggunaan sistem
<<<<<<< HEAD
        9. save                 - Untuk menyimpan data
        10. exit                - Untuk keluar dari aplikasi
        """)
=======
        9. save                 - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
        10. exit                - Untuk keluar dari aplikasi
        """)
>>>>>>> ade5631022edb7529872212d67bb0bd4d79d25d4
