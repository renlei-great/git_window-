import requests

session = requests.session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Cookie": "ref=5e47a68608d77; SERVERID=_srv80-67_; _vid=C8CB095834F000016C8C104A70AD1178; _cpmuid=1371810089; Hm_lvt_500f908d39095efce74d0e9c64f55ffb=1581754025; _user=43671a2257bde25d37ae8746779bb860_181902976_1581754303; _preemail=17548253266; _uid=181902976; _email=17548253266; _laid=0; _sso=181902976; Hm_lpvt_500f908d39095efce74d0e9c64f55ffb=1581754302; onlinenum=c%3A0; wpresence=J3kNayk6ywESXS6KnokRCxkcXtVEWjsfXkenxQ.ZGZ0MTgxOTAyOTc2",
}

# from_data = {
#             "loginemail": "17548253266",
#             "password": "123456",
#             "rcode": ""
#              }
#
# # url = "http://www.renren.com/PLogin.do"
#
# url = "https://security.kaixin001.com/login/login_auth.php"
#
# session.post(url, data=from_data, headers=headers)

r = requests.get("http://www.kaixin001.com/home/?uid=181902976",headers=headers)

with open("kxw.html", "w", encoding='utf8') as f:
    f.write(r.content.decode())