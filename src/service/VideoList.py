""" 
@description: 影视爬取_v2
@author: SmallTeddy
@see https://github.com/SmallTeddy/video-resource/blob/main/src/main.py
"""
import requests
import time
import json
import base64
import pytesseract
from PIL import Image
from io import BytesIO


class Api:

    def __init__(self):
        current_timestamp = int(time.time() * 1000)
        self.cookies = {
            '_clck': 'aG%2FCmMKawpPCmmrCn2dxaWVkwphmYWlpZ8KTZm9qcWloacKTwpdnwpVkZw%3D%3D%7C2%7Cfq1%7C0%7C0',
            '_clsk': '128761241771877460%7C' + str(current_timestamp) + '22%7C1%7Capi.a3gj.cn',
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

    def _getToken(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'If-None-Match': 'W/"27-vcQAX3AjsSgVDyEpCQWBBpZwj/Y"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

        response = requests.get('http://www.kkkob.com/v/api/getToken',
                                cookies=self.cookies, headers=headers, verify=False)

        return response.json()['token']

    def _formatListData(self, response):
        # print(json.dumps(response, indent=4, ensure_ascii=False)) # debug
        return json.dumps(response, indent=4, ensure_ascii=False)

    def _appendList(self, response):
        json_response = response.json()
        if 'list' in json_response and json_response['list']:
            for item in json_response['list']:
                self.final_data_list.append(item)

    def _search(self, data):
        response = requests.post('http://www.kkkob.com/v/api/search',
                                 cookies=self.cookies, headers=self.headers, data=data, verify=False)
        self._appendList(response)

    def _getDJ(self, data):
        response = requests.post('http://www.kkkob.com/v/api/getDJ',
                                 cookies=self.cookies, headers=self.headers, data=data, verify=False)
        self._appendList(response)

    def _getJuzi(self, data):
        response = requests.post('http://www.kkkob.com/v/api/getJuzi',
                                 cookies=self.cookies, headers=self.headers, data=data, verify=False)
        self._appendList(response)

    def _getXiaoyu(self, data):
        response = requests.post('http://www.kkkob.com/v/api/getXiaoyu',
                                 cookies=self.cookies, headers=self.headers, data=data, verify=False)
        self._appendList(response)

    def _getSearchX(self, data):
        response = requests.post('http://www.kkkob.com/v/api/getSearchX',
                                 cookies=self.cookies, headers=self.headers, data=data, verify=False)
        self._appendList(response)

    def _getSearchUpYunSo(name):
        # 发送请求获取数据
        response = requests.get(
            f'https://upapi.juapp9.com/search?keyword={name}&page=1')

        # 解码 base64 数据
        image_data = base64.b64decode(response.text)

        # 将解码后的数据转换为字典
        image_json_data = json.loads(image_data)

        if image_json_data['status'] == 'failed':
            print(image_json_data['msg'])
            return

        # 获取 code 字段的值
        image_code_url = image_json_data["result"]["code"]

        image_response = requests.get(image_code_url)

        # 将解码后的数据转换为图像
        image = Image.open(BytesIO(image_response.content))
        image.save('output_image.png')  # 保存图像到文件

        # 使用 Tesseract 识别图像中的文本
        captcha_text = pytesseract.image_to_string(image)
        # print(f'识别的验证码: {captcha_text.strip()}')

        with_code_response = requests.get(
            f"https://upapi.juapp9.com/search?keyword={name}&page=1&code={captcha_text.strip()}")

        with_code_data = base64.b64decode(with_code_response.text)
        with_code_json_data = json.loads(with_code_data)

        final_data_list = with_code_json_data['result']['items'][4:]

        print(final_data_list)

    def _getXshyun(self, name):
        try:
            # 发送请求获取数据
            response = requests.get(f'https://jx.xshyun.top/api.php?wd={name}')
            response.raise_for_status()  # 检查请求是否成功
            data_list = response.json().get('list', [])

            xshyun_final_data_list = []

            for item in data_list:
                # 发送请求获取详细信息
                data_info = requests.get(
                    f'https://jx.xshyun.top/api.php?ids={item["vod_id"]}&source={item["source"]}')
                data_info.raise_for_status()  # 检查请求是否成功

                info = data_info.json().get('list', [])
                if info:  # 确保 info 不为空
                    xshyun_final_data_list.append(info[0])  # 只添加第一个元素

            qa_list = [{'question': item['vod_name'], 'answer': item['vod_play_url']}
                       for item in xshyun_final_data_list]
            for item in qa_list:
                item['answer'] = item['answer'].split('$')
            self.final_data_list.extend(qa_list)

        except requests.RequestException as e:
            print(f"请求错误: {e}")
        except Exception as e:
            print(f"发生错误: {e}")

    def showFinalList(self, name):
        data = {
            'name': name,
            'token': self._getToken()
        }
        # ================数据采集=====start======
        self._search(data=data)
        self._getDJ(data=data)
        self._getJuzi(data=data)
        self._getXiaoyu(data=data)
        self._getSearchX(data=data)
        # getSearchUpYunSo()
        self._getXshyun(name=name)
        # ==============数据采集=======end=======

        processed_data = []
        for item in self.final_data_list:
            new_item = item.copy()

            new_item['资源名称'] = new_item.pop('question', None)
            new_item['资源链接'] = new_item.pop('answer', None)

            new_item.pop('id', None)
            new_item.pop('isTop', None)
            new_item.pop('question', None)
            new_item.pop('answer', None)

            processed_data.append(new_item)

        print(self._formatListData(processed_data))  # debug
        # return self._formatListData(processed_data)
