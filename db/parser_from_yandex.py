import requests, json
import sqlite3


conn = sqlite3.connect('D:\Проект, 10 класс\project\db.sqlite3')
cur = conn.cursor()
# cur.execute("""ALTER TABLE schools ADD COLUMN rating INTEGER""")
# cur.execute("""ALTER TABLE schools ADD COLUMN reviews""")
# conn.commit()


# получение базы школ с data.mos.ru
url = "https://search-maps.yandex.ru/v1/?apikey=09717143-2884-40e6-b453-2d130e8c1d1b" \
      "&lang=ru_RU&text=ГБОУ+школа+1596&format=json"
response = requests.get(url).json()
print(response)