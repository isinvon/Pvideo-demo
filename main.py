import requests
import time
import json

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

processed_data = []

def showFinalList():
    for item in final_data_list:
        new_item = item.copy()
        
        new_item.pop('id', None)
        new_item.pop('isTop', None)
        
        new_item['资源名称'] = new_item.pop('question', None)
        new_item['资源链接'] = new_item.pop('answer', None)
        
        processed_data.append(new_item)
        
    print(formatListData(processed_data))

search()
getDJ()
getJuzi()
getXiaoyu()
getSearchX()

showFinalList()

