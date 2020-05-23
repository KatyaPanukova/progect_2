from solution import *
import local as lc

Information.write('input.txt')

print(lc.MENU)
answer = str(input())
while answer != 6:
    if answer == lc.ONE_0:
        print(Business_Informatics())
    elif answer == lc.ONE_1:
        print(Cybernetics())
    elif answer == lc.ONE_2:
        print(Management())
    elif answer == lc.ONE_3:
        print(Sociology())
    elif answer == lc.ONE_4:
        print(Jurisprudence())
    elif answer == lc.ONE_5:
        print(Business_Informatics())
        print(Cybernetics())
        print(Management())
        print(Sociology())
        print(Jurisprudence())
    answer = str(input())
print(lc.END)
