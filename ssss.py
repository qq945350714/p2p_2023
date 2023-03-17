from utils import get_parameterized_data,get_register

str = "phone,pwd,imgVerifyCode,phoneCode,dyServer,invite_phone,status_code,status,description"

print(get_parameterized_data("register1.json", "test_register", str))

print(get_register("register1.json"))