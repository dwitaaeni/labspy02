print ("Program Mencari Bilangan Terbesar")
print ("---------------------------------")

a = int (input("Masukan Bilangan A : "))
b = int (input("Masukan Bilangan B : "))
c = int (input("Masukan Bilangan C : "))

print ()

if a > b and a > c :
    print("Bilangan Terbesar Adalah : A")
elif b > c and b > a:
    print("Bilangan Terbesar Adalah : B")
else :
    print("Bilangan Terbesar Adalah : C")
