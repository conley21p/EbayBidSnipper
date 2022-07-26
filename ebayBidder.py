from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

'''
item id url: the url of the item
max bid ebay: is the Max dollar amount you want to bid
increment amount: how much more you want to bid than current bid in dollars
'''
itemidurl = "https://www.ebay.com/itm/314077757413?hash=item49207e3fe5%3Ag%3A9ioAAOSwW61inrhl&LH_Auction=1"
maxbidebay = 2.00
increment = 1.00
lastBid = 0.00
timeleftInt = 1

'''
Navigate to sign on page and sign into your ebay account
'''
driver.get('https://www.ebay.com')
time.sleep(20)

while (timeleftInt > 0):
    driver.get(itemidurl)
    elements = driver.find_element(By.ID, 'prcIsum_bidPrice')
    timeLeft = driver.find_element(By.ID, 'vi-cdown_timeLeft')
#     print('Content:',elements.get_attribute('content'))
#     print('TimeLeft:',timeLeft.text)
#     print(timeLeft.text[-3:-1])
    if (lastBid < float(elements.get_attribute('content'))):
        lastBid = float(elements.get_attribute('content')) + increment
#         print(lastBid)
        timeleftInt = int(timeLeft.text[-3:-1])
        elements = driver.find_element(By.ID, 'MaxBidId')
        elements.send_keys(lastBid)
        elements = driver.find_element(By.ID, 'bidBtn_btn')
        # elements.click()
        elements = driver.find_element(By.ID, 'confirm_button')
        # elements.click()
    #Uncomment line below if you want to test
    #timeleftInt = 0

time.sleep(20)
driver.quit()
