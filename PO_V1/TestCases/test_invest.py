#-*- coding: utf-8 -*-

"""
用例1：正常投资，投资金额：1000
异常用例：
    1）投资为10  提示 要为100的整数倍
    2）投资为12  提示 要为10的整数倍
    3）投资为非数字 提示 要为1-的整数倍
    4）投资为0/负数/含空格/空  提示 请正确填写投标金额

    5）投资数 > 投资可投额 提示 购买标的金额不能大于标剩余金额
    #充值10万，创建一个借款9万块的标

    6）投资数 > 你可用余额 且 标可投 > 提示 你投的钱 > 你能投的钱
    你只有10万，你要投20万，标的可投为200万
    # 另外一个账号，永远都是10万。创建一个标为200万 你去投20万
"""

#前置（准备工作），步骤（用户页面操作），断言（页面操作）
#前置 - 通过代码来创建前置 - 尽量少的依赖环境数据
'''
1.投资账号登录：
2.要有可投的标 - 有可投余额。没有就加标？ -- 接口
3.用户余额充足 - 充值5000块钱 - 接口实现
              - 投资金额 - 不充。不大了呢，一口气冲2百万
              - 充个2000万（）
'''
#步骤
"""
1、首页  选一个标： 进入标页面
2、投资页面 - 输入金额，进行投资
"""

#断言
'''
1、个人页面 - 个人余额少的部分 == 投资前的金额 - 投资后的金额
2、投资记录
3、标的可投金额 - 投资金额 = 投资之后的金额
'''
import unittest

from ddt import ddt
from selenium import webdriver

from PO_V1.PageObjects.index_page import IndexPage
from PO_V1.PageObjects.login_page import LoginPage
from PO_V1.PageObjects.user_page import UserPage
from PO_V1.TestDatas import login_datas as ld


@ddt
class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #1、登录成功
        # 前置 - 打开网页
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        driver = LoginPage(cls.driver).login('18684720553','python')
        LoginPage(cls.driver).login(ld.success_data["user"], ld.success_data["passwd"])


    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass
    # def tearDown(self):
    #     self.driver.refresh()


    def test_invest_success(self):
        #2000 步骤
        #首页 - 选标投资
        IndexPage(self.driver).click_invest_button()
        # 标页面 - 获取用户余额、获取标的可投金额
        user_money = BidPage(self.driver).get_user_left_money().get_attribute("placeholder")
        print(user_money)
        bid_money = BidPage(self.driver).get_bid_money()
        print(bid_money)
        #标页面 - 投资操作 2000
        #标页面 - 弹出框
        BidPage(self.driver).invest(2000)
        #断言
        #投资金额 = 投资前钱 - 投资后的钱
        #个人页面 - 获取投资后的用户的可用余额
        after_user_money = UserPage(self.driver).get_user_left_money()
        print(after_user_money)
        #标页面 - 获取投资后的标可投金额
        pass


    def test_invest_failed_wrong_format(self):
        # 首页 - 选标投资
        # 获取 个人余额、获取标的可投金额
        # 标页面 - 获取用户余额、获取标的可投金额
        # 标页面 - 投资操作 10/-1/0/@%%%/空
        #断言
        #提示信息对不对？？
        #个人的钱有没有少？？

        pass









