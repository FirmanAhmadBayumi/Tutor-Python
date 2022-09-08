#prioritas dalam opearsi aritmatika
# 1. () angka di dalam kurung
# 2. ** eksponen atau pangkat
# 3. * , / , % , // (perkalian, pembagian, modulus, floor division)
# 4. + , - ()

bil1 = 10
bil2 = 4

# penjumlahan +
res = bil1 + bil2
print("Hasil: ", res)

# pengurangan -
res = bil1 - bil2
print("Hasil: ", res)

# perkalian *
res = bil1 * bil2
print("Hasil: ", res)

# pembagian / 
res = bil1 / bil2
print("Hasil: ", res)

# modulus %
res = bil1 % bil2
print("Hasil: ", res)

# floor division //
res = bil1 // bil2
print("Hasil: ", res) #hasil yang koma akan dibulatkan ke bawah

# operational precedence
x = 2
y = 4
z = 3

res = x ** y * z + x / y - y % z // x
print("Hasil: ", res)
