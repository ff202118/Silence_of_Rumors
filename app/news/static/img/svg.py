from bs4 import BeautifulSoup

def svg(string):
    # 读取 SVG 文件内容
    with open(f'{string}.svg', 'r', encoding='utf-8') as f:
        svg_content = f.read()

    # 使用 BeautifulSoup 解析 SVG 文件内容
    soup = BeautifulSoup(svg_content, 'xml')

    # 提取所有 <path> 标签，并获取其 d 属性值
    paths = soup.find_all('path')
    List = []
    for path in paths:
        d_attribute = path.get('d')
        List.append(d_attribute.replace(' ', ','))

    print(' '.join(List))

if __name__ == '__main__':
    # svg('Information')
    # svg('Entertainment')
    # svg('Society')
    # svg('Sports')
    # svg('Technology')
    # svg('Finance')
    # svg('Health')
    # svg('Education')
    # svg('Military')
    svg('Other')