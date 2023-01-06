from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import time


# создание таблиц
conn = sqlite3.connect('D:\Проект, 10 класс\project\db.sqlite3')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS predprof(
   id INT PRIMARY KEY,
   title STRING,
   description TEXT);""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS sections(
   id INT PRIMARY KEY,
   title STRING,
   category STRING,
   age_category STRING,
   free BOOLEAN,
   form STRING);""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS universities(
   id INT PRIMARY KEY,
   title STRING,
   count INT,
   school_id INT);""")
conn.commit()
# добавляю необходимые столбцы в таблицу schools
# cur.execute("""ALTER TABLE schools ADD COLUMN predprof_id STRING;""")
# cur.execute("""ALTER TABLE schools ADD COLUMN universities_id STRING;""")
# cur.execute("""ALTER TABLE schools ADD COLUMN sections_id STRING;""")
# conn.commit()


# инициализация WebDriver
browser = webdriver.Chrome(executable_path="D:\\Проект, 10 класс\\db\\chromedriver.exe")

# получаю информацию о предпрофильных классах
# browser.get('https://profil.mos.ru')
# predprof = browser.find_elements(By.XPATH, 'html/body/div[2]/div[1]/div[@class="row"]')
# n = 1
# for i in predprof:
#     titles = i.find_elements(By.XPATH, ".//h2")
#     descriptions = i.find_elements(By.XPATH, ".//p")
#     for title, description in zip(titles, descriptions):
#         cur.execute("""INSERT INTO predprof(id, title, description)
#                     VALUES(?, ?, ?);""", (n, title.text.capitalize(), description.text))
#         conn.commit()
#         n += 1


web_sites = cur.execute("""SELECT id, web_site FROM schools""").fetchall()
id_university = 1727
id_sections = 117390

for i in web_sites[407:]:
    try:
        browser.get(f"https://{i[1]}")
        time.sleep(5)
        # получаю список предпрофильных классов
        predprof_menu = browser.find_elements(By.XPATH, 'html/body/div[2]/div[2]/div[6]/div[2]/div[1]/a')
        predprof_id = []
        for j in predprof_menu:
            ids = j.find_elements(By.XPATH, ".//p")[0]
            time.sleep(5)
            cur_id = cur.execute("""SELECT id FROM predprof WHERE title = ?;""",
                                 (ids.text.capitalize(), )).fetchone()
            if cur_id:
                predprof_id.append(str(cur_id[0]))
        cur.execute("""UPDATE schools SET predprof_id = ? WHERE web_site = ?;""", (", ".join(predprof_id), i[1]))
        conn.commit()
        # получаю список вузов, с которыми сотрудничает школа
        href = [j.get_attribute("href") for j in predprof_menu]
        for j in href:
            browser.get(j)
            time.sleep(5)
            path_a = browser.find_elements(By.XPATH, "//div/a[text()='Сотрудничество с вузами']")
            if path_a:
                path_div = path_a[0].find_elements(By.XPATH, "./..")[0]
                browser.execute_script("arguments[0].click();", path_a[0])
                time.sleep(5)
                for k in path_div.find_elements(By.XPATH, ".//tr")[2:]:
                    data = k.find_elements(By.XPATH, "td")
                    if len(data) >= 5:
                        count = int(data[4].text) if data[4].text else 0
                        if len(data[1].text) > 5:
                            from_db = cur.execute("""SELECT count FROM universities WHERE school_id = ? AND title = ?""",
                                                  (i[0], data[1].text)).fetchone()
                            if from_db:
                                cur.execute("""UPDATE universities SET count = ? WHERE school_id = ? AND title = ?""",
                                            (from_db[0] + count, i[0], data[1].text))
                                conn.commit()
                            else:
                                cur.execute("""INSERT INTO universities(id, title, count, school_id) VALUES(?, ?, ?, ?)""",
                                            (id_university, data[1].text, count, i[0]))
                                conn.commit()
                                id_university += 1
        university_id = cur.execute("""SELECT id FROM universities WHERE school_id = ?""", (i[0], )).fetchall()
        if university_id:
            university_id = [str(university_id[0][0]), str(university_id[-1][0])]
        cur.execute("""UPDATE schools SET universities_id = ? WHERE web_site = ?;""", (", ".join(university_id), i[1]))
        conn.commit()

        browser.get(f"https://{i[1]}/dop-obr/poisk-kruzhkov-i-sekcij")
        time.sleep(5)
        # получаю информацию о доп образовании
        sections = browser.find_elements(By.CLASS_NAME, "panel-group")[0].find_elements(By.XPATH, "div")
        sections_id = []
        for j in sections:
            browser.execute_script("arguments[0].click();", j.find_elements(By.XPATH, "div/div[1]/div/div")[0])
            time.sleep(5)
            category = j.find_elements(By.XPATH, "div/div[1]/div/div")[0].text
            for k in j.find_elements(By.XPATH, ".//tr")[1:]:
                section = k.find_elements(By.XPATH, ".//td")
                free = True if section[6].text == "Да" else False
                cur.execute("""INSERT INTO sections(id, title, category, age_category, free, form) VALUES(?, ?, ?, ?, ?, ?)""",
                            (id_sections, section[1].text, category, section[4].text, free, section[8].text))
                conn.commit()
                if not sections_id:
                    sections_id.append(str(id_sections))
                id_sections += 1

        if sections_id:
            sections_id.append(str(id_sections - 1))
        cur.execute("""UPDATE schools SET sections_id = ? WHERE web_site = ?;""", (", ".join(sections_id), i[1]))
        conn.commit()
    except Exception as e:
        print("Error:", e, "     School-website:", i[1])


browser.quit()
conn.close()