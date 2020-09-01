def mainloop():
    import random

    n = random.randint(1, 100)
    print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilket!")

    antal_gissningar = 1

    while True:
        text = input("Din gissning: ")
        as_number = int(text)

        if as_number == n:
            print("Rätt!")
            print("Så här många gånger försökte du:", antal_gissningar)
            break

        antal_gissningar = antal_gissningar + 1
        if as_number < n:
            print("Fel! Mitt nummer är högre... Testa igen!")


        if as_number > n:
            print("Fel! Mitt nummer är lägre... Testa igen!")


mainloop()