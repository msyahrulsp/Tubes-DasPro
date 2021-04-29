#Kamus
# Kelas Kelompok
# Nomor Kelompok
#Nama Anggota           : 1. 16520490 - Farhandika Zahrir Mufti Guenia
#                         2. 16520430 - M. Syahrul Surya Putra
#                         3. 16520120 - Yakobus Iryanto Prasethio
#                         4. 16520370 - Muhammad Rifqi Riansyah M



# Prosedur F16 - help / openHelp
# Akses : Admin, User
''' Spesifikasi :  Prosedur ini memberikan command apa-apa saja yang user bisa nikmati berdasarkan role yang dimiliki user
'''
# I.S. : parameter fungsi ini hanya role yang akan digunakan untuk menentukan apa2 saja yang bisa
# F.S. : printout command apa saj ayang bisa di nikmati oleh user
# Proses : 
'''
jika role = user dan role = admin makan user bisa melakukan ini dan jika role = admin, makan user bisa melakukan lebih dari user biasa     
'''






def openHelp(role="nouser"): #memberikan default value "nouser" ketika tidak diberikan argumen (digunakn sebelum login)
    print("============ HELP ============")
    print("login - untuk melakukan login ke dalam sistem")
    if role == "user" or role == "admin":
        print("carirarity - untuk mencari gadget berdasarkan rarity")
        print("caritahun - untuk mencari gadget berdaasrkan tahun ditemukan")
        if role == 'admin':
            print("tambahitem - untuk menambahkan gadget atau consumable ke dalam inventory")
            print("hapusitem - untuk menghapus gadget atau consumable dari inventory")
            print("ubahjumlah - untuk mengubah jumlah gadget atau consumable pada inventory")
            print("riwayatpinjam - untuk melihat riwayat peminjaman gadget")
            print("riwayatkembali - untuk melihat riwayat gadget yang sudah dikembalikan")
            print("riwayatambil - untuk melihat riwayat pengambilan consumable")
        print("pinjam - untuk meminjam gadget")
        print("kembalikan - untuk mengembalikan gadget yang dipinjam")
        print("minta - untuk meminta consumable")
        print("save - untuk menyimpan perubahan yang telah dilakukan")
    print("help - untuk melihat panduan command")
    print("exit - untuk keluar dari program")