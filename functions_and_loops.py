###############
#FUNCTION AND LOOPS .py
# Input, Eksekusi, Looping #
###############

#(menginput int atau biasa disebut bilangan bulat dan menggulang code sampai user menginput 0 dan total nya akan dijumlah dan dikurang)

total = 0

while True:
    b = int(input("Bilangan: "))
    if b == 0:
        break
    total += b

print(f"\nTotal = {total}")


#------------------------------------------------------------
###############
#FUNCTION AND LOOPS .py
# Pilihan #
###############

#(membuat fungsi dan user diminta memilih apa yang ada dimenu)

def menu_pilihan(input_list=None):
  #Fungsi ini didefinisikan dengan parameter opsional input_list, yang defaultnya None. Jika tidak ada argumen yang diberikan saat memanggil fungsi, input_list akan bernilai None.

    if input_list is None:
        while True:
            print("   Menu")
            print("A. Item 1")
            print("B. Item 2")
            print("C. Item 3")
            print("D. Keluar\n")
            p = input("Pilihan: ")
            if p.lower() == 'd':
                break
    else:

        for p in input_list:
            print("Menu")
            print("A. Item 1")
            print("B. Item 2")
            print("C. Item 3")
            print("D. Keluar")
            print(f"Pilihan: {p}")
            if p.lower() == 'd':
                break



#README!!!

#-pada baris ke 8 kita menggunakan fungsi "menu_pilihan"

#-pada baris ke 8 kita gunakan paramater juga "(input_list=none):" itu parameter

#pada baris 12 itulah looping "while"

#------------------------------------------------------------
###############
#FUNCTION AND LOOPS .py
# INPUT INT dan Mengulang sebanyak 15x #
###############

#(meminta user untuk memasukan interger atau bilangan bulat dan program akan membuat nilai rata rata)

# Meminta user memasukkan 15 bilangan integer dan menampilkan rata-ratanya

jumlah_bilangan = 15                          #Variabel ini menyimpan jumlah bilangan yang akan diminta.
total = 0                                     #Variabel total diinisialisasi ke 0 untuk menyimpan bilangan yang dimasukkan.

for i in range(1, jumlah_bilangan + 1):       #Loop ini berjalan dari i = 1 sampai
    bil = int(input(f"Bilangan {i:2}: "))
    total += bil                              #Menambahkan nilai bil ke total. Ini adalah shorthand untuk 'total = total + bil'.

rata_rata = total / jumlah_bilangan

print()
print(f"Rata-rata = {rata_rata:<6.2f}.")
