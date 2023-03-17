import unittest
import requests

from api.loginapi import loginApi
from api.tender_api import tenderApi
from utils import request_third_api


class tender(unittest.TestCase):

    keywords = "13124523346"
    password = "test123"
    def setUp(self):
        self.session = requests.Session()
        self.tender = tenderApi()
        self.login = loginApi()
    def tearDown(self):
        self.session.close()

    # 查看投资产品详情
    def test_001getloaninfo(self):
        response = self.login.get_login(self.session, self.keywords, self.password)
        print(response.json())
        data = {"id":222}
        response = self.tender.get_loaninfo(self.session,data)
        print(response.text)
    # 进行投资,获取第三方接口数据,并再次发送投资
    def test_002get_tender(self):
        response = self.login.get_login(self.session, self.keywords, self.password)
        print(response.json())
        data = {"id": 222, "amount": "1000"}
        response = self.tender.get_tender(self.session, data)
        html = response.json().get("description").get("form")
        response = request_third_api(html)
        print(response.text)

    # 我的投资列表
    def test_003get_mytenderlist(self):
        response = self.login.get_login(self.session, self.keywords, self.password)
        data = {"status": "tender"}
        response = self.tender.get_mytenderlist(self.session, data)
        print(response.json())
