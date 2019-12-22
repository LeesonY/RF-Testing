#-*- coding: utf-8 -*-
from PO_V1.TestDatas.Comon_Datas import base_url
#正常场景
success_data = {"user":"18684720553","passwd":"python","check":"{}/Index/index".format(base_url)}





# 密码为空/用户名为空/用户名格式不正确
wrong_datas = [
    {"user":"18684720553","passwd":"","check":"请输入密码"},
    {"user":"","passwd":"python","check":"请输入手机号"},
    {"user":"186847","passwd":"python","check":"请输入正确的手机号"},
    {"user":"1868472055311","passwd":"python","check":"请输入正确的手机号"}
]

#用户名未注册 /密码错误
fail_datas = [
    {"user":"18600000000","passwd":"python","check":"此账号没有经过授权，请联系管理员!"},
    {"user":"18684720553","passwd":"111","check":"帐号或密码错误!"}
]



























