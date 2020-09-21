"""
1. Bygg ett program som låter användaren mata in ett reg.nr och skriv ut de två grupperna
var för sig; använd slicing-syntax för att dela upp inputsträngen.

Ex.

Ange regnr: ABC663
Bokstävsgrupp: ABC
Siffergrupp: 663

"""

reg_nr = input("Skriv reg nr:")
print(f"Regnr: {reg_nr}\nBokstävsgrupp:{reg_nr[0:3]}\nSiffergrupp:{reg_nr[3:7]} ")

"""
2. Bygg ett program där användaren matar in ett gäng heltal med komma emellan, och skriver ut följande:
    Ange tal med komma emellan: 1,2,3,5,100
    Första talet: 1
    Sista talet: 100
    Summan av talen: 111
    Talen baklänges: 100, 5, 3, 2, 1


"""

num = []

tal = input("Ange tal med komma emellan: 1,2,3,5,100: ").split(",")
back = ', '.join(list(reversed(tal)))
for i in tal:
    num.append(int(i))

print(f"Första talet:{tal[0]}\nSista talet:{tal[-1]}\nSumman av talen:{sum(num)}\nTalen baklänges: {back}")


