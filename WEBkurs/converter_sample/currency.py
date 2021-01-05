from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?', params={'date_req': date})
    soup = BeautifulSoup(response.content, 'lxml')
    if cur_from == 'RUR':
        cena = soup.body.valcurs.find('charcode', text=cur_to).parent.value.string.replace(',', '.')
        nominal = soup.body.valcurs.find('charcode', text=cur_to).parent.nominal.string
        itog = Decimal(float(cena) / int(nominal))
        result = Decimal(itog * int(amount))
        result = result.quantize(Decimal('.0001'))
    else:
        cena_peredavaemogo = soup.body.valcurs.find('charcode', text=cur_from).parent.value.string.replace(',', '.')
        nominal_peredavaemogo = soup.body.valcurs.find('charcode', text=cur_from).parent.nominal.string
        itog_cena = Decimal(float(cena_peredavaemogo) / int(nominal_peredavaemogo))

        cena = soup.body.valcurs.find('charcode', text=cur_to).parent.value.string.replace(',', '.')
        nominal = soup.body.valcurs.find('charcode', text=cur_to).parent.nominal.string

        itog = Decimal(float(cena) / int(nominal))

        result = Decimal((itog_cena / itog) * int(amount))
        result = result.quantize(Decimal('.0001'))
    return result


