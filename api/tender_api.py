import requests

from app import base_url


class tenderApi():
    def __init__(self):
        self.url_loaninfo = base_url + "/common/loan/loaninfo"
        self.url_tender = base_url + "/trust/trust/tender"
        self.url_mytenderlist = base_url + "/loan/tender/mytenderlist"

    # 投资产品详情
    def get_loaninfo(self,session,myid):
        response = session.post(url=self.url_loaninfo,data=myid)
        return response

    # 进行投资
    def get_tender(self,session,data):
        response = session.post(url=self.url_tender,data=data)
        return response

    # 我的投资列表
    def get_mytenderlist(self,session,data):
        response = session.post(url=self.url_mytenderlist, data=data)
        return response


