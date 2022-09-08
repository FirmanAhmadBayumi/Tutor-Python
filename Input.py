"""
  dalam bahasa pemrograman python ini ketika kita menginput sesuatu maka,
  input tersebut secara default adalah bertipe string. Jika ingin merubah
  inputan sesuai dengan tipe data yang kita inginkan maka harus kita casting terlebih
  dahulu dengan cara nama_variabel = type_data(input)(args)
"""

data = input("Type something : ")
print("Your data is", data, "with type", type(data))

#statement dibawah input yang diterima adalah bertipe integer
num1 = int(input("Type number decimal : "))

#statement dibawah input yang diterima adalah bertipe real/float
num2 = float(input("Type number floating : "))

print("Your number is", num1)
print("Your number is", num2)

"""
  jika kita ingin membuat/merubah suatu argumen ke tipe boolean,
  yang harus kita lakukan adalah dengan cara mengcasting terlebih
  dahulu ke tipe data integer, seperti contoh dibawah ini :
"""
