###############
#MATH .py
# Input dan Eksekusi #
###############

#(meminta user untuk menginput radius dan tinggi, lanjut dieksekusi menggunakan rumus)

#inputan user
Radius = float(input("Radius: "))       #jenis data yang diminta dan disimpan di variabel radius adalah bilangan desimal atau berkoma
Tinggi = float(input("Tinggi: "))       #jenis data yang diminya dan disimpan di variabel tinggi adalah bilangan desimal atau berkoma

#rumus dengan eksekusi
pi = 3.14                               #ini adalah pi yang biasa kita kenal 3.14, pi ini dijadikan sebagai variabel
volume= pi * Radius**2 * Tinggi         #eksekusi
luas_alas= pi * Radius**2               #eksekusi
luas_atas= pi * Radius**2               #eksekusi
luas_selimut= 2 * pi * Radius * Tinggi  #eksekusi

#output

print()
print(f".     Volume: {volume:<5,.2f}")
print(f".  Luas alas: {luas_alas:<5.2f}")
print(f".  Luas atas: {luas_atas:<5.2f}")
print(f"Luas selimut: {luas_selimut:<5,.2f}")



##README!!!

#disini kita menggunakan operator;

#"*" = sebagai kali

#"**" = sebagai pangkat

#ket. 22-25

#+++ ":<" itu menunjukan left-align (rata kiri) +++ "5" sebagai space (space ditambah disitu) +++ "," koma disitu sebgai pemisah +++ ".2f" sebagai float jadi misal output aslinya 3,918 jadi 3,91

#------------------------------------------------------------------------------------------
###############
#MATH .py
# Input dan Eksekusi #
###############

#(menginput data float dan eksekusi rill dan bilangan imajiner)

#input
rill_1     = float(input("Masukkan bilangan riil 1: "))
imajiner_1 = float(input("Masukkan bilangan imajiner 1: "))
rill_2     = float(input("Masukkan bilangan riil 2: "))
imajiner_2 = float(input("Masukkan bilangan imajiner 2: "))

#eksekusi
hasil_rill = rill_1 * rill_2 - imajiner_1 * imajiner_2
hasil_imajiner = rill_1 * imajiner_2 + rill_2 * imajiner_1

#output
print()
print(f"({rill_1} + {imajiner_1}j) * ({rill_2} + {imajiner_2}j) = {hasil_rill:.1f} + {hasil_imajiner}j")


#README!!!

#pada tugas ke 18 ini kita disuruh untuk membuat program atau code dengan sistem kerja user menginput nilai rill dan imajiner lalu program memisahkan dan memberi output jika bilangan itu rill maka output tidak ada variabel (j,i,k) lalu sebalikanya bilangan imajiner akan diberi variabel (j,i,k) agar user dapat mengetahui bahwa bilangan ini imajener.


#------------------------------------------------------------------------------------------
###############
#MATH .py
# Input dan Eksekusi #
###############

#(menginput float dan eksekusi dengan rumus di variabel c)

a = float(input("Masukkan sisi a: "))
b = float(input("Masukkan sisi b: "))

c = (a**2 + b**2)**0.5


print(f"\nSisi C =  {c:.2f}")


