import time
from selenium import webdriver
import keyboard
import os
clear = lambda: os.system('cls')

options = webdriver.ChromeOptions()
options.add_argument('headless') # 창 숨기기 옵션

driver = webdriver.Chrome('C:\stock_venvs\stock_crawling\Lib\site-packages\chromedriver',options=options)

driver.get('https://finance.naver.com/')
time.sleep(2)

find_list = ['047810','005930','068290','011000']

stock_list=[]
stock_price=[]

while True:
    if keyboard.is_pressed('f12'):
        print("pressed f12")
        time.sleep(0.2)
        driver.quit()
        break
    time.sleep(1)
    for n,i in enumerate(find_list):
        search_box = driver.find_element_by_name('query')
        search_box.send_keys(i)
        search_box.submit()
        time.sleep(0.8)
        company_name = driver.find_elements_by_xpath("//*[@id='middle']/div[1]/div[1]/h2/a")
        for j in company_name:
            if j.text not in stock_list:
                stock_list.append(j.text)

        find_price_today = driver.find_elements_by_class_name("no_up")

        price_list=[]
        price = ""

        for p in find_price_today:
            price_list.append(p.text)

        for pri in range(0, len(price_list[0]), 2):
            price += price_list[0][pri]
        if len(stock_price)!=len(find_list):
            stock_price.append(price)
        else:
            stock_price[n]=price

    clear()
    print(time.strftime('%c', time.localtime(time.time())))
    for n in range(len(find_list)):
        print(stock_list[n]," : ",stock_price[n])

    time.sleep(3)


driver.quit()