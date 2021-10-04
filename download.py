# -*- coding:utf-8 -*-

"""
时间:2021年10月04日
作者:幻非
"""

import requests
import os
import sys


def download(self):
    ts_list = []
    headers = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 '
        'Safari/537.36 '
    }
    response = requests.get(url=self, headers=headers).text.split()
    url_path = os.path.dirname(self) + '//'
    for i in response:
        if i.find('#') != 0:
            ts_list.append(i)
    # for i in ts_list:
    for i in range(len(ts_list)):
        num = int((i+1) / len(ts_list) * 100) // 2
        print("\r", end="")
        print("[" + "+" * num + '-' * (50 - num) + "]", "{}%: ".format(num * 2), end="")
        sys.stdout.flush()
        with open(os.path.basename(ts_list[i]), mode='wb') as f:
            f.write(requests.get(url=url_path + ts_list[i]).content)
    os.popen('copy /b *.ts video.mp4').read()
    os.system('del /Q *.ts')


if __name__ == "__main__":
    url = input("请输入m3u8地址:")
    download(url)
