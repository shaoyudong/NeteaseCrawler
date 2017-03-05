# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
driver.get('http://sports.163.com/17/0302/07/CEGMM8D60005877U.html')
try:
    elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'post_cnum_tie')]"))
    )
    print(elem.get_attribute("href"))

    commentWindow = elem.click()
    driver.switch_to.window(driver.window_handles[1])
    page = 0
    while (EC.element_to_be_clickable((By.LINK_TEXT,"下一页"))):
        elem2 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "下一页"))
        )
        textElems = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[starts-with(@id,'tie-data-')]//div[@class='body']/*[@class='content' or not(@class)]"))
        )
        page = page + 1
        print("第"+ str(page) + "页" + "\n")
        for textElem in textElems:
            if (textElem.text):
                print(textElem.text + "\n")
        elem2.click()


finally:
    driver.quit()
# elem = driver.find_element_by_xpath("//a[contains(@class, 'post_cnum_tie')]")
# print(elem.get_attribute("href"))
# print(elem.get_attribute("target"))
# commentWindow = elem.click()
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element_by_link_text("下一页").click()
# textelems = driver.find_elements_by_xpath("//div[starts-with(@id,'tie-data-')]//div[@class='body']/*[@class='content' or not(@class)]")
# print(textelems)
# for textelem in textelems:
#     if (textelem.text):
#         print(textelem.text + "\n")
