import requests

rq = requests.get("http://marylarodowicz.pl")
print(f"Kod odpowiedzi: {rq.status_code}")
print("\n")
print(rq.text)
