
__author__ = "Hamed Moradi"
__email__ = "hamdmrady63@gmail.com"

# checking if all modules are loaded correctly
try:
    import pickle # this is for saving cookies
    import sys # sys module 
    import os # os module 
    from bs4 import BeautifulSoup # for parsing and scraping in case needed
    from selenium import webdriver # webdriver
    from selenium.webdriver import Chrome # chrome 
    from selenium.webdriver.common.keys import Keys # keys
    from selenium.webdriver.common.by import By # by
    from selenium.webdriver.support.ui import WebDriverWait # webdriverwait
    from selenium.webdriver.support import expected_conditions # expected conditions
    from selenium.common.exceptions import TimeoutException # time out exception
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC # options
    import time # time module 
    import re
    import pyautogui as pygui
    print("all modules are loaded!")
except Exception as e:
    print("Error ->>>: {}".format(e))
class SooqAutomation:
    def driver(self):
        self.options = Options()
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
        self.options.add_argument("--window-size(400,400)")
        driver = driver = webdriver.Chrome(executable_path=r"chromedriver.exe",options=self.options)
        # In case if cookies doesn't work anymore you can uncomment this part and refreash the cookies!
        '''driver.get("https://ma.opensooq.com/")
        change = str(input("did you change it\n \n").strip().lower())
        if change == 'yes':
            print("saving cookies!")
            pickle.dump(driver.get_cookies(),open("cookies.pkl",'wb'))'''
        driver.get("https://ma.opensooq.com/")
        cookies = pickle.load(open("cookies.pkl",'rb'))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://sa.opensooq.com/en/find?page=100000")
        last_page = int(driver.find_element(By.XPATH,'//*[@id="listingLeft"]/ul/li[12]/a').text)
        print(last_page)
        for ii in range(1,last_page+1):
            y = 200
            driver.get(f"https://sa.opensooq.com/en/find?page={ii}")
            for i in range(1,31):
                print(i)
                driver.execute_script(f"window.scrollTo(0, {int(y)});")
                time.sleep(1)
                driver.find_element(By.XPATH,f'//*[@id="gridPostListing"]/li[{i}]/div/div[4]/object/div[2]').click()
                bs_obj = BeautifulSoup(driver.page_source,features='html.parser')
                id_for_xpath = bs_obj.findAll("label",{"class":re.compile('block icon-clip font-24')})[1]['for'][7:-8]
                print(id_for_xpath)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="{id_for_xpath}"]/div[2]/div[6]/div[2]/ul/li[5]/button/span')))
                pygui.write("Hello How are you doing today?")
                send_button = driver.find_element(By.XPATH,f'//*[@id="{id_for_xpath}"]/div[2]/div[6]/div[2]/ul/li[5]/button/span').click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="{id_for_xpath}"]/div[1]/div[3]/a[3]')))
                time.sleep(1)
                close_button = driver.find_element(By.XPATH,f'//*[@id="{id_for_xpath}"]/div[1]/div[3]/a[3]').click()
                time.sleep(1)
                y = y + 200
                print(y)
    def run(self):
        self.driver()

if __name__ == "__main__":
    bot = SooqAutomation()
    bot.run()

