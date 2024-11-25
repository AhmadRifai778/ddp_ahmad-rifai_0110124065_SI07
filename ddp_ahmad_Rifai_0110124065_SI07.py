#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0
print('------ Soal No 1 ------')

def celcius_ke_fahrenheit(celcius):
    hasil_konversi = (celcius * 9/5) + 32
    return hasil_konversi

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))
print(celcius_ke_fahrenheit(1000)) 

#nomor2
print('------ Soal No 2 ------')

def is_genap(angka):
    return angka % 2 == 0
print(is_genap(4))
print(is_genap(7))

#nomor3
#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai(60) #gagal
print('------ Soal No 3 ------')

def nilai_kelulusan(nilai):
    print()
    if nilai >= 80:
        return 'lulus'
    else :
        return 'gagal'
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))



# soal no 4
print('------ Soal No 4 ------')

#Fungsi untuk menampilkan bilangan ganjil yang kurang argumens
def bilangan(n): #parameter
    ganjil = [str(i) for i in range(1, n, 2)] 
    print(",".join(ganjil))

bilangan(20)