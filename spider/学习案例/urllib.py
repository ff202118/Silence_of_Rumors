# import urllib.request
#
# # case 1
#
# # url = 'http://www.baidu.com'
# # response = urllib.request.urlopen(url)
# # content = response.read().decode('utf-8')
# # print(content)
#
#
# # case 2---------------------------------------
#
# # print(type(response))
# # content = response.readlines()
# # print(content)
# # print(response.getcode())
# # print(response.geturl())
# # print(response.getheaders())
#
# # case 3---------------------------------------
#
# # 下载东西
# # urllib.request.urlretrieve(url, 'baidu.html')
#
# # case 4---------------------------------------
# # url = 'https://www.baidu.com'
# # response = urllib.request.urlopen(url)
# # content = response.read().decode('utf-8')
# # print(content)
#
#
# # headers = {
# #     'User-Agent': 'xxx'
# # }
# # request = urllib.request.Request(url=url, headers=headers)
# # response = urllib.request.urlopen(request)
# # content = response.read().decode('utf-8')
# # print(content)
#
# # case 5-----------------------------------------
#
# name = urllib.parse.quote('周杰伦')
# # print(name)
#
# data={
#     'name': '周杰伦',
#     # 'sex': '男',
#     # 'location': '中国台湾'
# }
#
# base_url = 'http://www.baidu.com/s?'
# new_data = urllib.parse.urlencode(data)
#
# index = base_url + new_data
#
# headers = {
#      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.50',
#      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#      'cookie': 'BIDUPSID=C76DD892B25E75A57C1D344DA490FD92; PSTM=1692507137; BAIDUID=C76DD892B25E75A5E8C6BA61389BD10B:FG=1; BD_UPN=12314753; ispeed_lsm=2'
#                '; H_WISE_SIDS=110085_275732_259642_278054_278574_274779_278388_279998_280227_278414_280810_280558_278791_280636_255879_281043_280633_281'
#                '235_277970_281147_279203_281393_280437_281520_279045_280650_281725_281150_281810_280169_281865_267170_281886_281830_278816_279711_282196'
#                '_281050_279010_282664_282665; BA_HECTOR=84a18ha4a4a42g85a081a1221ikprrl1q; BAIDUID_BFESS=C76DD892B25E75A5E8C6BA61389BD10B:FG=1; ZFY=vsc2'
#                'KPofKpn:ACKqQ6yMV7uzd1TKFilTa:ASKWFaP6p5E:C; BDRCVFR[kSyA9a8U-kc]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; H_PS_PSSID=39635_39669_39663_39687_'
#                '39692; PSINO=2; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=3959GBJI3j%2B5OlWk5orOXBDSVW8Tx8EsbDaqEVoa2TTSEE5osF%2FnXnAs2MYgxZ%2F0'
#                's97lXpaEoLw; BDSVRTM=0; COOKIE_SESSION=14_0_3_3_20_4_1_0_3_1_0_0_43_0_35_0_1699543762_0_1699543727%7C9%23111595_18_1699372693%7C3; ZD_ENT'
#                'RY=baidu; shifen[551408403894_18013]=1699543766; BCLID=10778840821467425121; BCLID_BFESS=10778840821467425121; BDSFRCVID=oV8OJeCAaR2PnQ5q'
#                'EXhe-EaJqeKK0gOTH6ONHBIWHKgUupCVfnYIEG0PPf8g0Ku-S2-sogKKymOTHrDF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=oV8OJeCAaR2PnQ5qEXhe-EaJqeKK0'
#                'gOTH6ONHBIWHKgUupCVfnYIEG0PPf8g0Ku-S2-sogKKymOTHrDF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC-htKv0jbTg-tP_-4_tbh_X5-RLfKOpVp7F5lON'
#                'Hf_40-TGjJ_kWM7-exQKWj6-ahkM5h7xOKQOXx7Iyq-nyUJP-ROmQDcXhlTN3KJmVbL9bT3v5Du9Dmce2-biW55L2Mbd-qbP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-Tr'
#                '0eaDDtMK; H_BDCLCKID_SF_BFESS=tRAOoC-htKv0jbTg-tP_-4_tbh_X5-RLfKOpVp7F5lONHf_40-TGjJ_kWM7-exQKWj6-ahkM5h7xOKQOXx7Iyq-nyUJP-ROmQDcXhlTN3KJmV'
#                'bL9bT3v5Du9Dmce2-biW55L2Mbd-qbP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-Tr0eaDDtMK'
# }
#
# request = urllib.request.Request(url=index, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
#
# import json
# obj = json.loads(content)
# print(obj)
#
# case 6---------------------------------------------------------------------------------

