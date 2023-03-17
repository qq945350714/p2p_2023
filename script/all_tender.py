# 投资全流程
import random
import unittest
import requests
from api.approve_api import approve_Api
from api.loginapi import loginApi
from api.tender_api import tenderApi
from api.trust_api import trust_Api
from utils import request_third_api, db_conn


class mytender(unittest.TestCase):
    phone = "13124523346"
    imgVerifyCode = "8888"
    verifycode = "8888"
    phone_code = "666666"
    keywords = "13124523346"
    password = "test123"
    r = random.random()
    def setUp(self) -> None:
        self.login = loginApi()
        self.trust = trust_Api()
        self.approve = approve_Api()
        self.tender = tenderApi()
        self.session = requests.Session()
    def tearDown(self) -> None:
        self.session.close()
        sql1 = "delete i.* from mb_member_info i inner join mb_member m on i.member_id = m.id where m.phone in ('13124523341','13124523342','13124523343','13124523344','13124523345','13124523346','13124523347');"
        db_conn.delete_sql(db_name='czbk_member', sql=sql1)
        sql2 = "delete l.* from mb_member_login_log l inner join mb_member m on l.member_id = m.id where m.phone in ('13124523341','13124523342','13124523343','13124523344','13124523345','13124523346','13124523347');"
        db_conn.delete_sql(db_name='czbk_member', sql=sql2)
        sql3 = "delete from mb_member_register_log where phone in ('13124523341','13124523342','13124523343','13124523344','13124523345','13124523346','13124523347');"
        db_conn.delete_sql(db_name='czbk_member', sql=sql3)
        sql4 = "delete from mb_member where phone in ('13124523341','13124523342','13124523343','13124523344','13124523345','13124523346','13124523347');"
        db_conn.delete_sql(db_name='czbk_member', sql=sql4)

    def test_all(self):
        # 1.注册登录login
        response1 = self.login.get_imgcode(self.session, str(self.r))
        response2 = self.login.get_smscode(self.session, self.phone, self.imgVerifyCode)
        response3 = self.login.get_register(self.session,self.phone,self.password,self.verifycode,self.phone_code)
        response = self.login.get_login(self.session,self.keywords,self.password)
        print("登录成功",response.text)
        # 2.开户充值trust
        response2 = self.trust.trust_01_register(self.session)
        html = response2.json().get("description").get("form")
        response = request_third_api(html)
        print("开户 ",response.text)
        # 获取充值短信验证码
        response = self.trust.trust_verifycode(self.session, self.r)
        # 充值
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
        print("充值结果 ",response.text)

        # 3. 查看投资tender
        # 查看投资产品详情
        data = {"id": 222}
        response = self.tender.get_loaninfo(self.session, data)
        # 进行投资
        data = {"id": 222, "amount": "10000"}
        response = self.tender.get_tender(self.session, data)
        html = response.json().get("description").get("form")
        response = request_third_api(html)
        # 查看我的投资列表
        data = {"status": "tender"}
        response = self.tender.get_mytenderlist(self.session, data)
        print("我的投资列表 ",response.json())
