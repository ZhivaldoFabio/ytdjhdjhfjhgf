# Menerima input angka dari pengguna
number = int(input("Masukkan sebuah angka: "))

# Menghitung hasil kuadrat angka menggunakan lambda function
square = (lambda x: x**2)(number)

# Mencetak hasil kuadrat
print("Hasil kuadrat dari angka", number, "adalah", square)
