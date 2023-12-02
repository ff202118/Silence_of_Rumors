'''
    comment.py 为了 news.json 中各新闻的 评论
    1. 先提取 commentUrl 至 commentUrl_order.txt、commentUrl_rom.txt
    2. 将 commentUrl_rom.txt 放置采集器中 提取评论数据 至 comments.xlsx
    3. 将 comments.xlsx 转至 comments.json
'''
import json
import re
import pandas as pd

'''
    预处理得到txt
'''
with open('../news/news.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

cnt = 0
# 使用正则表达式判断是否是合法的URL
pattern = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')

with open('commentUrl_order.txt', 'w', encoding='utf-8') as f, open('commentUrl_rom.txt', 'w', encoding='utf-8') as fp:
    for item in data:
        cnt += 1
        item['id'] = cnt
        path = str(item['commentUrl'])
        if re.match(pattern, path):
            f.write(str(cnt)+' '+path+'\n')
            fp.write(path+'\n')


'''
    根据上面的 txt 先采集到 xlsx 后，得到json，分为 热评 和 新评
'''
# 读取 Excel 文件
excel_file = 'comments.xlsx'  # 替换为你的 Excel 文件路径

df1 = pd.read_excel(excel_file, sheet_name='sheet1')
df2 = pd.read_excel(excel_file, sheet_name='sheet2')

# 将 DataFrame 转换为 JSON 字符串
json_data1 = df1.to_json(orient='records', lines=True)
json_data2 = df2.to_json(orient='records', lines=True)
# 将 JSON 字符串写入文件
json_file1 = 'hot_comments.json'  # 替换为你希望保存的 JSON 文件路径
json_file2 = 'new_comments.json'

with open(json_file1, 'w', encoding='utf-8') as f:
    f.write(json_data1)

# 转出来的是一个个字典，可能会报错，后续需把它转成列表
# 读取原始 JSON 文件
with open(json_file1, 'r', encoding='utf-8') as f:
    json_data = [json.loads(line) for line in f]

# 将列表形式的数据保存到新的 JSON 文件
with open(json_file1, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

with open(json_file2, 'w', encoding='utf-8') as f:
    f.write(json_data2)

# 转出来的是一个个字典，可能会报错，后续需把它转成列表
# 读取原始 JSON 文件
with open(json_file2, 'r', encoding='utf-8') as f:
    json_data = [json.loads(line) for line in f]

# 将列表形式的数据保存到新的 JSON 文件
with open(json_file2, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print(f"Excel 文件内容已成功保存为 JSON 文件: {json_file1}")
print(f"Excel 文件内容已成功保存为 JSON 文件: {json_file2}")