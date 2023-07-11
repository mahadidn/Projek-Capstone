##Bersih-bersih dataset
import pandas as pd

# Membaca file CSV ke dalam DataFrame
dataframe = pd.read_csv('company_data.csv')

# Menghitung jumlah data dengan nilai "1" pada atribut tertentu
count = (dataframe['Bankrupt?'] == 1).sum()
count2 = (dataframe['Bankrupt?'] == 0).sum()

# Menampilkan jumlah data yang memiliki nilai "1"
print("1. Total data yang ingin diprediksi")
print("Jumlah data perusahaan bangkrut '1':", count)
print("Jumlah data perusahaan tidak bangkrut '0':", count2)
#3####################################################################
import pandas as pd

# Membaca file CSV
df = pd.read_csv('company_data.csv')

# Menentukan kriteria penghapusan baris
kriteria = df['Bankrupt?'].astype(str).str.contains('0')

# Memilih baris yang memenuhi kriteria
baris_hapus = df[kriteria].head(6300).index

# Menghapus baris yang memenuhi kriteria
df = df.drop(baris_hapus)

# Menyimpan data ke file CSV baru
df.to_csv('company_data(2).csv', index=False)


# Menghitung jumlah data dengan nilai "1" pada atribut tertentu
count3 = (df['Bankrupt?'] == 1).sum()
count4 = (df['Bankrupt?'] == 0).sum()

print("\n2. Setelah dibalancing ingin di prediksi")
# Menampilkan jumlah data yang memiliki nilai "1"
print("Jumlah data perusahaan bangkrut '1':", count3)
print("Jumlah data perusahaan tidak bangkrut '0':", count4)
