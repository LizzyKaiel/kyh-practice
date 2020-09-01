def mainloop():
    def ask_number():
        text = input("Vad är din gissning?: ")
        tal = int(text)
        return tal

    import random

    n = random.randint(1, 100)
    print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilket!")

    antal_gissningar = 1

    while True:
        answer = ask_number()

        if answer == n:
            print("Rätt!")
            print("Så här många gånger försökte du:", antal_gissningar)
            break

        antal_gissningar = antal_gissningar + 1
        if answer < n:
            print("Fel! Mitt nummer är högre... Testa igen!")


        if answer > n:
            print("Fel! Mitt nummer är lägre... Testa igen!")


mainloop()