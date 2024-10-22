import math  # Mengimpor library untuk operasi matematika

# Lambda function untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r * r  # Fungsi lambda yang menerima jari-jari r dan menghitung luas lingkaran

# Contoh penggunaan
jari_jari = 7  # Mendefinisikan jari-jari lingkaran
area = luas_lingkaran(jari_jari)  # Memanggil fungsi lambda untuk menghitung luas berdasarkan jari-jari

# Menampilkan hasil dengan format dua desimal
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")  # Mencetak luas lingkaran dengan format dua angka desimal
