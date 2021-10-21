from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import requests, os, time
from dotenv import load_dotenv

def goto(URL,driver):
    driver.get(URL)

def antibotcookie(driver):
    driver.execute_script("document.querySelector('#usercentrics-root').shadowRoot.querySelector('section[data-testid]').querySelector('div').querySelector('div[data-testid]').querySelector('div[aria-label=\"Footer including buttons\"]').querySelector('div').querySelector('div').querySelector('div').querySelector('button[aria-label=\"Accept All\"]').click()")

def normalcookie(driver):
    pass

def check_URL(URL, gpuName):
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome('./chromedriver',chrome_options=options)

    goto(URL, driver)

    time.sleep(1)
    try:
        antibotcookie(driver)
    except:
        normalcookie(driver)


    try:
        result = driver.execute_script('''
    result = document.contains(document.querySelector('div[class=\"grid-y align-center error-box__text-wrapper\"]'));
    return result;
    ''')

        
        if result == True:

            print('Running, no result found!')
        else :
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            log = f"[{current_time}] : {gpuName}s are available at {URL}! \n"

            with open('log.txt', 'a') as writer:
                writer.write(log)

            url = os.environ.get("DISCORD_URL")
            requests.post(url,data = {'content': log})
            

    except Exception as e:
        print(e)

    driver.close()


load_dotenv()
while True:
    check_URL('https://m.notebooksbilliger.de/nvidia+geforce+rtx+3080+founders+edition+686455','3080')
    check_URL('https://m.notebooksbilliger.de/nvidia+geforce+rtx+3060+ti+founders+edition+720601','3060TI')
    check_URL('https://m.notebooksbilliger.de/nvidia+geforce+rtx+3080+ti+founders+edition+719852','3080TI')
    check_URL('https://m.notebooksbilliger.de/nvidia+geforce+rtx+3070+founders+edition+692950','3070')
    check_URL('https://m.notebooksbilliger.de/nvidia+geforce+rtx+3070+ti+founders+edition+jiu+725375','3070TI')
    time.sleep(5)