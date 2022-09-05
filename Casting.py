#casting adalah merubah suatu tipe data ke tipe data lain

data_int = 17
print("data = ", data_int, " bertipe ", type(data_int))

print("\n")

#proses casting

print("====INTEGER====")
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data = ", data_float, " bertipe ", type(data_float))
print("data = ", data_str, " bertipe ", type(data_str))
print("data = ", data_bool, " bertipe ", type(data_bool)) #akan bernilai False jika value = 0

print("\n")

print("=====FLOAT=====")
data_float = 17.9
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data = ", data_float, " bertipe ", type(data_int)) #nilai akan dibulatkan ke bawah
print("data = ", data_str, " bertipe ", type(data_str))
print("data = ", data_bool, " bertipe ", type(data_bool)) #akan bernilai False jika value = 0

print("\n")

print("=====BOOLEAN=====")
data_bool = True
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)

print("data = ", data_int, " bertipe ", type(data_int)) #nilai akan dibulatkan ke bawah
print("data = ", data_str, " bertipe ", type(data_str))
print("data = ", data_float, " bertipe ", type(data_float)) #akan bernilai False jika value = 0

print("\n")

print("=====STRING=====")
# KONSEP CASTING PADA STRING
# 1. ketika ingin casting string ke int dan float maka nilai dari string harus nilai angka tdk blh huruf atau kata
# 2. jika casting string ke boolean dan diisi dari nilai berapapun bahkan 0 maka akan menghasilkan = True
#    jika ingin bernilai false maka string harus dikosongkan ("")


data_str = "17"
data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)

print("data = ", data_int, " bertipe ", type(data_int)) 
print("data = ", data_float, " bertipe ", type(data_float))
print("data = ", data_bool, " bertipe ", type(data_bool))