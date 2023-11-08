import random
import math
"""Véletlen számok generálása 10 és 30 közötti egész szám"""

def veletlen():
    """[10,30] közötti véletlen számokat generálunk """
    i:int=0
    while i<10:
        szam: int = math.floor(random.random()*21+10)
        print(szam, end=" ")
        i+=1


#1. Generálj 5 véletlen lottó számot
#[1,90]

def elso():
    i:int=0
    lotto_szamok:int=0
    while i<5:
        lotto_szamok= math.floor(random.random()*90)
        print(lotto_szamok, end=" ")
        i+=1
    print("")


#2. Generálj 1 véletlen számot
#döntsd el róla, hogy páros vagy páratlan?
def masodik():
    veletlen_szam=math.floor(random.random()*1000)
    if veletlen_szam %2==0:
        print("A szám páros", +veletlen_szam)
    else:
        print("A szám páratlan", +veletlen_szam)
    print("")

# 3. Generálj 15 db egész számot [0,1] között.
#Hány 1-est generáltál?
def harmadik():
    i:int=0
    szamok:int=0
    egyesek:int=0
    while i<=15:
        szamok=math.floor(random.random()*2)
        print(szamok, end=" ")
        if szamok==1:
            egyesek+=1
        i+=1
    print("")
    print(f"{egyesek} db egyest generált")
    print("")


#4. Generálj egy véletlen számot 1 és 10 között!
#Szorozd meg 3-mal!
#Vonj ki belőle 15-öt
#Oszd el 6-tal
#Szorozd be 2-vel
#Vond ki belőle az eredeti számot!
#A program irja, ki hogy az eredmény egyenlő-e 5-tel?
def negyedik():
    veletlen_szam:int=math.floor(random.random()*10+1)
    osszeg:int=((((veletlen_szam*3)-15)/6)*2)-veletlen_szam
    print(veletlen_szam)
    if osszeg==5:
        print("Egyenlő 5-tel")
    else:
        print(f"Nem egyenlő 5-tel, mert a szám:{osszeg} ")

#5. Írj metodust,mely a aparaméterben kapott szövegnek kiírja a hosszát!
#Az 5. karakterét nagybetűvel
def otodik():
    szoveg:str=("Ez egy szöveg példa")


