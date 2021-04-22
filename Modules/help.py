def openHelp(role="nouser"): #memberikan default value "nouser" ketika tidak diberikan argumen (digunakn sebelum login)
    print("============ HELP ============")
    if role == "admin":
        print("register - untuk melakukan registrasi user baru")
        print("login - untuk melaukan login ke dalam sistem")
        print("carirarity - untuk mencari gadget berdasarkan rarity")
        print("caritahun - untuk mencari gadget berdaasrkan tahun ditemukan")
        print("tambahitem - untuk menambahkan gadget atau consumable ke dalam inventory")
        print("hapusitem - untuk menghapus gadget atau consumable dari inventory")
        print("ubahjumlah - untuk mengubah jumlah gadget atau consumable pada inventory")
        print("riwayatpinjam - untuk melihat riwayat peminjaman gadget")
        print("riwayatkembali - untuk melihat riwayat gadget yang sudah dikembalikan")
        print("riwayatambil - untuk melihat riwayat pengambilan consumable")
        print("save - untuk menyimpan perubahan yang telah dilakukan")
        print("help - untuk melihat panduan command")
        print("exit - untuk keluar dari program")


    elif role == "user":
        print("login - untuk melakukan login ke dalam sistem")
        print("carirarity - untuk mencari gadget berdasarkan rarity")
        print("caritahun - untuk mencari gadget berdaasrkan tahun ditemukan")
        print("pinjam - untuk meminjam gadget")
        print("kembalikan - untuk mengembalikan gadget yang dipinjam")
        print("minta - untuk meminta consumable")
        print("save - untuk menyimpan perubahan yang telah dilakukan")
        print("help - untuk melihat panduan command")
        print("exit - untuk keluar dari program")

    elif role == "nouser":
        print("login - untuk melakukan login ke dalam sistem")
        print("help - untuk melihat panduan command")
        print("exit - untuk keluar dari program")
