# # '''
# #     raw.xlsx 为采集器所采集
# #     process.py主要为了把xlsx变成json格式，位于后续处理
# # '''
# # import json
# # import pandas as pd
# #
# # # 读取 Excel 文件
# # excel_file = 'raw.xlsx'  # 替换为你的 Excel 文件路径
# # df = pd.read_excel(excel_file)
# #
# # # 将 DataFrame 转换为 JSON 字符串
# # json_data = df.to_json(orient='records', lines=True)
# #
# # # 将 JSON 字符串写入文件
# # json_file = 'info.json'  # 替换为你希望保存的 JSON 文件路径
# # with open(json_file, 'w', encoding='utf-8') as f:
# #     f.write(json_data)
# #
# #
# # # 转出来的是一个个字典，可能会报错，后续需把它转成列表
# # # 读取原始 JSON 文件
# # with open(json_file, 'r', encoding='utf-8') as f:
# #     json_data = [json.loads(line) for line in f]
# #
# # # 将列表形式的数据保存到新的 JSON 文件
# # with open(json_file, 'w', encoding='utf-8') as f:
# #     json.dump(json_data, f, indent=2, ensure_ascii=False)
# #
# #
# # print(f"Excel 文件内容已成功保存为 JSON 文件: {json_file}")
#
#
# import pandas as pd
#
# List = ['1', '2', '3', '4', '5']
# df = pd.read_excel('谣言.xlsx')
#
# Link = []
# Content = []
# for i in range(len(df)):
#     link = []
#     content = []
#     for j in List:
#         strlink = df.loc[i, j + '_link']
#         strcont = df.loc[i, j + '_content']
#
#         if not pd.isna(strlink):
#             link.append(strlink)
#             content.append(strcont)
#         else:
#             break
#
#     Link.append('\t'.join(link))
#     Content.append('\t'.join(content))
#
#
# data = {}
#
# data['follow_link'] = Link
# data['follow_content'] = Content
#
# df2 = pd.DataFrame(data)
# df2.to_excel('example.xlsx', index=False)
import pandas as pd

names = [
    "方家琪", "赵伊诺", "司洪凯", "樊承鑫", "黄培钧",
    "田佳翠", "孙程程", "刘馨灿", "马萱颖", "崔硕",
    "张凯伦", "郭佳鑫", "祝锦康", "谢飞", "王丹阳",
    "亓欣豪", "罗扬", "邹晓琳", "张珂", "石慧琴",
    "张炳毅", "李业", "郭聪", "郝宏洋", "鲁鹏飞",
    "任衍利", "陈长翎", "赵梓壮", "孔浩", "高光宇",
    "商壬午", "梁育东", "余永峰", "卢法伟", "温福洪",
    "鉴思远", "高甲第", "刘笑", "孙宇成"
]
# 加载Excel文件
df = pd.read_excel('二类赛国省奖汇总表.xlsx')

Dict = {}
# matches = df[df.apply(lambda row: "赵伊诺" in str(row), axis=1)]

for name in names:
    matches = df[df.apply(lambda row: name in str(row), axis=1)]
    if matches is None:
        continue
    List =[]
    for competition, rank, date in zip(matches['赛事名称'], matches['获奖情况'], matches['获奖日期']):
        List.append(competition + '  ' + rank + '  ' + str(date))
    Dict[name] = List

# print(matches)
print(Dict)

string = ''
for key, val in Dict.items():
    string += '\n' + key + '\n'
    for competition in val:
         string += competition + '\n'

with open('个人奖项 2023.txt', 'w', encoding='utf-8') as f:
    f.write(string)