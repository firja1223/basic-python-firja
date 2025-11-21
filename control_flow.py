###############
#CONTROL FLOW .py
###############

#(Kode ini bertujuan untuk mengenkripsi teks menggunakan metode shift cipher sederhana (seperti Caesar cipher))

def masukan_int():
    while True:
        try:
            bilangan = int(input("bilangan: "))
            if bilangan <= 0 or bilangan > 5:
                print("Nilai harus bilangan bulat positif dan tidak melebihi 5.\n")
            else:
                return bilangan
        except ValueError:
            print("Bilangan yg dimasukkan bukan integer! Mohon diulangi.\n")

def enkripsi(teks, bilangan):
    hasil = ""
    for karakter in teks:
        hasil += chr((ord(karakter) + bilangan))
    return hasil



#------------------------------------------------------------
###############
#CONTROL FLOW .py
###############

#(meminta user memasukan suatu int positif sampai blngan itu salah, dan outputnya banyak bilangan genap yang dimasukan)

def nilai():
  genap = 0
  while True:
    try:
      bilangan = int(input("blng: "))
      if bilangan < 0:
          break
      elif bilangan % 2 == 0:
          genap += 1

    except ValueError:
      break
  return genap

a = nilai()
print(f"bilangan genap: a")


#------------------------------------------------------------
###############
#CONTROL FLOW .py
###############

#(meminta user masukan suatu pesan dan tampilan berapa huruf A dan a dalam pesan tersebut)

pesan_yang_diinput_user = input("PSN: ")

jumlah_A = pesan_yang_diinput_user.count('A')       #count itu sebagai mencari dan menghitung berapa banyak

jumlah_a = pesan_yang_diinput_user.count('a')

print(f"Ada {jumlah_A} A dan {jumlah_a} a.")