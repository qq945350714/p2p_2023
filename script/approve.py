import unittest

from api.approve_api import approve_Api
from api.loginapi import loginApi
import requests

class approve(unittest.TestCase):
    realname = "张三"
    card_id = "110117199003070995"
    keywords = "13124523346"
    password = "test123"
    def setUp(self) -> None:
        self.login = loginApi()
        self.approve = approve_Api()
        self.session = requests.Session()
        self.response1 = self.login.get_login(self.session, self.keywords, self.password)
    def tearDown(self) -> None:
        self.session.close()
    def test_approve(self):
        print(self.response1.json())
        response2 = self.approve.approve(self.session, self.realname, self.card_id)

    def test_getmsg_approve(self):
        response = self.approve.get_approve(self.session)

