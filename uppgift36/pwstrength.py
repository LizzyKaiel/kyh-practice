"""
  a) om lösenordet är mer än 10 tecken långt får det +1 poäng
  b) om lösenordet innehåller både siffror och bokstäver (det räcker med de engelska bokstäverna) så får det +1 poäng
  c) om lösenordet innehåller någon av symbolerna “#%&+_-” får det +1 poäng
  d) om lösenordet innehåller något annat tecken än bokstäver, siffror och symbolerna i (3) är det ogiltigt och får 0 poäng.
"""

def compute_strength(password):
    valid = set('#%+_-')
    score = 0

    if len(password) >= 10:
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any((c in password) for c in valid):
        score += 1

    if any(char not in valid and not char.isalnum() for char in password):
        score = 0


    return score


