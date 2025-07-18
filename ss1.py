# from selenium.webdriver import Chrome
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# driver=Chrome()
# url='https://www.python.org/'
# driver.get(url)
# WebDriverWait(driver,10).until(lambda d:"Python" in d.title)
# print(driver.find_element(By.XPATH,'//*[@id="touchnav-wrapper"]/header/div/div[3]').text)

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains
driver=Chrome()
driver.get("https://www.baidu.com/")
driver.find_element(By.XPATH,'//*[@name="wd"]').send_keys("python")
driver.find_element(By.XPATH,'//*[@id="su"]').click()
WebDriverWait(driver,10).until(title_contains("python"))#条件语句
while True:
  h3list=driver.find_elements(By.CSS_SELECTOR,'h3.t')
  for i in h3list:
      print(i.text)
  driver.find_element(By.XPATH,'//*[@id="page"]/div/a[last()]').click()#last()下一页
  time.sleep(1.5)
input() #防止闪退(如果想停留在浏览器页面)  

# import time,os,pandas
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# os.chdir(r'D:\py_first\20250715-200228\oooo')
# db=pandas.read_excel('student.xlsx',engine='openpyxl')
# driver=Chrome()
# url='http://antpython.net/webspider/grade_form'
# for idx,row in db.iterrows():
#     name=row['姓名']
#     语文=row['语文成绩']
#     数学=row['数学成绩']
#     英语=row['英语成绩']
#     driver.get(url)
#     WebDriverWait(driver,5).until(lambda d:"已提交数据" in d.page_source)
#     time.sleep(1)
#     driver.find_element(By.XPATH,'//*[@id="sname"]').send_keys(name)
#     time.sleep(1)
#     driver.find_element(By.XPATH,'//*[@id="yuwen"]').send_keys(语文)
#     time.sleep(1)
#     driver.find_element(By.XPATH,'//*[@id="shxue"]').send_keys(数学)
#     time.sleep(1)
#     driver.find_element(By.XPATH,'//*[@id="yingyu"]').send_keys(英语)
#     time.sleep(1)
#     driver.find_element(By.XPATH,'//*[@id="submit_button"]').click()
#     time.sleep(1)
#     print(name,语文,数学,英语)
#     WebDriverWait(driver,5).until(lambda d:"提交成功!" in d.page_source)
# #driver.close()
# x=input()


