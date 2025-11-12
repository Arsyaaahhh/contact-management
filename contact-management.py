#Program manajemen kontak
def lihat_kontak():
        if len(kontak)>0: # Mengecek apakah list kontak tidak kosong
            for num, item in enumerate(kontak, start=1): #fungsi enumerate untuk menampilkan index dan item
                print(f'{num}. {item["nama"]} ({item["nomor_hp"]}, {item["email"]})') #menampilkan kontak
        else:
            print("Kosong")
            return 1 #mengembalikan ke pilihan 1 jika list kosong

def input_kontak():
    nama = input("Masukkan nama: ")
    nomor_hp = input("Masukkan nomor: ")
    email = input("Masukkan email: ")
    kontak_baru = {"nama": nama, "nomor_hp":nomor_hp, "email":email}
    kontak.append(kontak_baru) #fungsi append untuk menamnah
    print("Berhasil menambahkan kontak!")


def hapus_kontak():
    if lihat_kontak() == 1: # Mengecek apakah list kontak kosong, kalau kosong 
        return #kembali ke menu utama(1) jika list kosong

    else:
        index_hapus = int(input("Pilih kontak yang mau dihapus: ")) #meminta input index kontak yang mau dihapus
        del kontak[index_hapus - 1] #menghapus kontak berdasarkan index yang diinput user, -1 karena index list mulai dari 0
        print("Kontak berhasil dihapus!")


kontak1 = {"nama":"hang", "nomor_hp": "081234567", "email":"hang@mail.com"}
kontak2 = {"nama":"ryan", "nomor_hp": "088234567", "email":"ryn@mail.com"}
kontak3 = {"nama":"anandu", "nomor_hp": "085234567", "email":"nndu@mail.com"}
kontak = [kontak1,kontak2,kontak3]

while True:
    print("\nMenu Kontak")
    print("1. Lihat semua")
    print("2. Tambah kontak")
    print("3. Hapus kontak")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1,2,3,4): ")

    if pilihan == "1":
        lihat_kontak()


    elif pilihan == "2":
        input_kontak()

    elif pilihan == "3":
        hapus_kontak() 

    elif pilihan == "4":
        print("Thank you :)")
        break
    else :
        print("Masukan pilihan yang benar") 