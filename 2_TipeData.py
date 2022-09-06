#fungsi dari statement type adalah mencari tipe data apa yang digunakan oleh suatu variabel
#cara penggunaan = type(nama_variabel)

#1.tipe data : angka satuan (integer)
data_integer = 1
print("Data : ", data_integer, " bertipe", type(data_integer))


#2. tipe data : angka dengan koma (koma)
data_float = 2.5
print("Data : ", data_float, " bertipe", type(data_float))

#3. tipe data : kumpulan karakter (string)
data_string = "firman"
print("Data : ", data_string, " bertipe", type(data_string))

#4. tipe data : biner true/false (bool)
data_bool = True
print("Data : ", data_bool, "true", type(data_bool))


##Tipe data khusus

#Bilangan Kompleks
data_komplex = complex(5,6)
print("Data : ", data_komplex, "true", type(data_komplex))
#menghasilkan output (5+6j) j adalah imaginer


#menggunakan type data dari bahasa C
from ctypes import c_double #import library bahasa c menggunakan statement from ctypes import c_namatipedata

data_c_double = c_double(3.14)
print("Data : ", data_c_double, "true", type(data_c_double))
