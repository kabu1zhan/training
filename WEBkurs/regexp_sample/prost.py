import re
text = 'a123b45с6d'

def find_all_digits(text):
    exp = r'\d+'  #Тут напишите своё регулярное выражение
    return re.findall(exp, text)

a = find_all_digits(text)
print(a)