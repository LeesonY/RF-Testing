#-*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class IndexPage:

    def __init__(self,driver):
        self.driver = driver

    #检测昵称是否存在
    def check_nick_name_exists(self):
        '''

        :return: 存在返回true，不存在返回false
        '''
        WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH,'//a[text()="关于我们"]')))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
            return True
        except:
            return False


    #点击投标按钮
    def click_invest_button(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="抢投标"][1]')))
        self.driver.find_element_by_xpath('//a[text()="抢投标"][1]').click()






