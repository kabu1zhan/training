import unittest
from bs4 import BeautifulSoup
import re

def parse(path_to_file):
    with open("{}".format(path_to_file), encoding='utf-8') as data:
        soup = BeautifulSoup(data, 'lxml')
        '1'
        imgs = len(soup.body.find(id='bodyContent').find_all("img", width=lambda x: int(x or 0) > 199))
        '2'
        header = soup.body.find(id='bodyContent').find_all(re.compile(r'[hH1-6]{2}'))
        headers = 0
        for i in header:
            i.text
            if i.text[0] in 'ETC':
                headers += 1
        '3'
        all_links = soup.body.find(id='bodyContent').find_all('a')
        linkslen = 0
        for link in all_links:
            current_count = 1
            siblings = link.find_next_siblings()
            for sibling in siblings:
                if sibling.name == 'a':
                    current_count += 1
                    linkslen = max(current_count, linkslen)
                else:
                    current_count = 0
        '4'
        lists = 0
        html_lists = soup.body.find(id='bodyContent').find_all(['ul', 'ol'])
        for html_list in html_lists:
            if not html_list.find_parents(['ul', 'ol']):
                lists += 1


    return [imgs, headers, linkslen, lists]




if __name__ == '__main__':
  a = parse('D:/wiki/Spectrogram')
  print(a)