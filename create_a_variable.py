###############
#PERDANA .py
# Input dan Menata #
###############

#(membuat input dan output menggunakan 3 variabel)
nama_depan_1 = input("Masukkan nama depan orang pertama: ")         #untuk meminta nama depan orang pertama (input)
nama_belakang_1 = input("Masukkan nama belakang orang pertama: ")   #untuk meminta nama belakang orang pertama (input)
nama_depan_2 = input("Masukkan nama depan orang kedua: ")           #untuk meminra nama depan orang kedua   (input)
nama_belakang_2 = input("Masukkan nama belakang orang kedua: ")     #untuk meminta nama belakang orang kedua (input)

nama_lengkap_1 = f"{nama_depan_1} {nama_belakang_1}"           #berfungsi mengumpulkan informasi data? nilai dari variabel nama depan 1 dan nama belakang 1
nama_lengkap_2 = f"{nama_depan_2} {nama_belakang_2}"           #berfungsi mengumpulkan informasi data/ nilai dari variabel nama depan 2 dan nama belakang 2

print(f"{nama_lengkap_1} berpasangan dengan {nama_lengkap_2}.")


###############
#PERDANA .py
# Input dan Menata #
###############

#(membuat input dan output menggunakan 3 variabel)

nama_depan_1 = input("Masukkan nama depan orang pertama: ")         #untuk meminta nama depan orang pertama (input)
nama_belakang_1 = input("Masukkan nama belakang orang pertama: ")   #untuk meminta nama belakang orang pertama (input)
nama_depan_2 = input("Masukkan nama depan orang kedua: ")           #untuk meminra nama depan orang kedua   (input)
nama_belakang_2 = input("Masukkan nama belakang orang kedua: ")     #untuk meminta nama belakang orang kedua (input)
nama_depan_3 = input("Masukkan nama depan orang ketiga: ")           #untuk meminra nama depan orang ketiga   (input)
nama_belakang_3 = input("Masukkan nama belakang orang ketiga: ")     #untuk meminta nama belakang orang ketiga (input)

nama_lengkap_1 = f"{nama_depan_1} {nama_belakang_1}"           #berfungsi mengumpulkan informasi data/ nilai dari variabel nama depan 1 dan nama belakang 1
nama_lengkap_2 = f"{nama_depan_2} {nama_belakang_2}"           #berfungsi mengumpulkan informasi data/ nilai dari variabel nama depan 2 dan nama belakang 2
nama_lengkap_3 = f"{nama_depan_3} {nama_belakang_3}"           #berfungsi mengumpulkan informasi data/ nilai dari variabel nama depan 2 dan nama belakang 2

print(f"Pemain 1: {nama_lengkap_1}\nPemain 2: {nama_lengkap_2}\nPemain 3: {nama_lengkap_3}")  #untuk mengeprint input dari variabel atas lalu di satukan divariabel nama lengkap lalu disatukan disinii.

###############
#PERDANA .py
# Input dan Menata #
###############

# (membuat inputan untuk 4 orang dengan 8 variabel, lalu buat seperti table)

nama_depan_1 = input("Masukkan nama depan orang pertama: ")         #untuk meminta nama depan orang pertama (input)
nama_belakang_1 = input("Masukkan nama belakang orang pertama: ")   #untuk meminta nama belakang orang pertama (input)
nama_depan_2 = input("Masukkan nama depan orang kedua: ")           #untuk meminra nama depan orang kedua   (input)
nama_belakang_2 = input("Masukkan nama belakang orang kedua: ")     #untuk meminta nama belakang orang kedua (input)
nama_depan_3 = input("Masukkan nama depan orang ketiga: ")           #untuk meminra nama depan orang ketiga   (input)
nama_belakang_3 = input("Masukkan nama belakang orang ketiga: ")     #untuk meminta nama belakang orang ketiga (input)
nama_depan_4 = input("Masukkan nama depan orang keempat: ")          #untuk meminta nama depan orang empat (input)
nama_belakang_4 = input("Masukkan nama belakang orang keempat: ")    #untuk meminta nama belakang orang empat (input)

data_orang = [ (nama_depan_1, nama_belakang_1),  (nama_depan_2, nama_belakang_2),  (nama_depan_3, nama_belakang_3), (nama_depan_4, nama_belakang_4)
]  #fungsi "[]" untuk menyimpan banyak itemm.


print("Depan    | Belakang")
print("---------+---------")
#untuk tabel

for depan, belakang in data_orang:
    print(f"{depan:<8} | {belakang:<8}")
#mencetak data dan "for" adalah sebagai loop, 8 di code print sebagai lebar minimum


