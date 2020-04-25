import requests


class TieBaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        # 定义请求头中的user_agent
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

    def get_url_list(self):  # 生成URL列表
        # 使用了列表生成式，返回一个列表
        return ['http://tieba.baidu.com/f?kw='+ self.tieba_name +'&pn={}'.format(i*50) for i in range(1000)]

    def pares_url(self,url):  # 访问URL，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content

    def save_response(self,html, idnex):  # 保存到本地
        url_path = '{}-{}页.html'.format(self.tieba_name, idnex+1)
        with open(url_path, 'wb') as f:
            f.write(html)

    def main(self):  # 爬取贴吧的主要逻辑处理方法
        # 生成URL列表
        url_list = self.get_url_list()
        # 遍历，访问URL，获取响应
        for url in url_list:
            # 访问url,获取响应
            index = url_list.index(url)
            html = self.pares_url(url)
            # 保存到本地
            self.save_response(html, index)


if __name__ == '__main__':
    tieba = TieBaSpider('美女视频')
    tieba.main()