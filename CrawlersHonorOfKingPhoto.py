# coding : utf8
# time : 2023/7/24 11:10
# author : jediaelwu2020@163.com
# describe :
"""

"""
import time
import requests

agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
herolist_num = []
herolist_skin_num = []
herolist_name =[]
herolist = requests.get("https://pvp.qq.com/web201605/js/herolist.json", headers=agent)
# print(herolist)
# print(herolist.text) # 编码后的文本：和平守望|金属风暴
# print(herolist.content)     # 没编码的文本：\xe8\x8e\xb1\xe8\xa5\xbf\xe5\xa5\xa5
data = herolist.json()     # json格式
print(data)
time.sleep(100)

for item in data:
    herolist_num.append(item['ename'])  # 拿到英雄的编号
    herolist_name.append(item['cname'])  # 拿到英雄的名字
    if item['ename'] == 518:      # 马超编号有问题，这里额外取出
        herolist_skin_num.append(3)
        continue
    herolist_skin_num.append(item['skin_name'].count('|')+1) # 拿到对应的皮肤数量
print(herolist_num)
print(herolist_name)
print(herolist_skin_num)

# 开始爬取
for i in herolist_num:
    time.sleep(1)
    index=herolist_num.index(i)
    for k in range(1,herolist_skin_num[index]+1 ):
        img_skin = requests.get(
            f'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{i}/{i}-bigskin-{k}.jpg',
            headers=agent).content
        with open(f'.\img_skin\img_{i}_{herolist_name[index]}_{k}.jpg', mode='wb') as f:
            print(f'正在打印图片img_{i}_{herolist_name[index]}_{k}.jpg。')
            f.write(img_skin)

