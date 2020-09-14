from pathlib import Path
import json

def main():
    p = Path("massadata.json")
    s = p.read_text(encoding="utf8")
    o = json.loads(s)

    sumValue1 = sum(d["item"] for d in o["entries"] if d)
    sumValue2 = sum(d['spec'] for d in o["entries"] if d)
    sumValue3 = sum(d['total'] for d in o["entries"] if d)
    total = sumValue1 + sumValue2 + sumValue3

    print(f"Total sum for items: {sumValue1}\nTotal sum for spec: {sumValue2}\nTotal sum for total: {sumValue3} ")
    print(f"Everything in total: {total}")

if __name__ == '__main__':
    main()
