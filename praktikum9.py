#nomor 1
#celcius ke farenheit

def celcius_ke_fahreinheit(celcius):
    fahreinheit = (celcius*9/5)+32
    return fahreinheit

print(celcius_ke_fahreinheit(0))
print(celcius_ke_fahreinheit(100))


#nomor 4
#menampilkan bilangan ganjil

def bilangan(angka):
    for i in range (1,angka):
        if i % 2 != 0:
            print(i, end=", ")

bilangan(20)

#nomor 3
# fungsi untuk melihat lulus atau tidak lulus
print()
def nilai(n = 0):
    if n <= 60:
        print(f"nilai {n} tidak lulus")
    elif n > 60 and n <= 100:
        print(f"nilai {n} lulus")
    else:
        print("tidak diketahui")
nilai(70)
nilai(50)

#nomor 2
# menentukan apakah bilangan genap atau bukan

def is_genap(n):
    return n % 2== 0

print(is_genap(3))