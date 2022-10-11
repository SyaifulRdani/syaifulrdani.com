# namaDepan = "Syaiful"
# namaBelakang = "Rochmandani"
# Hobby = "Bulutangkis"
# Umur = "18"
# print (" Namaku  :",namaDepan, namaBelakang, "\n", "Hobbyku :",Hobby,"\n", "Umurku  :",Umur,"\n")

stop = True
while (stop):
    
    print("Selamat Datang Di Mini ATM")
    print("Silahkan Pilih option :")
    print("1. Check Uang Saya")
    print("2. Ambil Uang Saya")
    print("3. Tabung Uang Saya")
    print("4. Keluar")
    option=int(input("Silahkan Pilih Option Diatas :"))
    uang_kamu=400000
    if option==1:
        print("Uang Kamu Sisa Rp.",uang_kamu)
    elif option==2:
        print("Uang Kamu Sisa Rp. ",uang_kamu,", Mau Ambil Uang Berapa?")
        print("1. 100.000")
        print("2. 250.000")
        option2=int(input("Nomor berapa :"))
        a=100000
        b=250000
        if option2 ==1:
            print("Uang kamu sisa : ",uang_kamu-a)
        elif option2 == 2:
            print("Uang kamu sisa : ",uang_kamu-b,"\n")
        print("Terima kasih sudah bertransaksi di bank kami 🙏  ")
    elif option ==3:
        print("Saat ini uang anda",uang_kamu)
        uangmsuk=int(input("Masukkan uang kamu : "))
        uangmsuk=uangmsuk+uang_kamu
        print("Saldo non Tunai Berjumlah : ",uangmsuk)
        print("Selamat kamu berhasil menabungkan uangmu, yang hemat yaa")        
        
    elif option ==4:
        keluar=input("Keluar ? y/n : ")
        if keluar == "y" or keluar == "Y":
            stop=False
        elif keluar == "n" or keluar == "N":
            stop=True
    else:
        print("Opsi tidak ditemukan, silahkan isi kembali")