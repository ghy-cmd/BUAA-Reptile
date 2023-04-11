import time

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = ''#your web
    headers = {
        'User-Agent': '',#TO DO
        'Cookie':''#TO DO
    }
    data = {#TO DO
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
    while(True):
        res = requests.post(url, data=data, headers=headers)
        content = BeautifulSoup(res.text, "html.parser")
        con = content.find_all('td')
        for d in con:
            if d.find('input') and d.find('input')['id'] == 'xkyq_2021-2022-3-B3J060311-001-A':#TO DO
                l = d.text.find(':')
                r = d.text.rfind('/')
                num = int(d.text[l + 1:r])
                print(num)
                # if num == 0:
        time.sleep(30)
