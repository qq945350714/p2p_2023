import random
from bs4 import BeautifulSoup
import requests
import unittest
from api.loginapi import loginApi
import logging

from api.trust_api import trust_Api
from utils import assert_utils, request_third_api


class trust(unittest.TestCase):
    keywords = "13124523346"
    password = "test123"
    r = random.random()
    # paymentType = "chinapnrTrust"
    # formStr = "reForm"
    # amount = "1000"
    # valicode = "8888"


    def setUp(self) -> None:

        self.login = loginApi()
        self.session = requests.Session()
        self.trust = trust_Api()
    def tearDown(self) -> None:
        self.session.close()
    def test_001register(self):
        # 登录成功
        response = self.login.get_login(self.session,self.keywords,self.password)
        print(response.json())
        # 发送开户第三方接口请求
        response2 = self.trust.trust_01_register(self.session)
        html = response2.json().get("description").get("form")
        response = request_third_api(html)
        print(response.text)
    def test_002trust_verifycode(self):
        # 获取充值短信验证码

        response = self.trust.trust_verifycode(self.session,self.r)
        print(response.text)

    def test_003getdata(self):
        # 获取充值信息
        response = self.login.get_login(self.session, self.keywords, self.password)
        response = self.trust.trust_verifycode(self.session,self.r)
        data = {"paymentType": "chinapnrTrust",
             "formStr": "reForm",
             "amount": "10000000",
             "valicode": "8888"}
        response = self.trust.trust_getdata(self.session,data)
        html = response.json().get("description").get("form")
        # 调用第三方充值接口,充值成功
        response = request_third_api(html)
        print(response.text)