# import urllib.request
#
# url = 'http://www.baidu.com/s?'
# headers = {
#      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.50',
#      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#      'cookie': 'BIDUPSID=C76DD892B25E75A57C1D344DA490FD92; PSTM=1692507137; BAIDUID=C76DD892B25E75A5E8C6BA61389BD10B:FG=1; BD_UPN=12314753; ispeed_lsm=2'
#                '; H_WISE_SIDS=110085_275732_259642_278054_278574_274779_278388_279998_280227_278414_280810_280558_278791_280636_255879_281043_280633_281'
#                '235_277970_281147_279203_281393_280437_281520_279045_280650_281725_281150_281810_280169_281865_267170_281886_281830_278816_279711_282196'
#                '_281050_279010_282664_282665; BA_HECTOR=84a18ha4a4a42g85a081a1221ikprrl1q; BAIDUID_BFESS=C76DD892B25E75A5E8C6BA61389BD10B:FG=1; ZFY=vsc2'
#                'KPofKpn:ACKqQ6yMV7uzd1TKFilTa:ASKWFaP6p5E:C; BDRCVFR[kSyA9a8U-kc]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; H_PS_PSSID=39635_39669_39663_39687_'
#                '39692; PSINO=2; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=3959GBJI3j%2B5OlWk5orOXBDSVW8Tx8EsbDaqEVoa2TTSEE5osF%2FnXnAs2MYgxZ%2F0'
#                's97lXpaEoLw; BDSVRTM=0; COOKIE_SESSION=14_0_3_3_20_4_1_0_3_1_0_0_43_0_35_0_1699543762_0_1699543727%7C9%23111595_18_1699372693%7C3; ZD_ENT'
#                'RY=baidu; shifen[551408403894_18013]=1699543766; BCLID=10778840821467425121; BCLID_BFESS=10778840821467425121; BDSFRCVID=oV8OJeCAaR2PnQ5q'
#                'EXhe-EaJqeKK0gOTH6ONHBIWHKgUupCVfnYIEG0PPf8g0Ku-S2-sogKKymOTHrDF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=oV8OJeCAaR2PnQ5qEXhe-EaJqeKK0'
#                'gOTH6ONHBIWHKgUupCVfnYIEG0PPf8g0Ku-S2-sogKKymOTHrDF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC-htKv0jbTg-tP_-4_tbh_X5-RLfKOpVp7F5lON'
#                'Hf_40-TGjJ_kWM7-exQKWj6-ahkM5h7xOKQOXx7Iyq-nyUJP-ROmQDcXhlTN3KJmVbL9bT3v5Du9Dmce2-biW55L2Mbd-qbP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-Tr'
#                '0eaDDtMK; H_BDCLCKID_SF_BFESS=tRAOoC-htKv0jbTg-tP_-4_tbh_X5-RLfKOpVp7F5lONHf_40-TGjJ_kWM7-exQKWj6-ahkM5h7xOKQOXx7Iyq-nyUJP-ROmQDcXhlTN3KJmV'
#                'bL9bT3v5Du9Dmce2-biW55L2Mbd-qbP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-Tr0eaDDtMK'
# }
# # 获取request
# request = urllib.request.Request(url=url, headers=headers)
# # 获取handler
# handler = urllib.request.HTTPhandler()
# # 获取opener
# opener = urllib.request.build_opener(handler)
# # 调用opener
# response = opener.open(request)

