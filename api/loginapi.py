import requests

from app import base_url


class loginApi():
    def __init__(self):
        self.url_imgcode = base_url + '/common/public/verifycode1/'
        self.url_smscode = base_url + '/member/public/sendSms'
        self.register_url = base_url + '/member/public/reg'
        self.login_url = base_url + "/member/public/login"

    def get_imgcode(self,session,r):
       url = self.url_imgcode + r
       response = session.get(url=url)
       return response
    def get_smscode(self,session,phone,imgVerifyCode):

       data = {'phone': phone, 'imgVerifyCode': imgVerifyCode, 'type': 'reg'}
       response = session.post(url=self.url_smscode,data=data)
       return response
    def get_register(self,session,phone,password,verifycode,phone_code):
        data = {"phone": phone,
                "password": password,
                "verifycode": verifycode,
                 "phone_code": phone_code,
                 "dy_server": "on"}
        response = session.post(url=self.register_url,data=data)
        return response
    def get_login(self,session,keywords,password):
        data = {"keywords": keywords,
                 "password": password}
        response = session.post(url=self.login_url, data=data)
        return response


