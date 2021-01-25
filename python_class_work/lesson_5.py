import requests
import pprint
import  jsonpath
# url_api_reg = "http://8.129.91.152:8766/futureloan/member/register"
# api_data_reg = {
#     "mobile_phone": "13606776518",
#     "pwd": "12345678",
#     "type": "1",
#     "reg_name": "lemon666"
# }
# head_reg = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
# response = requests.post(url=url_api_reg, json=api_data_reg, headers=head_reg)
# pprint.pprint(response.json())

# url_api_log = "http://8.129.91.152:8766/futureloan/member/login"
# api_data_log = {
#     "mobile_phone": "13606776518",
#     "pwd": "12345678"
# }
# head_log = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
# response = requests.post(url=url_api_log, json=api_data_log, headers=head_log)
# pprint.pprint(response.json())
# res = response.json()
#
# member_id = jsonpath.jsonpath(res,"$.data.id")[0]
# token = jsonpath.jsonpath(res,"$.data.token_info.token")[0]
# url_api_rec = "http://8.129.91.152:8766/futureloan/member/recharge"
# api_data_rec = {
#     "member_id": member_id,
#     "amount": 6300
# }
# head_rec = {"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": "Bearer "+token}
# response = requests.post(url=url_api_rec, json=api_data_rec, headers=head_rec)
# pprint.pprint(response.json())

url_baidu = "http://www.baidu.com/s"
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
parameter ={"wd": "柠檬班"}
response = requests.get(url=url_baidu, headers=head, params=parameter)
print(response.content.decode("utf8"))
