'''
    对采集器收集到的 raw.xlsx 进行预处理 得到 news.json
'''
import json
import pandas as pd

# 读取 Excel 文件
excel_file = 'raw.xlsx'  # 替换为你的 Excel 文件路径
df = pd.read_excel(excel_file)

# 将 DataFrame 转换为 JSON 字符串
json_data = df.to_json(orient='records', lines=True)

# 将 JSON 字符串写入文件
json_file = 'news.json'  # 替换为你希望保存的 JSON 文件路径
with open(json_file, 'w', encoding='utf-8') as f:
    f.write(json_data)


# 转出来的是一个个字典，可能会报错，后续需把它转成列表
# 读取原始 JSON 文件
with open(json_file, 'r', encoding='utf-8') as f:
    json_data = [json.loads(line) for line in f]

# 将列表形式的数据保存到新的 JSON 文件
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)


print(f"Excel 文件内容已成功保存为 JSON 文件: {json_file}")


