
# 1.Najvyssie cislo
print(1e+308)



# 2.Vypocet prepony
a = float(input('Zadaj odvesnu a: '))
b = float(input('Zadaj odvesnu b: '))

c = round((a**2 + b**2)**(1/2), 1)

print('Prepona sa rovna: ',c)



#Opýtaj sa používateľa na nejaké veľké číslo. Vypíš posledné 3 cifry z tohto čísla
number = int(input('Zadaj lubovolne velke cislo: '))
lastNumbers = []

lastNumbers.append(number%10)
number /= 10

lastNumbers.append(int(number)%10)
number /= 10

lastNumbers.append(int(number)%10)

print("posledne cisla su: ",*reversed(lastNumbers))




# 3.hod kockou
import random
diceNumber = random.randint(1,6)
print('Na kocke padlo: ',diceNumber)



# 4.Sprav program, ktorý sa používateľa opýta sériu otázok a potom vypíše všetky údaj
from datetime import datetime
now = datetime.now()

currentYear = int(now.strftime("%Y"))

name = input('Zadajte vase meno: ')
address = input('Zadajte vasu adresu: ')
yearOfBirth = int(input('Zadajte rok vasho narodenia: '))
spacer = '-'*15

age = currentYear - yearOfBirth

print(spacer)
print('Meno: ', name)
print('Adresa: ', address)
print('Vek: ', age)
print(spacer)
