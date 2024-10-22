def konversisuhu(temperature, value):
    # Fungsi untuk mengonversi suhu dari Celsius ke Fahrenheit atau sebaliknya
    if value == 'C':
        # Jika input adalah Celsius, konversi ke Fahrenheit
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'  # Mengembalikan suhu dalam Fahrenheit
    else:
        # Jika input adalah Fahrenheit, konversi ke Celsius
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'  # Mengembalikan suhu dalam Celsius

# Konversi dari Celsius ke Fahrenheit
celsius_temperature = 30  # Mendefinisikan suhu dalam Celsius
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'C')  # Memanggil fungsi untuk konversi
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")  # Menampilkan hasil konversi

# Konversi dari Fahrenheit ke Celsius
fahrenheit_temperature = 86  # Mendefinisikan suhu dalam Fahrenheit
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'F')  # Memanggil fungsi untuk konversi
print(f"{fahrenheit_temperature}°F dikonversi ke Celsius adalah {temperaturesuhu}°{target_value}")  # Menampilkan hasil konversi
