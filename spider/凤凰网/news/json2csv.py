import json
import csv


def json_to_csv(json_data, csv_file):
    # 从 JSON 字符串中加载数据
    data = json.loads(json_data)

    # 获取 CSV 文件的头部（列名）
    header = list(data[0].keys())

    # 打开 CSV 文件进行写入
    with open(csv_file, 'w', newline='', encoding='utf') as csvfile:
        # 创建 CSV 写入器对象
        csv_writer = csv.DictWriter(csvfile, fieldnames=header)

        # 写入头部
        csv_writer.writeheader()

        # 写入数据
        csv_writer.writerows(data)


# 示例 JSON 数据
with open('news.json', 'r', encoding='utf-8') as f:
    json_data = f.read()
# print(json_data)
# 指定 CSV 文件名
csv_file_name = 'news.csv'

# 将 JSON 转换为 CSV
json_to_csv(json_data, csv_file_name)

print(f'Conversion complete. CSV file saved as {csv_file_name}')
