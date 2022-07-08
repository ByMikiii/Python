# 1.hod kockou + vykreslit kocku

dice = '+---------+\n' \
       '| {}  {}  {} |\n' \
       '| {}  {}  {} |\n' \
       '| {}  {}  {} |\n' \
       '+---------+'
diceModels = ['', dice.format(' ',' ',' ',' ','O',' ',' ',' ',' '), dice.format(' ',' ','O',' ',' ',' ','O',' ',' '), dice.format(' ',' ','O',' ','O',' ','O',' ',' '),
              dice.format('O',' ','O',' ',' ',' ','O',' ','O'), dice.format('O',' ','O',' ','O',' ','O',' ','O'), dice.format('O',' ','O','O',' ','O','O',' ','O') ]

import random
diceNum = random.randint(1,6)
print('Na kocke padlo: ')
print(diceModels[diceNum]+'\n')



# 2.Opýtaj sa používateľa na číslo a prekonvertuj toto číslo na binárne. Výpis zarovnaj na 32 bitové binárne číslo.

number = int(input('Zadaj cislo ktore chces prekonvertovat na binarne: '))
binaryNumber = "{0:b}".format(number)
print("Cislo v binarnej forme: "+"{:0>32}".format(binaryNumber)+'\n')



# 3.Vypíš čísla do tabulky od 0 po 15 v decimálnej, binarnej, octálnej a hexadecimálnej forme.

width = 51

tableHeader = '+{:-^{width}}+'.format('Tabuľka číselných sústav',width = width) +'\n' \
        '|{: ^{width}}|'.format('{: ^{width}}|'.format('dec',width=width/4)+'{: ^{width}}|'.format('bin',width=width/4)+'{: ^{width}}|'.format('oct',width=width/4)+'{: ^{width}}'.format('hex',width=width/4), width = width) +'\n' \
        '+{:-^{width}}+'.format('',width = width)


print(tableHeader)
for i in range(16):
      print( '|{: ^{width}}|'.format('{: ^{width}}|'.format(str(i),width=width/4)+'{:^{width}}|'.format("{0:#b}".format(i),width=width/4)+'{: ^{width}}|'.format("{0:#o}".format(i),width=width/4)+'{: ^{width}}'.format("{0:#X}".format(i),width=width/4), width = width))

print('+{:-^{width}}+'.format('',width = width))
