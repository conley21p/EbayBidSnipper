
'''
The Designer is not liable for any misuse of the script
'''
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
itemidurl = "https://www.ebay.com/itm/314078573362?hash=item49208ab332:g:bIUAAOSwgFdiqMyC"
maxbidebay = 10.00
increment = 1.00
lastBid = 0.00
timeleftInt = 1

'''
Navigate to sign on page and sign into your ebay account
'''
driver.get('https://www.ebay.com')

#Cange amount to sleep till you want your bot to start bidding
time.sleep(30)

while (timeleftInt > 0):
    print("**************\n\n")
    
    #if you uncomment clicking the confirm button you may be able to uncomment line below
    driver.get(itemidurl)
    
    elements = driver.find_element(By.ID, 'prcIsum_bidPrice')
    timeLeft = driver.find_element(By.ID, 'vi-cdown_timeLeft')
    print('Content:',elements.get_attribute('content'))
    print('TimeLeft:',timeLeft.text)
    if(timeLeft.text[-1] == 's'):
        # print(timeLeft.text[-3:-1])
        timeleftInt = int(timeLeft.text[-3:-1])
    elif(timeLeft.text[-4:-1] == 'min'):
        # print(timeLeft.text[-6:-4])
        timeleftInt = int(timeLeft.text[-6:-4])

    print('lastbid: ', lastBid)
    print('float(elements.get_attribute("content"):',float(elements.get_attribute('content')))

    if (lastBid < float(elements.get_attribute('content'))):
        lastBid = float(elements.get_attribute('content')) + increment
        print('bid amount:',lastBid)
        timeleftInt = int(timeLeft.text[-3:-1])
        if (lastBid <= maxbidebay):
            elements = driver.find_element(By.ID, 'MaxBidId')
            elements.send_keys(lastBid)
            elements = driver.find_element(By.ID, 'bidBtn_btn')
            elements.click()
            try:
                elements = driver.find_element(By.ID, 'confirm_button')
                # uncomment to actually buy
                # elements.click()
            except:
                print('You were out bid')
    #time.sleep(20)
    #timeleftInt = 0

time.sleep(20)
driver.quit()
