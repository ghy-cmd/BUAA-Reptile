import time

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = ''
    headers = {
        'User-Agent': '',
        'Cookie': ''
    }
    data = {
        'kcdmpx': '',
        'kcmcpx': '',
        ' rlpx': '',
        'rwh': '',
        'zy': '',
        'qz': '',
        'token': '',
        'pageKclb': '',
        'pageXklb': '',
        'pageXkmkdm': '',
        'pageXnxq': '',
        'pageKkxiaoqu': '',
        'pageKkyx': '',
        'pageKcmc': ''
    }
    while (True):
        res = requests.post(url, data=data, headers=headers)
        print(res.status_code)
        # print(res.text)
        time.sleep(20)
