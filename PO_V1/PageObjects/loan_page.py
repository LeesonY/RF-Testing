#-*- coding: utf-8 -*-
from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class LoanPage:
    # 属性
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def find_element_wait(self,locator) -> WebElement:
        wait = WebDriverWait(self.driver,20)
        ele = wait.until(EC.visibility_of_element_located((By.XPATH,locator)))
        return ele


    def BidLoan(self):
        '''投标'''
        #进入投标页面
        self.find_element_wait()














