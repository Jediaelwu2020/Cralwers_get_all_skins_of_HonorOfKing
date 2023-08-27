# coding : utf8
# time : 2023/8/26 14:54
# author : jediaelwu2020@163.com
# describe :
"""

"""
import time
import requests

agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
herolist_num = []
herolist_name =[]
data = requests.get("https://pvp.qq.com/web201605/js/herolist.json", headers=agent).json()
print(data)

for item in data:
    herolist_num.append(item['ename'])  # 拿到英雄的编号
    herolist_name.append(item['cname'])  # 拿到英雄的名字
print(herolist_num)
print(herolist_name)

# 开始爬取
for i in herolist_num:
    index = herolist_num.index(i)
    img_head_portrait = requests.get(
        f'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{i}/{i}.jpg',headers=agent).content

    with open(f'.\img_little_head_portrait\img_{herolist_name[index]}_{i}.jpg', mode='wb') as f:
        print(f'正在打印图片img_{herolist_name[index]}_{i}.jpg。')
        f.write(img_head_portrait)




