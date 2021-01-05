from django.contrib.sites import requests

r = requests.get(URL, headers=HEADERS, params=KEYWORDS3, verify=False)
soup = bs(r.content, 'html.parser')
items = soup.find_all('div', class_='col-md-12 col-lg-12 col-xs-12')

for item in items:
	td_list_of_winners.extend(
		item.find_all('td')
		)
winner_bin_to_access.append(
    td_list_of_winners[4].get_text(strip=True),
    )
q = ''.join(winner_bin_to_access)
splited = q.split()