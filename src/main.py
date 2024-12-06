import requests
import time
import json
import base64
import pytesseract
from PIL import Image
from io import BytesIO

# 获取用户输入
name = input("请输入要搜索的名称: ")

def getToken():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"27-vcQAX3AjsSgVDyEpCQWBBpZwj/Y"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = requests.get('http://www.kkkob.com/v/api/getToken', cookies=cookies, headers=headers, verify=False)
    
    return response.json()['token']

current_timestamp = int(time.time() * 1000)

cookies = {
    '_clck': 'aG%2FCmMKawpPCmmrCn2dxaWVkwphmYWlpZ8KTZm9qcWloacKTwpdnwpVkZw%3D%3D%7C2%7Cfq1%7C0%7C0',
    '_clsk': '128761241771877460%7C' + str(current_timestamp) + '22%7C1%7Capi.a3gj.cn',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.kkkob.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'name': name,
    'token': getToken()
}

def formatListData(response):
    print(json.dumps(response, indent=4, ensure_ascii=False))

final_data_list = []

def appendList(response):
    json_response = response.json()
    if 'list' in json_response and json_response['list']:
        for item in json_response['list']:
            final_data_list.append(item)

def search():
    response = requests.post('http://www.kkkob.com/v/api/search', cookies=cookies, headers=headers, data=data, verify=False)
    appendList(response)

def getDJ():
    response = requests.post('http://www.kkkob.com/v/api/getDJ', cookies=cookies, headers=headers, data=data, verify=False)
    appendList(response)

def getJuzi():
    response = requests.post('http://www.kkkob.com/v/api/getJuzi', cookies=cookies, headers=headers, data=data, verify=False)
    appendList(response)

def getXiaoyu():
    response = requests.post('http://www.kkkob.com/v/api/getXiaoyu', cookies=cookies, headers=headers, data=data, verify=False)
    appendList(response)

def getSearchX():
    response = requests.post('http://www.kkkob.com/v/api/getSearchX', cookies=cookies, headers=headers, data=data, verify=False)
    appendList(response)

def getSearchUpYunSo():
    # 发送请求获取数据
    response = requests.get(f'https://upapi.juapp9.com/search?keyword={name}&page=1')

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
    
    with_code_response = requests.get(f"https://upapi.juapp9.com/search?keyword={name}&page=1&code={captcha_text.strip()}")

    with_code_data = base64.b64decode(with_code_response.text)
    with_code_json_data = json.loads(with_code_data)
    
    final_data_list = with_code_json_data['result']['items'][4:]
    
    print(final_data_list)

processed_data = []

def showFinalList():
    for item in final_data_list:
        new_item = item.copy()
        
        new_item['资源名称'] = new_item.pop('question', None)
        new_item['资源链接'] = new_item.pop('answer', None)
        
        new_item.pop('id', None)
        new_item.pop('isTop', None)
        new_item.pop('question', None)
        new_item.pop('answer', None)
        
        processed_data.append(new_item)
        
    print(formatListData(processed_data))

search()
getDJ()
getJuzi()
getXiaoyu()
getSearchX()

# getSearchUpYunSo()

showFinalList()
