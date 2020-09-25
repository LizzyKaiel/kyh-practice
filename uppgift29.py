import requests
import webbrowser
from pathlib import Path

r = requests.get("https://api.adviceslip.com/advice")
data = r.json()
dic = data["slip"]
value = dic['advice']

content = Path("uppgift29_template.html").read_text()
s = content.replace('QUOTE_TEXT', value)
p = Path('goat_quote.html')
p.write_text(s, encoding="utf8")

webbrowser.open('goat_quote.html')