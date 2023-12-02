import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://news.ifeng.com/'
driver.get(url)

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

xpath_expression = "//h2[contains(@class, 'news-stream-newsStream-news-item-title')]/a"
elements = driver.find_elements(By.XPATH, xpath_expression)
# 遍历找到的元素并点击
for element in elements:
    element.click()
element = driver.find_element(By.CLASS_NAME, "news-stream-basic-more")
print(element.text)

driver.quit()