from uppgift36.pwstrength import compute_strength

def main():
    password = input("Choose a password:")
    pw = compute_strength(password)
    print(f"Ditt lösenord får {pw} poäng!")



if __name__ == '__main__':
    main()