# case 7--------------------------------------------------------------------
import urllib.request
import random

url = 'http://www.baidu.com/s?'
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.50',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
     'cookie': 'BIDUPSID=C76DD892B25E75A57C1D344DA490FD92; PSTM=1692507137; BAIDUID=C76DD892B25E75A5E8C6BA61389BD10B:FG=1; BD_UPN=12314753; ispeed_lsm=2'
               '; H_WISE_SIDS=110085_275732_259642_278054_278574_274779_278388_279998_280227_278414_280810_280558_278791_280636_255879_281043_280633_281'
               '235_277970_281147_279203_281393_280437_281520_279045_280650_281725_281150_281810_280169_281865_267170_281886_281830_278816_279711_282196'
               '_281050_279010_282664_282665; BA_HECTOR=84a18ha4a4a42g85a081a1221ikprrl1q; BAIDUID_BFESS=C76DD892B25E75A5E8C6BA61389BD10B:FG=1; ZFY=vsc2'
               'KPofKpn:ACKqQ6yMV7uzd1TKFilTa:ASKWFaP6p5E:C; BDRCVFR[kSyA9a8U-kc]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; H_PS_PSSID=39635_39669_39663_39687_'
               '39692; PSINO=2; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=3959GBJI3j%2B5OlWk5orOXBDSVW8Tx8EsbDaqEVoa2TTSEE5osF%2FnXnAs2MYgxZ%2F0'
               's97lXpaEoLw; BDSVRTM=0; COOKIE_SESSION=14_0_3_3_20_4_1_0_3_1_0_0_43_0_35_0_1699543762_0_1699543727%7C9%23111595_18_1699372693%7C3; ZD_ENT'
               'RY=baidu; shifen[551408403894_18013]=1699543766; BCLID=10778840821467425121; BCLID_BFESS=10778840821467425121; BDSFRCVID=oV8OJeCAaR2PnQ5q'
               'EXhe-EaJqeKK0gOTH6ONHBIWHKgUupCVfnYIEG0PPf8g0Ku-S2-sogKKymOTHrDF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=oV8OJeCAaR2PnQ5qEXhe-EaJqeKK0'
               'gOTH6ONHBIWHKgUupCVfnYIEG0PPf8g0Ku-S2-sogKKymOTHrDF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC-htKv0jbTg-tP_-4_tbh_X5-RLfKOpVp7F5lON'
               'Hf_40-TGjJ_kWM7-exQKWj6-ahkM5h7xOKQOXx7Iyq-nyUJP-ROmQDcXhlTN3KJmVbL9bT3v5Du9Dmce2-biW55L2Mbd-qbP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-Tr'
               '0eaDDtMK; H_BDCLCKID_SF_BFESS=tRAOoC-htKv0jbTg-tP_-4_tbh_X5-RLfKOpVp7F5lONHf_40-TGjJ_kWM7-exQKWj6-ahkM5h7xOKQOXx7Iyq-nyUJP-ROmQDcXhlTN3KJmV'
               'bL9bT3v5Du9Dmce2-biW55L2Mbd-qbP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-Tr0eaDDtMK'
}
# 获取request
request = urllib.request.Request(url=url, headers=headers)

proxies_pool = [
    {'http' : '182.34.20.41:9999489421'},
    {'http' : '182.34.20.41:9999498915'},
    {'http' : '182.34.20.41:9999113516'},
]
proxies = random.choice(proxies_pool)
print(proxies)
# 获取handler
handler = urllib.request.ProxyHandler(proxies=proxies)
# 获取opener
opener = urllib.request.build_opener(handler)
# 调用opener
response = opener.open(request)

content = response.read().decode('utf-8')
print(content)