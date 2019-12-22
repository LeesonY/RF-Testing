#-*- coding: utf-8 -*-
from selenium import webdriver
from PO_V1.PageObjects.login_page import LoginPage
from PO_V1.PageObjects.index_page import IndexPage
from PO_V1.TestDatas import Comon_Datas as cd
from PO_V1.TestDatas import login_datas as ld
from ddt import ddt,data
import unittest

#用例三部曲：前置、步骤、断言
@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #前置 - 打开网页
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("{}/Index/login.html".format(cd.base_url))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        #刷新当前页面
        self.driver.refresh()


    #正常用例 登录+首页
    def test_login_2_success(self):
        #步骤 - 登录操作 - 登录页面 18684720553、pyhton
        LoginPage(self.driver).login(ld.success_data["user"], ld.success_data["passwd"])
        #断言 - 页面是否存在  我的账户  元素 元素定位+元素操作
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        # url跳转
        self.assertEqual(self.driver.current_url,ld.success_data["check"])

    # 异常用例 - ...
    @data(*ld.wrong_datas)
    def test_login_0_failed_by_wrong_datas(self,data):
        #步骤 - 登录操作 - 登录页面 - 密码为空 18684720553
        LoginPage(self.driver).login(data["user"],data["passwd"])
        #断言 - 页面的提示内容为：请输入密码
        self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_loginForm())

    @data(*ld.fail_datas)
    def test_login_1_failed_by_fail_datas(self,data):
        # 步骤 - 登录操作 - 登录页面 - 密码为空 18684720553
        LoginPage(self.driver).login(data["user"], data["passwd"])
        #断言 - 页面的提示内容为：请输入密码
        self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_pageCenter())


    # def test_login_failed_by_no_user(self):
    #     # 步骤 - 登录操作 - 登录页面 - 密码为空 18684720553
    #     LoginPage(self.driver).login("", "python")
    #     # 断言 - 页面的提示内容为：请输入密码
    #     self.assertEqual("请输入手机号码", LoginPage(self.driver).get_error_msg_from_loginForm())
    #
    # def test_login_failed_by_wrong_user_formater(self):
    #     # 步骤 - 登录操作 - 登录页面 -
    #     LoginPage(self.driver).login("1867744","python")
    #     self.assertEqual("请输入正确的手机号",LoginPage(self.driver).get_error_msg_from_loginForm())


















