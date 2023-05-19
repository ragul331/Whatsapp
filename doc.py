from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")


login_time = 10               
new_msg_time = 5            
send_msg_time = 3         
action_time = 2               
image_path = "C:\Ragul_P R_Resume_10-04-2023-21-06-19 (1).pdf"    #document path

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://web.whatsapp.com')
input("Press ENTER...")

with open('message.txt', 'r') as file:
    msg = file.read()

link = 'https://web.whatsapp.com'
driver.get(link)
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={num}'
        driver.get(link)
        time.sleep(new_msg_time)
        attach_btn = driver.find_element(By.CLASS_NAME, '_1OT67')
        attach_btn.click()
        time.sleep(action_time)
        msg_input = driver.find_element(By.CLASS_NAME, '_1CGek input')
        msg_input.send_keys(image_path)
        time.sleep(action_time)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)
driver.quit()