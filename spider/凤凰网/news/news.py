'''
    raw.json 由采集器获取
    news.py 对 raw.json 进行处理, 获取更加详细的 news.json
'''

import requests
from bs4 import BeautifulSoup
import json
import re

# url = 'https://news.ifeng.com/'
commentUrl = 'https://gentie.ifeng.com/c/comment/'

headers_data = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: userid=1700057622401_7zf21s5738; if_mid=1700057622401_7zf21s5738; prov=cn0531; city=0531; weather_city=sd_jn; region_ip=124.133.234.x; region_ver=1.2; BAIDU_SSP_lcr=https://www.baidu.com/link?url=HCB5SGtGmeW04UzgzIy0Jy566EoitlwuGpqIIv6U-E7&wd=&eqid=a7aabba2006f57aa000000026554d214; Hm_lvt_854ddd4a39be7c994420d51fb2e3ded7=1700057624; Hm_lpvt_854ddd4a39be7c994420d51fb2e3ded7=1700057624; adb_isBlock=0; ifengWindowCookieName_1065=2; news20231115=1
Host: news.ifeng.com
If-Modified-Since: Wed, 15 Nov 2023 14:10:52 GMT
Referer: https://www.ifeng.com/
Sec-Ch-Ua: "Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-site
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0
"""
# 将字符串按行拆分，并提取键值对
headers_list = [line.split(': ', 1) for line in headers_data.strip().split('\n')]
# 创建字典
headers = {key: value for key, value in headers_list}

with open('raw.json', 'r', encoding='utf-8') as f:
    data = f.read()
    data = json.loads(data)


def getData(url):
    try:
        # 获取响应
        response = requests.get(url=url, headers=headers)
        # soup确定到目标数据
        soup = BeautifulSoup(response.text, 'html.parser')
        script = str(soup.find('script', string=re.compile(r'var allData'))).split('\n')
        allData = json.loads(script[0].replace('<script>var allData = ', '').strip(';'))
        # 根据目标数据allData进一步获取
        docData = allData['docData']
        detail = docData['fhhAccountDetail']
        keywords = allData['keywords']
        # 进一步获取
        contentData = docData['contentData']
        path_url = commentUrl + url.split("/")[-1]
        newsTime = detail['newsTime']
        source = detail['catename']
        content = str(contentData['contentList'][0]['data'])

        # 使用正则表达式匹配<p>标签内的文本
        pattern = re.compile(r'<p>(.*?)<\/p>')
        matches = re.findall(pattern, content)

        # 将匹配到的文本连接成一个字符串
        result_text = '\n'.join(matches)

        return newsTime, source, keywords, result_text, path_url
    except:
        pass

cnt = 0
for item in data:
    cnt += 1
    try:
        # 获取到url
        url = item['url']
        newsTime, source, keywords, content, path_url = getData(url)
        # 修改数据
        item['id'] = cnt
        item['newsTime'] = newsTime
        item['source'] = source
        item['content'] = content
        item['keywords'] = keywords
        item['commentUrl'] = path_url
    except:
        pass

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
