numbers = input("Masukkan sekumpulan bilangan (pisahkan dengan koma): ").split(",")
numbers = list(map(int, numbers))

largest = lambda num_list: max(num_list)
smallest = lambda num_list: min(num_list)

print("Bilangan terbesar dari kumpulan bilangan yang di input adalah : ", largest(numbers))
print("Bilangan terkecil dari kumpulan bilangan yang di input adalah : ", smallest(numbers))
