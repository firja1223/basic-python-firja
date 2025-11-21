###############
#STRING .py
# Input dan Memilih #
###############

#(membuat daftar menu dan user diminta untuk input pilihannya)

print("   Menu")
print("1. Daftar mahasiswa")
print("2. Tambah mahasiswa")
print("3. Cari mahasiswa")
print("4. Ubah data mahasiswa")
print("5. Hapus data mahasiswa")


pilihan = (input("pilihan"))
print(f"Anda memilih {pilihan}.")


#----------------------------------------------------------------------------------------
###############
#STRING .py
# Input dan Eksekusi #
###############

#(awal menggunakan float, float adalah bilangan desimal atau berkoma)

# Minta radius
radius = input("Radius:")     #meminta user untuk menginput data radius
radius = float(radius)        #ini adalah fungsi konversi tipe data

# Hitung Eksekusi
pi = 3.14156
luas_lingkaran = pi * radius * radius
keliling_lingkaran = 2 * pi * radius

# Tampilkan hasil
print(f"Keliling ={keliling_lingkaran:6.2f}.")
print(f"Luas ={luas_lingkaran:6.2f}.")


#----------------------------------------------------------------------------------------
###############
#STRING .py
# Input dan Mengganti #
###############

#(memebuat input variabel awal besar, input variabel akhir kecil)

nama_depan = input("Nama depan")
nama_belakang = input("Nama belakang")

nama_depan = nama_depan.strip()
nama_belakang = nama_belakang.strip()

nama_depan = nama_depan.upper()             #upper berfungsi untuk membuat semua di variabel yang ditentukan akan besar semua / biasa disebut CAPSLOCK
nama_belakang = nama_belakang.lower()       #lower berfungsi untuk membuat semua di variabel yang ditentukan akan kecil semua / biasa disebut non-CAPSLOCK

print("Nama anda: {} {}".format(nama_depan, nama_belakang))


