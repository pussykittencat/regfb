from random import seed
from random import randint
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random, subprocess, time, pyotp, os, io, selenium


#mở chrome
driver = webdriver.Chrome(r'C:\Users\ADMIN\OneDrive\Máy tính\reg\chromedriver.exe')

#đếm số dòng file mail

with open(r"C:\Users\ADMIN\OneDrive\Máy tính\reg\mail.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip() for line in f]
    for ditme in range((len(lines))):
        # mở fb
        driver.get("https://mbasic.facebook.com/reg")
        time.sleep(1)

        # điền họ
        ho = driver.find_element_by_xpath(r'//*[@id="firstname"]/div/input')
        fa = open(r'C:\Users\ADMIN\OneDrive\Máy tính\reg\ho.txt', 'r', encoding="utf-8")
        for i in fa.readlines():
            x = i.split("|")
            hoten = x[randint(0,len(x))]
        fa.close()
        ho.send_keys(hoten)

        #điền tên
        ten = driver.find_element_by_xpath(r'//*[@id="firstname"]/div/div[1]/input')
        fb = open(r'C:\Users\ADMIN\OneDrive\Máy tính\reg\ten.txt', 'r', encoding="utf-8")
        for o in fb.readlines():
            y = o.split("|")
            tenho = y[randint(0,len(y))]
        fb.close()
        ten.send_keys(tenho)


        #giới tính
        a = randint(1,3)
        if a == 1:
            for i in driver.find_elements_by_xpath(r'/html/body/div/div/div[2]/div[2]/table/tbody/tr/td/form/div[3]/div/div[2]/div/table/tbody/tr/td[2]/label/input'):
                i.click()
        elif a == 2:
            for i in driver.find_elements_by_xpath(r'/html/body/div/div/div[2]/div[2]/table/tbody/tr/td/form/div[3]/div/div[2]/div/table/tbody/tr/td[1]/label/input'):
                i.click()
        else:
            for i in driver.find_elements_by_xpath(r'/html/body/div/div/div[2]/div[2]/table/tbody/tr/td/form/div[3]/div/div[2]/div/table/tbody/tr/td[3]/label'):
                i.click()


        #ngày/tháng/năm
        def live(p,r):
            ngay = driver.find_element_by_xpath(str(p))
            chngay = Select(ngay)
            chngay.select_by_value(str(r))
        live('//*[@id="day"]', randint(2,28))
        live('//*[@id="month"]', randint(1,12))
        live('//*[@id="year"]', randint(1972,2000))

        #điền mail
        mail = driver.find_element_by_id('contactpoint_step_input')
        coun_mail = lines[ditme] 
        coun_mail = coun_mail.split('|')
        mail.send_keys(coun_mail[0])

        #điền pwd
        pwd = driver.find_element_by_id('password_step_input')
        fd = open(r"C:\Users\ADMIN\OneDrive\Máy tính\reg\pwd.txt", "r", encoding="utf-8")
        pwd.send_keys(fd.readlines())
        fd.close()

        ditme += 1
f.close()   
        
        





