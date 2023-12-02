import urllib.request

for i in range(10):
    st = i*20
    url = f'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={st}&limit=20'

    headers = {
        'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'bid=L3EaSz2ZpcA; douban-fav-remind=1; __gads=ID=14b7d1ccb108d622-22630ab795e100fc:T=1685371712:RT=1685371712:S=ALNI_MYGLjcksiqOCyCstJTEiZ6ILmVPaA; __gpi=UID=00000c0c52dd8934:T=1685371712:RT=1685371712:S=ALNI_MbEyFjJheO9TXvEr8_1JBloPhbwIg; viewed="30695339_26633121"; __utma=30149280.1442114512.1694053706.1694053706.1694053706.1; __utmz=30149280.1694053706.1.1.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; ll="118220"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1699713075%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D8RlsSuzblBcTQ7SB2uJ0uF7QWXFKXwXImCgxjJYT98Pj9T5IVLToYZk4Jyv6jokZ%26wd%3D%26eqid%3Ddaba94920046ccbe00000002654f9030%22%5D; _pk_id.100001.4cf6=9a9006ff2303ee07.1699713075.; _pk_ses.100001.4cf6=1; ap_v=0,6.0',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',
        'Sec-Ch-Ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # 包装url
    request = urllib.request.Request(url=url, headers=headers)
    # 获取响应
    response = urllib.request.urlopen(request)
    # 获取内容
    content = response.read().decode('utf-8')
    #
    with open(f'./doban{i}.json', 'w', encoding='utf-8') as f:
        f.write(content)