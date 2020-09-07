def is_it_too_long(name):
    return len(name) > 5

def main():
    students = input("Skriv in name med kommatecken:").split(',')
    for name in students:
     if is_it_too_long(name):
           print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()