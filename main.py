
import os
import time

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

os.environ['PATH'] = r'E:/Chromedriver' # change this to your chromedriver path

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # disable logging

logo = """


  _______    _                   _ _____      _           _____ _               _             
 |__   __|  | |                 | |  __ \    (_)         / ____| |             | |            
    | | ___ | | ___ __   ___  __| | |__) | __ _  ___ ___| |    | |__   ___  ___| | _____ _ __ 
    | |/ _ \| |/ / '_ \ / _ \/ _` |  ___/ '__| |/ __/ _ \ |    | '_ \ / _ \/ __| |/ / _ \ '__|
    | | (_) |   <| |_) |  __/ (_| | |   | |  | | (_|  __/ |____| | | |  __/ (__|   <  __/ |   
    |_|\___/|_|\_\ .__/ \___|\__,_|_|   |_|  |_|\___\___|\_____|_| |_|\___|\___|_|\_\___|_|   
                 | |                                                                          
                 |_|                                                                          
                       

"""


print(logo)
productPage = input("Enter the link of the product: ")
productName = input("Enter the name of the product: ")
delay = int(input("Enter the delay between each page(in seconds): "))
loops = int(input("Enter the number of loops (8 seconds every loop): "))

while loops >= 0:
    if productName == "":
        print("Product name not entered, exiting")
        quit()
    if productPage == "":
        print("Product page not entered, exiting")
        quit()
    else:
        if productName.islower():   # if product name is lowercase, make it uppercase
            productName2 = productName.upper()
        elif productName.isupper(): # if product name is uppercase, make it lowercase (for consistency)
            productName2 = productName.lower()

        try:
            driver = webdriver.Chrome(options=options)
            driver.get(productPage)

            time.sleep(5)
        except:
            print("Error")

        html = driver.page_source
        soup = bs4.BeautifulSoup(html, 'html.parser')

        item_in_store = soup.find_all('div', class_='css-12sieg3')
        items = []

        for product in item_in_store:
            if (productName or productName2 and "https://www.tokopedia.com/" in product.text):
                items.append(product.find('a')['href'])
                items.append(product.find("div", {"class": "css-1ksb19c"}).getText())

        print("Results : ")
        print("\n")

        # print the url and price of the item
        for item in items:
            print(item)
        
        time.sleep(delay)
        loops-=1
        print("Loop starting...")
