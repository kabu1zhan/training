import requests
from decimal import Decimal
from bs4 import BeautifulSoup
cur_from = 'KZT'
cur_to = 'USD'
date = '27/04/2020'
ammount = Decimal("1000.1000")
response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?', params={'date_req': date})
soup = BeautifulSoup(response.text, 'lxml')

cena_peredavaemogo = soup.body.valcurs.find('charcode', text=cur_from).parent.value.string.replace(',', '.')
nominal_peredavaemogo = soup.body.valcurs.find('charcode', text=cur_from).parent.nominal.string
itog_cena = Decimal(float(cena_peredavaemogo)/int(nominal_peredavaemogo))

cena = soup.body.valcurs.find('charcode', text=cur_to).parent.value.string.replace(',', '.')
nominal = soup.body.valcurs.find('charcode', text=cur_to).parent.nominal.string

itog = Decimal(float(cena)/int(nominal))

end = Decimal((itog_cena/itog)*int(ammount))
print(end.quantize(Decimal('.0001')))
