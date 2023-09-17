import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import time


if __name__ == '__main__':
    # 用来爬取豆瓣的电影数据
    dict_aiqing = []
    mulu = pd.read_excel("动画.xlsx")
    subject = mulu["id"]
    fail = []

    for i in range(0,len(mulu)):
        print(i)
        id = [subject[i]]

        url = 'https://movie.douban.com/subject/{}/reviews'.format(id[0])

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }

        param = {
            "start" : 0
        }

        response = requests.get(url, headers=header,params=param)



        if response.ok:
            print(response.status_code)

            soup = BeautifulSoup(response.text, 'lxml')

            contents = soup.select("#link-report-intra > span:nth-child(1)")

            for content in contents:
                intro = content.text
                # print(intro)
                id.append(intro)
                dict_aiqing.append((id))

        else:
            print("糟糕！",id[0])
            print(response.status_code)
            fail.append(id[0])

        # time.sleep(4)

    #导出到excel表格
    writer = pd.ExcelWriter('动画简介.xlsx')  # 写入Excel文件
    data = pd.DataFrame(dict_aiqing)
    data.to_excel(writer, '动画简介', float_format='%.5f')  # ‘page_1’是写入excel的sheet名
    writer.save()
    writer.close()
    # print(dict_aiqing)

    # 导出到excel表格
    writer = pd.ExcelWriter('动画失败.xlsx')  # 写入Excel文件
    data = pd.DataFrame(fail)
    data.to_excel(writer, '失败', float_format='%.5f')  # ‘page_1’是写入excel的sheet名
    writer.save()
    writer.close()

    print(fail)

    #用来强制跳出窗口，提醒我程序跑完了
    a = [0,1,2,3]
    b = [1,2,3,4]
    plt.plot(a,b)
    plt.show()