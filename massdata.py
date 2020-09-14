from pathlib import Path
import json

def main():
    p = Path("massadata.json")
    s = p.read_text(encoding="utf8")
    o = json.loads(s)
    entries_list = o.split('[')["entries"]
    totals = {}


    sumValue1 = sum(d["item"] for d in totals.values() if d)
    sumValue2 = sum(d['spec'] for d in totals.values() if d)
    sumValue3 = sum(d['total'] for d in totals.values() if d)
    total = sumValue1 + sumValue2 + sumValue3


    print(total)