from urllib import request, parse
import string

def get_params():

    head = 'http://baidu.com/s?wd='
    name = '美女'
    url = head+name
    encode_url = parse.quote(url, safe=string.printable)
    print(encode_url)
    response = request.urlopen(encode_url)
    print(response)
    data = response.read().decode()
    print(data)
    with open('02-baidu.html', 'w', encoding='utf-8') as f:
        f.write(data)


get_params()