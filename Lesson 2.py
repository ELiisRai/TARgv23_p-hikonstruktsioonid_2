
#komenurk

a=float(input("\nAlpha:"))
b=float(input("Beta:"))
c=float(input("Gamma:"))
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("See on kolmnurk")
    else:
        print("Lihtsalt nurgad")
else:
    print("Andmed ei ole õiged")



#kalkulaator
try:
    a=float(input("\nEsimene arv:"))
    try:
        b=float(input("Teine arv:"))
        t=input("Teha:")
        if t in['+','-','/','*','**','%','//']:  #''=""
            if t=='+':
                v=a+b
            elif t=='-':
                v=a-b
            elif t=='*':
                v=a*b
            elif t=='**':
                v=a**b
            elif t=='/':
                if b==0:
                    v="DIV/0"
                else:
                    v=a/b
            elif t=='%':
                v=a%b
            else:
                v=a//b
            print("{0}{1}{2}={3}".format(a,t,b,v))
        else:
            print("Tundmatu märk")
    except:
        print("Vale b arvu andmetüüp")
except:
    print("Vale a arvu andmetüüp")


# Ulesanne 1
a=input("\nMinu grupp: ")
if a=="TARgv23":
    p=int(input("Mitu pudumised sul on? : "))
    if b<15:
       h=float(input("Mis on sinu keskmine hinne? : "))
       if h>3.8:
           print("Toetus!")
       else:
            print("Liiga madal keskmine hinne. Toetust ei ole!")
    else:
        print("Toetus ei määratakse")
else:
    print("Rühm ei sobi")

# Variaant 2
g=input("\nRühma nimetus: ")
p=int(input("Mitu puudumised sul on?: "))
h=float(input("Mis on sinu keskmine hinne?: "))
if g=="TARgv23" and p<15 and h>3.8:
    print("Toetus!")
else:
    print("Toetus ei saa!")



#Ülesanne 2
k=input("\nKas sa oled poiss või tüdruk?: "). lower()
if k=="poiss" or k=="boy" or k=="p" or k=="m":
    print("Vali vaba magamiskoht esimesel korrusel")
elif k=="tüdruk" or k=="girl" or k=="t" or k=="n":
    print("Vali vaba magamiskoht teisel korrusel")
else:
    print("Lugege küsimus veel kord!")


#Võileib
s=input("\nKas tahad süüa? : "). lower()
if s=="jah" or s=="yes":
    v=int(input("1-võileib juustuga / 2-võileib vorstiga : "))
    if v in [1,2]:
        if v==1:
            print("Palun juustuga")
        else:
            print("Palun vorstiga")
    else:
        print("Vale valik!")
else:
    print("Ei taha süüa, siis ei taha")


#Ulesanded: Tingimuslik operaator IF
#1 a,b
n=input("\nKuidas sinu nimi on? : "). lower()
if n=="juku":
    print("Lähme sinuga kinosse!")
    n=int(input("Kui vana sa oled?\n"))
    if n<6:
        print("Tasuta!")
    elif n<14:
        print("Lastepilet")
    elif n<65:
        print("Taispilet")
    elif n>65:
        print("Sooduspilet")
    elif n>100:
        print("Viga andmetega")
    else:
        print("Viga andmetega")
else:
    print("Kas sa tead kus on Juku?")

#2
n1=input("\nKuidas sinu nimi on? \n")
n2=input("Ja sinu? \n")
print("Väga meeldiv,"+n1+" ja "+n2+"\nTäna te olete pinginaabrid!")

#3
a=float(input("\na="))
b=float(input("b="))
s=a*b
print("Põranda pindala : ",s)
v=input("Kas te soovite remondi teha? : ").lower()
if v=="jah" or v=="yes":
    m=float(input("Kui palju maksab ruutmeeter? : "))
    h=s*m
    print("Põranda vahetamise hind on ",h)
else:
    print("OK")

#4
a=float(input("\nAlghind : "))
if a>700:
    h=a-a*0.3
    print("Hind soodustega : ", h)
else:
    print("Sinu hind : ", a)

#5
t=float(input("\nKui palju kraadi toas?\n"))
if 18<t<32:
    print("See on soovitav toasoojus talves!")
elif t>32:
    print("See on liiga palav")
else:
    print("See on madal. Pane sooja riide selga!")

#6
p=float(input("\nKui pikk sa oled?\n"))
if p< 160:
    print("Sa oled lühike")
elif p<180:
    print("Sa oled keskmine")
else:
    print("Sa oled pikk")

#7
p=float(input("\nKui pikk sa oled?\n"))
s=input("Kas sa oled M või N?"). lower()
if p< 160:
    if s=="m":
        print("Sa oled lühike mees")
    else:
        print("Sa oled keskmine naine")
