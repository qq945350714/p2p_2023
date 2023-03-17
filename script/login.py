import random
import requests
import unittest
from parameterized import parameterized
from api.loginapi import loginApi
import logging
from utils import assert_utils, get_register, get_parameterized_data


class login(unittest.TestCase):
    phone = "13124523346"
    imgVerifyCode = "8888"
    phone_code = "666666"
    password = "test123"

    r = random.random()
    def setUp(self):
        self.login = loginApi()
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    # 获取图片验证码
    def test_001get_imgcode(self):
        response = self.login.get_imgcode(self.session, str(self.r))
        self.assertEqual(200, response.status_code)

    # 获取短信验证码
    def test_002get_smscode(self):
        response1 = self.login.get_imgcode(self.session, str(self.r))
        response2 = self.login.get_smscode(self.session, self.phone, self.imgVerifyCode)
        assert_utils(self,response2,200,200,"短信发送成功")

    # 注册
    @parameterized.expand(get_parameterized_data("register1.json","test_register","phone,pwd,imgVerifyCode,phoneCode,dyServer,invite_phone,status_code,status,description"))
    def test_003get_register(self, phone, pwd, imgVerifyCode, phoneCode, dyServer, invite_phone,status_code, status, description):
        response1 = self.login.get_imgcode(self.session, str(self.r))

        response2 = self.login.get_smscode(self.session, phone, self.imgVerifyCode)
        print(response2.text)
        response3 = self.login.get_register(self.session, phone, pwd, imgVerifyCode, phoneCode)
        print(response3.text)
        assert_utils(self, response3, status_code, status, description)



    # 登录
    def test_004get_login(self):
        response1 = self.login.get_imgcode(self.session, str(self.r))
        response2 = self.login.get_smscode(self.session, self.phone, self.imgVerifyCode)
        response3 = self.login.get_register(self.session,self.phone,self.password,self.imgVerifyCode,self.phone_code)
        response4 = self.login.get_login(self.session,self.phone,self.password)
        assert_utils(self,response4, 200, 200, "登录成功")
        print(response4.json())
