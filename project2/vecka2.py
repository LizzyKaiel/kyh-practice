"""

Feedback från användare av programmet:
 - Det behövs fler frågor!
 - Vi vill ha poäng!

Feedback från kollegor:
 - Vi vill ha lite mer ordning och reda i program - det är massa dubbel kod!
  Kan vi använda listor, dictionaries och/eller funktioner för att minska upprepningar i koden?
 - Det känns dumt att hårdkoda frågorna/svaren i koden! Kan vi lagra dem i en (eller flera) separata textfiler
  (listor eller json eller vad ni vill som passar) som vi läser in när programmet startar?

Exempelkörning:

```
Vilken funktion används för att skriva ut saker på skärmen?
print
Rätt!
Hur tar man fram längden på listan i variabeln "fruits"?
len
Fel! Rätt svar är: len(fruits)
Vad heter nyckelordet för att göra en loop i Python?
Ditt svar:   for
Fel! Rätt svar är: for
RESULTAT.
Du fick 1 poäng av 3 möjliga.
```
Observera att användaren råkade trycka mellanslag när hen svarade "
 for"; det är därför det blev fel trots att det var rätt svar så att säga!

"""

from pathlib import Path


def main():
    file = Path("q_and_a.txt")
    text = file.read_text(encoding='utf8').splitlines()
    qa_dictionary = {}

    def q_a(new_line):
        q, a = new_line.split(':')
        qa_dictionary[q] = a.replace('\n', '')

    def inititiate_questions():
        for line in text:
            q_a(line)

    def run():
        score = 0
        for q, a in qa_dictionary.items():
            player_answer = input('Question ' + q)
            if player_answer.lower() == a.lower():
                score += 1
        print(f"You got {score}☆ out of {(len(qa_dictionary))}☆")
    inititiate_questions()
    run()

if __name__ == '__main__':
    main()

