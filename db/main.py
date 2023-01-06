import requests
import sqlite3


# получение базы школ с data.mos.ru
url = "https://apidata.mos.ru/v1/datasets/2263/rows?$filter=Cells/OrgTypeeqобщеобразовательная&api_key=75ab750063735238359b560dadce5698"
params = {"Id": 2263, "VersionNumber": 4.10}
response = requests.get(url, params=params).json()

# создание таблиц schools и addresses
conn = sqlite3.connect('project.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS schools(
   id INT PRIMARY KEY,
   short_name STRING,
   full_name STRING,
   educational_services STRING,
   institutions_addresses STRING,
   legal_organization STRING,
   chief_name STRING,
   public_phone STRING,
   email STRING,
   web_site STRING);""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS addresses(
   id INT PRIMARY KEY,
   adm_area STRING,
   district STRING,
   address STRING,
   public_phone STRING,
   available_k STRING,
   available_o STRING,
   available_z STRING,
   available_s STRING);
""")
conn.commit()

n = 1
translate = {"FullTimeEdu": "очная форма обучения", "PartTimeEdu": "заочная форма обучения",
             "FullPartTimeEdu": "очно-заочная форма обучения", "ExternalEdu": "самообразование",
             "InFamilyEdu": "семейное обучение", "HasPreschoolEdu": "дошкольное образование"}

# обработка данных и загрузка в базу данных
for i in range(len(response)):
    addresses = []
    for j in response[i]["Cells"]['InstitutionsAddresses']:
        a = {}
        a["AdmArea"] = j["AdmArea"]
        a['District'] = j['District']
        a['Address'] = j['Address']
        a['PublicPhone'] = ", ".join([x['PublicPhone'] for x in j['PublicPhone']])
        a['available_k'] = j['Availability'][0]['available_k']
        a['available_o'] = j['Availability'][0]['available_o']
        a['available_z'] = j['Availability'][0]['available_z']
        a['available_s'] = j['Availability'][0]['available_s']
        addresses.append(a)
    if response[i]["Cells"]['EducationalServices']:
        forms = ", ".join(list(map(lambda x: translate[x],
                                   list(filter(lambda x: response[i]["Cells"]['EducationalServices'][0][x] == "да",
                                               response[i]["Cells"]['EducationalServices'][0].keys())))))
    else:
        forms = "-"
    school = (i + 1, response[i]["Cells"]["ShortName"], response[i]["Cells"]["FullName"], forms,
              ", ".join([str(x) for x in range(n, n + len(addresses) + 1)]),
              response[i]["Cells"]['LegalOrganization'], response[i]["Cells"]['ChiefName'],
              response[i]["Cells"]['PublicPhone'][0]['PublicPhone'], response[i]["Cells"]['Email'][0]["Email"],
              response[i]["Cells"]['WebSite'])
    cur.execute("""INSERT INTO 
        schools(id, short_name, full_name, educational_services, institutions_addresses, legal_organization,
        chief_name, public_phone, email, web_site) 
           VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", school)
    conn.commit()
    for j in range(len(addresses)):
        a = (n + j, addresses[j]["AdmArea"], addresses[j]["District"], addresses[j]["Address"],
             addresses[j]['PublicPhone'], addresses[j]['available_k'],
             addresses[j]['available_o'], addresses[j]['available_z'], addresses[j]['available_s'])
        cur.execute("""INSERT INTO 
                addresses(id, adm_area, district, address, public_phone, available_k,
                available_o, available_z, available_s) 
                   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);""", a)
        conn.commit()
    n += len(addresses) + 1
conn.close()