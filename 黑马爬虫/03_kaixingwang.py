import requests

session = requests.session()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

from_data = {
            "loginemail": "17548253266",
            "password": "123456",
            "rcode": ""
             }

# url = "http://www.renren.com/PLogin.do"

# url = "https://security.kaixin001.com/login/login_auth.php"

url = "https://security.kaixin001.com/login/login_post.php"

session.post(url, data=from_data, headers=headers)

r = session.get("http://www.kaixin001.com/home/?uid=181902976",headers=headers)

with open("renrne1.html", "w", encoding='utf8') as f:
    f.write(r.content.decode())