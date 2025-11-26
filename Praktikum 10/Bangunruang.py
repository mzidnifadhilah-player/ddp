import math
def kubus(sisi):
    hasil = math.pow(sisi,3)
    return hasil

def balok(p,l,t):
    hasil = p*l*t
    return hasil

def prisma(alas,tinggi_segitiga,tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma 
    return hasil

def tabung(jari_jari,tinggi):
    alas = 22/7 * jari_jari
    hasil = alas * tinggi
    return hasil

def kerucut(v,r,j,t):
    hasil = (1/3) * math.pi * (j**2)* t
    return hasil 

print(kubus(3))
print(balok(3,3,3))
print(prisma(10,3,4))
print(tabung(8,5))
print(kerucut(10,5,2,2))