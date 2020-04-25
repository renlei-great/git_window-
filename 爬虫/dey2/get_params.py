from urllib import request, parse
import string

def get_params():
    url = 'http://baidu.com/s?'
    params = {
        'wd':'中文',
        'key':'zhong',
        'value':'san',
    }
    str_params = parse.urlencode(params)
    print(str_params)
    end_url = url+ str_params
    start_url = request.quote(end_url, safe=string.printable)
    print(start_url)
    response = request.urlopen(start_url)
    print(response)
    data = response.read().decode('utf-8')
    print(data)


get_params()
