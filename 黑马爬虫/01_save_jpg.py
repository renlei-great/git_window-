import requests

byt = "\n".encode()
i = 0
while True:
    # 发送请求
    # url = 'https://www.sina.com.cn/'
    url = 'http://tieba.baidu.com/f?kw=%E6%AD%A6%E6%B1%89&pn={}'.format(i)
    response = requests.get(url)
    i += 50
    byt += response.content
    if i >500:
        break


# 用content保存数据
# with open('content.html', 'wb') as f:
#     f.write(response.content)

# 用text保存数据
print("保存")
response.encoding='utf8'
print(response.text)
with open('content1.html', 'bw') as f:
    f.write(byt)
