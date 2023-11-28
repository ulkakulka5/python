f=open("in.txt","r")


while True:
    print("odszyfrowac czy zaszyfrowac?(o/z): ")
    odp=input()
    if odp=="o" or odp=="O":
        odp = "o"
        break
    elif odp=="z" or odp=="Z":
        odp = "z"
        break
    
alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

klucz=int(input("podaj szyfr(l.calkowita): "))
klucz %= 26
tekst=f.readline()
wynik=""


if odp=="o":
    for l in tekst:
        index= alfabet.find(l)-klucz
        index%52
        wynik= wynik+alfabet[index]

elif odp=="z":
    for l in tekst:
        index = alfabet.find(l) + klucz
        index %= 52
        wynik= wynik+alfabet[index]
        
f.close()

g=open("out.txt","a")
g.write(wynik)
g.close()