elif p<180:
    if s==m:
        print("Sa oled keskmine mees")
    else:
        print("Sa oled pikk naine")
else:
    if s==n:
        print("Sa oled väga pikk naine")
    else:
        print("Sa oled pikk mees")


#8
print("\nPiim - 1 euro, Saiake - 0.5, Leib - 2 euro")
p=input("Kas sa soovid piima? : ").lower()
s=input("Kas sa soovid saiake? : ").lower()
l=input("Kas sa soovid leiba? : ").lower()
print("Hind sulle: ")
if p=="jah" and s=="jah" and l=="jah":
    v=1+0.5+2
    print(v)
elif p=="jah" and s=="ei" and l=="jah":
    v=1+0+2
    print(v)
elif p=="jah" and s=="jah" and l=="ei":
    v=1+0.5+0
    print(v)
elif p=="ei" and s=="jah" and l=="jah":
    v=0+0.5+2
    print(v)
elif p=="ei" and s=="jah" and l=="ei":
    v=0+0.5+2
    print(v)
elif p=="ei" and s=="ei" and l=="jah":
    v=0+0+2
    print(v)
elif p=="jah" and s=="ei" and l=="ei":
    v=1+0+0
    print(v)
else:
    print("0")


#9 Ruut
print("\nSiseta küljed...")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))
if a==b==c==d:
    print("See on Ruut!")
else:
    print("See on mingi teine figuur")

#10 Matemaatika
try:
    a=float(input("\nEsimene arv:"))
    try:
        b=float(input("Teine arv:"))
        t=input("Teha:")
        if t in['+','-','/','*',]:  
            if t=='+':
                v=a+b
            elif t=='-':
                v=a-b
            elif t=='*':
                v=a*b
            elif t=='/':
                if b==0:
                    v="DIV/0"
                else:
                    v=a/b
            else:
                v=a//b
            print("{0}{1}{2}={3}".format(a,t,b,v))
        else:
            print("Tundmatu märk")
    except:
        print("Vale b arvu andmetüüp")
except:
    print("Vale a arvu andmetüüp")


#11 Juubel
s=float(input("\nMis on sinu sünnipäeva aasta?\n"))
v=2023-s
if v//5:
    print("Sel aastal sul on juubeli")
else:
    print("Sel aastal tavaline sünnipäev")

#Vaariant2
#sp=date(int(input("\nSünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: ")))
#praegu=date.today().year
#if(praegu - sp.year)%5==0:
#    print("Juubel")
#else:
#    print("Tavaline sunnipäev")


#12 Müük
h=float(input("\n Siseta toote täishind: "))
if h<10:
    print("Hind sulle - ",h-h*0.1)
else:
    print("Hind sulle - ",h-h*0.2)

#13 Jalgpalli meeskond
s=input("\nKas sa oled M või N?\n").lower()
if s=="m":
    v=float(input("Kui vana sa oled?"))
    if 16<=v<=18:
        print("Saab kandiderida")
    else:
        print("Meil on vanusepiirang")
else:
    print("Me võtame ainult poisid")

#14 Busside logistika

i=float(input("\nKui palju inimesed on vaja transporterida?\n"))
k=float(input("Kui palju kohad bussis on?\n"))
a=i//k # täis bussid
p=i-a*k # ostatok ljudei
an=a+1
print("Meil on vaja ",an," bussid")
print("Viimasel bussil on ",p," inimesi")

#Praaktikaliine töö

print("\nTere! Olen sinu sõber - Phyton!")
nimi=input("Kuidas sinu nimi on?\n")
print(nimi+", oi kui ilus nimi!")
print(nimi+"! Kas leian Sinu keha indeksi? 0-ei, 1- jah")
try:
    v=str(input("\n"))
    if v=="1":
            pikkus=float(input("Kui pikk sa oled?\n"))
            mass=float(input("Kui palju sa kaalud?\n"))
            indeks=mass/((0.01*pikkus)*(0.01*pikkus))
            print(nimi,"! Sinu keha indeks on: ", round(indeks,1))
            print("See tahendab - ")
            if indeks<16:
                print("Tervisele ohtlik alakaal	")
            elif indeks<19:
                print("Alakaal")
            elif indeks<25:
                print("Normaalkaal")
            elif indeks<30:
                print("Ülekaal")
            elif indeks<35:
                print("Rasvumine")
            elif indeks<40:
                print("Tugev rasvumine")
            else:
                print("Tervisele ohtlik rasvumine")
    else:
            print("Kahju! See on väga kasulik info!")
except: 
    print("ValueError")

print("\n")
print("Kohtumiseni, ",nimi,"! Igavesti Sinu, Phyton!")

    