""" 
@File           : VideoList.py
@Time           : 2024年11月26日13:46:44
@Desc           : 爬取影视返回列表
@OriginAuthor   : SmallTeddy <https://github.com/SmallTeddy>
@ModyfyAuthor   : Sinvon
@Modify         : 2024年12月8日16:10:15
"""
import requests
import time
import json

class VideoList:
    """ 
    影视列表
    """
    def __init__(self):
        self.cookies = {
            '_clck': 'aG%2FCmMKawpPCmmrCn2dxaWVkwphmYWlpZ8KTZm9qcWloacKTwpdnwpVkZw%3D%3D%7C2%7Cfq1%7C0%7C0',
            '_clsk': f"128761241771877460%7C{int(time.time() * 1000)}22%7C1%7Capi.a3gj.cn",
        }
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://www.kkkob.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.final_data_list = []

    def get_token(self):
        response = requests.get(
            'http://www.kkkob.com/v/api/getToken',
            cookies=self.cookies,
            headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            },
            verify=False
        )
        return response.json().get('token')

    def append_list(self, response):
        json_response = response.json()
        if 'list' in json_response and json_response['list']:
            self.final_data_list.extend(json_response['list'])

    def search_videos(self, name):
        data = {'name': name, 'token': self.get_token()}
        endpoints = [
            'http://www.kkkob.com/v/api/search',
            'http://www.kkkob.com/v/api/getDJ',
            'http://www.kkkob.com/v/api/getJuzi',
            'http://www.kkkob.com/v/api/getXiaoyu',
            'http://www.kkkob.com/v/api/getSearchX',
        ]
        for endpoint in endpoints:
            response = requests.post(endpoint, cookies=self.cookies, headers=self.headers, data=data, verify=False)
            self.append_list(response)

    def get_processed_list(self):
        processed_data = []
        for item in self.final_data_list:
            processed_data.append({
                '资源名称': item.get('question'),
                '资源链接': item.get('answer'),
            })
        return processed_data

    def get_videos(self, name):
        self.final_data_list.clear()
        self.search_videos(name)
        return self.get_processed_list()

# 示例使用
# if __name__ == "__main__":
#     video_list_tool = VideoList()
#     name = input("请输入要搜索的名称: ")
#     video_list = video_list_tool.get_videos(name)
#     print(json.dumps(video_list, indent=4, ensure_ascii=False))
