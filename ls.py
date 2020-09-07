def is_it_too_long(name, max_length):
    return len(name) > max_length

def main():
    try:
        max_length = int(input("Skriv in max längd på name: "))
    except ValueError:
        max_length = 5
    students = input("Skriv in name med kommatecken:").split(',')
    for name in students:
     if is_it_too_long(name, max_length):
           print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()