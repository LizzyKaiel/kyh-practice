from pathlib import Path
import json

def main():
    p = Path("massadata.json")
    s = p.read_text(encoding="utf8")
    o = json.loads(s)


    sumValue1 = sum(d["item"] for d in o["entries"] if d)
    sumValue2 = sum(d['spec'] for d in o["entries"] if d)
    sumValue3 = sum(d['total'] for d in o["entries"] if d)

    print(f"Total sum for items: {sumValue1}\n"
          f"Total sum for spec: {sumValue2}\n"
          f"Total sum for total: {sumValue3} ")


if __name__ == '__main__':
    main()
