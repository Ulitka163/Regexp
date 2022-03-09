from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
contacts_list_new = []

for i in contacts_list:
  entry = ','.join(i[0:3])
  pattern = r"^(\w+)[,\s]?(\w+)(,|\s)?(\w+)?,?,?"
  true_name = re.sub(pattern, r"\1,\2,\4", entry)
  result = true_name.split(',') + i[3:]

  for b in contacts_list_new[1:]:
    if result[0:2] == b[0:2]:
      for a in range(len(b)):
        if b[a] == '':
          b[a] = result[a]
      break
  else:
    contacts_list_new.append(result)

phonebook = []

for i in contacts_list_new:
  entry = ','.join(i)
  pattern = r"(\+7|8)?\s?\(?(\d{3})\)?(-|\s)?(\d{3})-?(\d{2})-?(\d{2})\s?\(?(доб.)?\s?(\d{4})?\)?"
  true_phone = re.sub(pattern, r"+7(\2)\4-\5-\6 \7\8", entry)
  true_list = true_phone.split(',')
  phonebook.append(true_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
 datawriter = csv.writer(f, delimiter=',', lineterminator='\n')
 # Вместо contacts_list подставьте свой список
 datawriter.writerows(phonebook)