print("program penentu bilangan terbesar")
print("===================================")

print ("masukan nilai yang di inginkan")

X= int(input("masukan bilangan pertama:"))
Y= int(input("masukan bilanagn kedua  :"))
Z= int(input("masukan bilangan ketiga :"))
if X > Y and Y > Z:
    Print (X, "Terbesar dari 3 bilangan yang di input")
elif Y > X and Y > Z:
    Print(Y, "Terbesar dari 3 bilangan yang di input")
else:
    print(Z, "Terbesar dari 3 bilangan yang di input")
