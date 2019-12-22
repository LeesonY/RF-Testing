#-*- coding: utf-8 -*-
from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class UserPage:
    # 属性
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def get_user_left_money(self):
        self.driver.get('http://120.78.128.25:8765/Member/index.html')
        loc = (By.XPATH,'//li[@class="color_sub"]')
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
        money = self.driver.find_element(*loc).text
        return money














