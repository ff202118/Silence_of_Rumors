import pandas as pd
import json

# 读取JSON文件
with open('news.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 将JSON数据转换为DataFrame
df = pd.json_normalize(data)

# 将DataFrame写入Excel文件
df.to_excel('news.xlsx', index=False)
