from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/username/.config/google-chrome")

driver = webdriver.Chrome(options=options)  

image_path="C:\img.jpeg"

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
        time.sleep(8)
        actions = ActionChains(driver)
        attach_btn= driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div')
        attach_btn.click()
        image_btn= driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
        image_btn.send_keys(image_path)
        time.sleep(2)
        for line in msg.split('\n'):
            actions.send_keys(line)
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(5)
driver.quit()
