from lib2to3.pgen2 import driver
import undetected_chromedriver as uc
import time

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

#Links to videos
driver.get('<path to your history html file>')
arr = []
time.sleep(50)
elems = driver.find_elements_by_tag_name('a')
for elem in elems:
    href = elem.get_attribute('href')
    if href is not None:
        if "https://www.youtube.com/watch" in href:     # Only include video links
            arr.append(href)
            print(href)
    if len(arr)>1000:                                   #Number of most recent links to be included
        break
print("Array generated")

#Visiting links
for i in reversed(arr):
    driver.get(i)
    time.sleep(15)                                      #Time to stay in each link

#In case of uncertain internet connection
# for i in range (len(arr)-1,-1,-1):
#     try:
#         driver.get(arr[i])
#         driver.find_element_by_xpath('//*[@id="img"]')
#     except:
#         print('failed loading site' + arr[i] + '\nAttempting again.....', end='\n\n')
#         i-=1