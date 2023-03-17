from app import base_url
import requests

class approve_Api():
    def __init__(self):
        self.url_approve = base_url + "/member/realname/approverealname"
        self.url_get_approve = base_url + "/member/member/getapprove"
    def approve(self,session,realname,card_id):
        data = {"realname": realname, "card_id": card_id}
        response = session.post(url=self.url_approve, data=data,files={"x":"y"})
        return response

    def get_approve(self, session):
        response = session.post(url=self.url_get_approve)
        return response
