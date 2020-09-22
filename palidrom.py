palidrom = input("Skriv in en plaidrom:").replace(" ", "")
print(f"Längden på ordet: {len(palidrom)}")

def isPalindrom(s):
    return s == s[::-1]

s = palidrom.lower()
ans = isPalindrom(s)

if ans:
    print("Detta är en palidrom")
else:
    print("Detta är inte en palindrom")