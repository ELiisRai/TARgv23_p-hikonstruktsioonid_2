print("Tere tulemast!".center(50))
kool=input("\tMis koolis sa õpid?: ") #str kool
kursus=int(input("\tMis kursususel?: ")) #int kursus

# it is a comment

print("\nTere tulemast kooli "+kool.upper()+"!\nOle hea "+str(kursus)+".kursuse õpilaseks!") #kool on KOOL

print("\nTere tulemast kooli",kool.lower(),"!\nOle hea",kursus,".kursuse õpilaseks!") #kool on kool (small symbols)

print("\nTere tulemast kooli {0}!\nOle hea {1}.kursuse õpilaseks!".format(kool,kursus))

print(type(kool))
print(type(kursus))

print("\nSumma")
a1=float(input("\tArv 1: "))
a2=float(input("\tArv 2: "))
print("Vastus:", a1+a2)
print("\nSumma {0} + {1} = {2}".format(a1,a2,a1+a2))
print("Lahutamine {0} - {1} = {2}".format(a1,a2,a1-a2))
print("Korrutis {0} * {1} = {2}".format(a1,a2,a1*a2))
print("Jagamine {0} / {1} = {2}".format(a1,a2,a1/a2))
print("Astendamine {0} astmes {1} = {2}".format(a1,a2,a1**a2))
print("Jagamisjääk {0} ja {1} jääk = {2}".format(a1,a2,a1%a2))

tehe=input("\nMida teha: ")
v=eval(str(a1)+tehe+str(a2))
print(v)


# Ülesanne 1
print("\nTere, maailm!")
nimi=(input("Nimi: "))
print("Tere, maailm! Tervitav sind "+nimi)
vanus=(input("Kui vana sa oled? "))
print("Tere, maailm! Tervitav sind "+nimi+"! Sa oled "+str(vanus)+" aastat vana.")

# Ülesanne 2
vanus=str(input("\nVanus: "))
nimi=str(input("Eesnimi: "))
pikkus=float(input("Pikkus: "))
print("Kas käib koolis?")
if vanus <=str(18):
    print("Jah")
if vanus >str(18):
    print("Ei")

# Ülesanne 3
a=float(input("\nKommide arv:"))
print(str(a))
m=float(input("Mitu kommid sa soovid ära võtta? "))
print("Nüüd laual on ",a-m,"komme")

# Ülesanne 4
u=float(input("\nPuu ümbermõdu: "))
print("Puu läbimõdu: ",round(u/3.14,2))

#Vaariant 2
#c=float(input("Ümbermõõt: "))
#d=round(c/pi,2) #import math -> math.pi
#print("Läbimõõt: {0}".format(round(d,2)))

# Ülesanne 5
print("\nArvutame, kui pikk on ristikükujulise maatüki diagonaal.")
m=float(input("M mõõtme: "))
n=float(input("N mõõtme: "))
print("Maatüki diagonaal on ",round((m**2+n**2)**0.5,2),"m")

# Ülesanne 6
try:
  aeg = float(input("\nMitu tundi kulus sõiduks? "))
  teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus =round(aeg / teepikkus,2) - Oli viga :)
  kiirus=round(teepikkus/aeg,2)
  print("Sinu kiirus oli " + str(kiirus) + " km/h")
except:
    print("Andmetüübi viga!")

# Ülesanne 7
a1=float(input("\na1= "))
a2=float(input("a2= "))
a3=float(input("a3= "))
a4=float(input("a4= "))
a5=float(input("a5= "))
print("Aritmetiline keskmine: ",(a1+a2+a3+a4+a5)/5)

# Ülesanne 8
print("\t   @,,@")
print("\t   (--)")
print("\t  (\__/)")
print('\t  ^^""^^ ')

# Ülesanne 9
print("\nArvutame kolmnurga ümbermõdu.")
a=str(input("a= "))
b=str(input("b= "))
c=str(input("c= "))
p=float(a+b+c)
print("P=",p)

# Ülesanne 10
print("\nPIZZA")
print("Pizza hind - 12,90€")
p=float(12.90)
print("Jootraha - 10%")
j=float(1.29)
c=float(p+j)
v=float(input("Kui palju teid oli?"))
print("Igaüks peab maksma: ",round(c/v,2))

