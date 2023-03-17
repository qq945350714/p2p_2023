import json

from bs4 import BeautifulSoup
import requests
import pymysql
import app
# 断言参数化



def assert_utils(self,response,status_code,status,description):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(status, response.json().get("status"))
    self.assertIn(description, response.json().get("description"))

# 解析form表单中的内容，并提取第三方请求的参数
def request_third_api(html):
    soup = BeautifulSoup(html, "html.parser")
    third_url = soup.form['action']
    data = {}
    for input in soup.find_all('input'):
        data.setdefault(input['name'], input['value'])
    # 发送第三方请求
    response = requests.post(third_url, data=data)
    return response


# 数据库操作
class db_conn:
    @classmethod
    def get_conn(cls,db_name):
        conn = pymysql.connect(host=app.db_url, port=3306, user=app.db_user, password=app.db_pwd,
                               database="czbk_member",autocommit=True)
        return conn
    @classmethod
    def close_conn(cls,cursor=None,conn=None):
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    @classmethod
    def delete_sql(cls,db_name,sql):
        try:
            conn = cls.get_conn(db_name)
            cursor = conn.cursor()
            cursor.execute(sql)
        except Exception as e:
            conn.rollback()
        finally:
            cls.close_conn(cursor,conn)


 # 读取获取图片验证码JSON文件数据
def get_imgVerify_data(filename):
    file = app.base_dir + "/data/" + filename
    data_list = []
    with open(file=file,encoding="utf-8") as f:
        json_data = json.load(f)
        json_data2 = json_data.get("test_get_img_verify_code")
        for n in json_data2:
            data_list.append((n.get("type"),n.get("status_code")))
    return data_list

# 读取注册数据
def get_register(filename):
    file = app.base_dir + "/data/" + filename
    data_list = []
    with open(file=file, encoding="utf-8") as f:
        json_data = json.load(f)
        json_data2 = json_data.get("test_register")
        for n in json_data2:
            data_list.append((n.get("phone"),n.get("pwd"),n.get("imgVerifyCode"),n.get("phoneCode"),n.get("dyServer"),n.get("invite_phone"),n.get("status_code"),n.get("status"),n.get("description")))
    return data_list

#定义统一的读取所有参数数据文件的方法
    #filename： 参数数据文件的文件名
    #method_name: 参数数据文件中定义的测试数据列表的名称，如：test_get_img_verify_code
    #param_names: 参数数据文件一组测试数据中所有的参数组成的字符串，如："type,status_code"

def get_parameterized_data(filename,method_name,param_names):

    file = app.base_dir + "/data/" + filename
    test_case_data = []
    with open(file=file,encoding="utf-8") as f:
        file_data = json.load(f)
        test_data_list = file_data.get(method_name)
        for test_data in test_data_list:
            # print("test_data是每个大括号里的数据:".format(test_data))
            test_param = []
            for param in param_names.split(","):
                # print("param是传入的参数化的每一个项:{}".format(param))
                test_param.append(test_data.get(param))
                # test_params = tuple(test_param)
            # print("test_params是{}".format(test_params))
            # 每完成一组测试数据的读取，就添加到test_case_data后，直到所有的测试数据读取完毕
            test_case_data.append(test_param)
    # print("test_case_data = {}".format(test_case_data))
    return test_case_data


