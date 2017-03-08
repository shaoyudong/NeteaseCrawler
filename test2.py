# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo

# 建立mongo数据库
clinet = pymongo.MongoClient("localhost", 27017)
db = clinet["Netease"]

# 创建webdriver
driver = webdriver.Chrome("C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
driver.get('http://sports.163.com/17/0302/07/CEGMM8D60005877U.html')
try:
    elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'show-all-tie')]"))
    )
    print(elem.get_attribute("href"))

    commentWindow = elem.click()
    driver.switch_to.window(driver.window_handles[1])
    page = 0
    bflag = 0
    while (True):
        try:
            elem2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "下一页"))
            )
        except:
            bflag = 1
        finally:
            textElems = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[starts-with(@id,'tie-data-')]//div[@class='body']/*[@class='content' or not(@class)]"))
            )
            page = page + 1
            print("第"+ str(page) + "页" + "\n")
            for textElem in textElems:
                if (textElem.text):
                    print(textElem.text + "\n")
                    db["comments"].insert(dict({"contents": textElem.text}))
            if bflag:
                break
            if EC.element_to_be_clickable(elem2):
                elem2.click()
            time.sleep(2)
finally:
    driver.quit()

