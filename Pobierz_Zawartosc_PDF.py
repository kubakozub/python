import requests
from bs4 import BeautifulSoup
import os

url = "https://archiwum.mz.gov.pl/zdrowie-i-profilaktyka/grypa/materialy-do-pobrania/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        link = a['href']
        if link.endswith('.pdf'):
            pdf_url = link
            pdf_filename = os.path.basename(pdf_url)
            with open(pdf_filename, 'wb') as pdf_file:
                pdf_content = requests.get(pdf_url).content
                pdf_file.write(pdf_content)
                print(f"Downloaded: {pdf_filename}")
else:
    print(f"Error: {response.status_code}")
