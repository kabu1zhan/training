import requests
token = '27aad3e627aad3e627aad3e63927dbef19227aa27aad3e67937e77ce9e7eff37920c96c'
version = '5.71'
username = 'kabiljan'

id = requests.get('https://api.vk.com/method/users.get',
                    params={
                        'user_ids': username,
                        'access_token': token,
                        'v': version
                    }
                        )
data_id = id.json()['response'][0]['id']

Poluchit_Spisok_Druzei = requests.get('https://api.vk.com/method/friends.get',
                    params={
                        'user_id': data_id,
                        'fields': 'bdate',
                        'access_token': token,
                        'v': version
                    })
data_druzia = Poluchit_Spisok_Druzei.json()['response']['items']
friends = dict()
for i in data_druzia:
    if 'bdate' in i.keys():
        i_date = i['bdate'].split('.')
        if len(i_date) == 3:
            bdate_year = int(i_date[2])
            friend_age = 2020 - bdate_year
            if friend_age not in friends:
                friends[friend_age] = 0

            friends[friend_age] += 1
friends_list = sorted(friends.items(), key=lambda el: (-el[1], el[0]))


print(data_druzia)
