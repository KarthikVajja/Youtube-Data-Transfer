from lib2to3.pgen2 import driver
import undetected_chromedriver as uc
import time
import pandas
import numpy as np

driver = uc.Chrome(executable_path='<path to your driver>')

#Login
try:
    driver.get(r'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en-GB&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    driver.implicitly_wait(15)
  
    loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    print('Enter email:', end=' ')
    email = input()
  
    nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    nextButton[0].click()
  
    passWordBox = driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    print('Enter password:', end=' ')
    password = input()
  
    nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()
  
    print('Login Successful...!!')
    time.sleep(5)
except:
    print('Login Failed')

df = pandas.read_csv('~/Desktop/takeout-20220114T162156Z-001/Takeout/YouTube and YouTube Music/subscriptions/subscriptions.csv')
subs = np.array(df['Channel URL'])
print(subs)

for i in subs:
    driver.get(i)
    sub_button = driver.find_element_by_xpath('//*[@id="subscribe-button"]')
    sub_button.click()
    pref_button = driver.find_element_by_xpath('//*[@id="notification-preference-button"]')
    pref_button.click()
    all_pref = driver.find_element_by_xpath('//*[@id="items"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')
    all_pref.click()

# In case of unstable internet connection