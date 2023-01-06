import sqlite3


conn = sqlite3.connect('project.db')
cur = conn.cursor()
all = cur.execute("""SELECT * FROM universities""").fetchall()
for i in all:
    if ";" in i[1]:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (i[1].replace(';', ''), i[0]))
    if "имени" in i[1]:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (i[1].replace('имени', 'им.'), i[0]))
    if i[1].endswith(")"):
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (i[1].split(" (")[0], i[0]))
    conn.commit()
    title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0], )).fetchone()[0]
    if '"' in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.split('"')[1], i[0]))
    elif '«' in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("".join(title.split('«')[1:]).replace("»", ""), i[0]))
    conn.commit()
    title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "НИТУ МИСиС" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("(НИТУ МИСиС )", ""), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное автономное образовательное учреждение высшего образования " \
       "Первый Московский государственный медицинский университет им. И.М. Сеченова Министерства " \
       "здравоохранения РФ (Сеченовский Университет)" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Первый МГМУ им. И.М.Сеченова", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Министерства иностранных дел" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Министерства иностранных дел", "МИД"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московский государственный институт международных отношений" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Московский государственный институт международных отношений", "МГИМО"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Национальный исследовательский университет" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Национальный исследовательский университет", "НИУ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московский государственный университет" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Московский государственный университет", "МГУ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московский государственный технический университет" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Московский государственный технический университет", "МГТУ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "(национальный исследовательский университет)" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace(" (национальный исследовательский университет)", ""), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московский государственный технологический университет" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Московский государственный технологический университет", "МГТУ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Российский национальный исследовательский медицинский университет" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Российский национальный исследовательский медицинский университет", "РНИМУ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Министерства здравоохранения Российской Федерации" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace(" Министерства здравоохранения Российской Федерации", ""), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Министерства внутренних дел" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Министерства внутренних дел", "МВД"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Российский государственный университет" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Российский государственный университет", "РГУ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "(Технологии. Дизайн. Искусство)" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace(" (Технологии. Дизайн. Искусство)", ""), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Российский экономический университет" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Российский экономический университет", "РЭУ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московское высшее общевойсковое командное училище орденов Ленина и Октябрьской Революции Краснознаменное училище Министерства обороны Российской Федерации" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Общевойсковое командное училище", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Национальный исследовательский Московский государственный строительный университет" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Московский государственный строительный университет", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московский технический университет связи и информатики" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("МТУСИ", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Академия гражданской защиты Министерства Российской Федерации по делам гражданской обороны, чрезвычайным ситуациям и ликвидации последствий стихийных бедствий" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Академия гражданской обороны МЧС России", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Национальный исследовательский ядерный университет" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Национальный исследовательский ядерный университет", "НИЯУ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "        ГИТИС" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("        ГИТИС", " ГИТИС"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Российской Федерации" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Российской Федерации", "РФ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московский авиационный институт" in title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title.replace("Московский авиационный институт", "МАИ"), i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное бюджетное образовательное учреждение высшего образования Московский автомобильно-дорожный государственный технический университет (МАДИ)" == title or\
            "Московский автомобильно-дорожный государственный технический университет (МАДИ)" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("МАДИ", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Российский университет транспорта" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    (title + " (МИИТ)", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Российская академия народного хозяйства и государственной службы при Президенте РФ".lower() == title.lower():
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("РАНХиГС", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Национальный исследовательский университет Московский институт электронной техники" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("НИУ МИЭТ", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Академия Государственной противопожарной службы Министерства Российской Федерации по делам гражданской обороны, чрезвычайным ситуациям и ликвидации последствий стихийных бедствий" == title or\
            "Академия Государственной противопожарной службы Министерства РФ по делам гражданской обороны, чрезвычайным ситуациям и ликвидации последствий стихийных бедствий" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Академия ГПС МЧС", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное бюджетное учреждение науки Институт космических исследований Российской академии наук" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Институт космических исследований РАН", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное бюджетное учреждение науки Институт биоорганической химии им. академиков М.М. Шемякина и Ю.А. Овчинникова Российской академии наук" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Институт биоорганической химии", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное бюджетное учреждение науки Институт общей и неорганической химии им. Н.С. Курнакова Российской академии наук" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Ионх РАН имени Н.С.Курнакова", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Черноморское высшее военно-морское ордена Красной Звезды училище им. П.С. Нахимова Министерства обороны РФ" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Училище им. Нахимова", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное бюджетное учреждение науки Институт проблем управления им. В.А. Трапезникова Российской академии наук." == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Институт Проблем Управления им. В. А. Трапезникова РАН", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московский государственный медико-стоматологический университет им. А.И. Евдокимова Министерства здравоохранения РФ" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("МГМСУ им. А. И. Евдокимова", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Центральный научно-исследовательский испытательный институт инженерных войск Министерства обороны РФ" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("ЦНИИИ ИВ Минобороны России", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Московский пограничный институт Федеральной службы безопасности РФ" == title or\
        "Московский пограничный институт" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("МПИ ФСБ России", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Военный учебно-научный центр Сухопутных войск Общевойсковая академия Вооруженных Сил РФ" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Общевойсковая академия ВС РФ", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Военная академия Ракетных войск стратегического назначения им. Петра Великого" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("ВА РВСН им. Петра Великого", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Российский государственный аграрный университет – МСХА им. К.А. Тимирязева" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("РГАУ-МСХА им. К.А. Тимирязева", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное бюджетное учреждение науки Институт конструкторско-технологической информатики Российской академии наук" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("ИКТИ РАН", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Театральный институт им. Бориса Щукина при Государственном академическом театре им. Евгения Вахтангова" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Театральный институт им. Б. Щукина", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное бюджетное учреждение науки Институт общей физики им. А.М.Прохорова Российской академии наук" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("ИОФ РАН", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Военная академия воздушно-космической обороны им. Маршала Советского Союза Г.К. Жукова Министерства обороны РФ" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("ВА ВКО им. Г. К. Жукова", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Федеральное государственное бюджетное учреждение науки Институт мировой литературы им. А.М. Горького Российской академии наук" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("Институт мировой литературы имени А.М.Горького РАН", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Государственный университет морского и речного флота им. адмирала С.О. Макарова" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("ГУМРФ имени адмирала С.О.Макарова", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    if "Голицынский пограничный институт Федеральной службы безопасности РФ" == title:
        cur.execute("""UPDATE universities SET title = ? WHERE id = ?""",
                    ("ГПИ ФСБ России", i[0]))
        conn.commit()
        title = cur.execute("""SELECT title FROM universities WHERE id = ?""", (i[0],)).fetchone()[0]
    print(title)

conn.commit()