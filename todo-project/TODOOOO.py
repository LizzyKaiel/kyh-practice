from pathlib import Path
import sys

def main():
    file = Path("todolist.txt")
    text = file.read_text(encoding='utf8').splitlines()
    while True:
        choice = int(input("1: Lista TODO\n2: Lägg till uppgift\n3: Ta bort uppgift\n4: Avbryt programmet\nVälj:"))
        if choice == 1:
            show_list(text)
        elif choice == 2:
            text.append(add_task())
        elif choice == 3:
            text = remove_task(text)
        elif choice == 4:
            file.write_text(save_list(text), encoding='utf8')
            sys.exit()
        else:
            print("Pucko! Ej gilltigt nummer!!!")
        print("---------------------------------")


def show_list(text):
    number = 0
    for line in text:
        number = number + 1
        print(f"{number}: {line}")

def add_task():
    return input("Skriv uppgift: ")

def remove_task(text):
    show_list(text)
    remove_number = int(input("Skriv numret på uppgiften du vill ta bort: "))
    del text[remove_number - 1]
    print(text)
    return text

def save_list(text):
    return "\n".join(text)


if __name__ == '__main__':
    main()
