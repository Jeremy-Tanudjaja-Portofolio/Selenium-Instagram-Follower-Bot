import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium import webdriver
import selenium.common.exceptions as exceptions

class Instagram_Bot:

    def __init__(self):
        self.google_driver = "D:\Development res\Chrome Driver\chromedriver.exe"
        self.google_service = Service(self.google_driver)
        self.follower_count = 0

    def login_instagram(self):
        driver = webdriver.Chrome(self.google_driver)
        driver.get("https://www.instagram.com/")
        time.sleep(3)


        # fill username
        username = driver.find_element(By.NAME,"username")
        username.send_keys("instagram username")
        time.sleep(1)

        #fill password
        password = driver.find_element(By.NAME, "password")
        password.send_keys(r"instagram password")
        time.sleep(1)

        # Enter
        click_login = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        click_login.click()
        time.sleep(4)

        #check if login is successful
        try:
            get_error_message = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[2]/p").get_attribute("innerHTML")
            if get_error_message == "":
                return driver
            else:
                get_error_message = ""
                print("retrying login")
                self.login_instagram()
        except exceptions.NoSuchElementException:
            get_error_message = ""
            return driver


    def find_follower(self, driver):
        driver.get("https://www.instagram.com/jeremy_tanudjaja/")
        time.sleep(10)
        self.follower_count = int(driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div/span").get_attribute("innerHTML"))
        print(self.follower_count)
        time.sleep(6)

        driver.get("https://www.instagram.com/jeremy_tanudjaja/followers/")
        time.sleep(10)
        scroll_time = time.time()+60

        while scroll_time>time.time():
            try:
                scroll_down = driver.find_element(By.CLASS_NAME, r"_aanq").click()
                driver.execute_script(f"arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down)
                time.sleep(4)
            except exceptions.ElementNotInteractableException:
                print("element not interactable")
            except exceptions.WebDriverException:
                print("")
        return driver

    def follow_all(self, driver):
        print("its follow time")
        for i in range(1, 20):
            try:
                # /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]
                # /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[3]/button
                # /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]
                # /html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button
                follow = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[{i}]/div[3]/button")
                follow.click()
                time.sleep(1)
                print(f"follow {i}")
            except exceptions.ElementClickInterceptedException:
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]").click()
                time.sleep(1)