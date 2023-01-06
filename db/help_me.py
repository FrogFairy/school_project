from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome(executable_path="D:\\Проект, 10 класс\\db\\chromedriver.exe")
browser.get(f"https://sch2091.mskobr.ru/predprof/med-class/project-metrics")

path_a = browser.find_elements(By.XPATH, "//div/a[contains(text(), 'Сотрудничество с вузами')]")
path_div = path_a[0].find_elements(By.XPATH, "./..")[0]
browser.execute_script("arguments[0].click();", path_a[0])
for k in path_div.find_elements(By.XPATH, ".//tr")[2:]:
    data = k.find_elements(By.XPATH, "td")
    print(data)