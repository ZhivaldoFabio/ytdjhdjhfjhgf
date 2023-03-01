def find_longest_word(sentence):
    # Menghapus whitespace pada awal dan akhir kalimat
    sentence = sentence.strip()

    # Memisahkan kalimat menjadi list kata-kata
    words = sentence.split()

    # Menghitung panjang setiap kata dan mencari kata terpanjang
    longest_word = max(words, key=lambda word: len(word))

    return longest_word


# Meminta pengguna untuk memasukkan sebuah kalimat
sentence = input("Masukkan sebuah kalimat: ")

# Mencari kata terpanjang dalam kalimat menggunakan function
longest_word = find_longest_word(sentence)

# Mencetak kata terpanjang yang ditemukan
print("Kata terpanjang dalam kalimat tersebut adalah:", longest_word)
