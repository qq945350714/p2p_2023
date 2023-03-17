from app import base_url
import requests

class trust_Api():
    def __init__(self):

        self.trust_url_01 = base_url + "/trust/trust/register"
        self.url_trust_verifycode = base_url + "/common/public/verifycode/"
        self.url_trust_recharge = base_url + "/trust/trust/recharge"

    def trust_01_register(self,session):
        response = session.post(url=self.trust_url_01)
        return response
    # 获取充值验证码
    def trust_verifycode(self,session,r):
        url = self.url_trust_verifycode + str(r)
        response = session.get(url)
        return response

    # 获取充值信息

    def trust_getdata(self,session,data):
        response = session.post(url=self.url_trust_recharge, data=data)
        return response