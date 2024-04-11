import re
from sqlalchemy import func, cast, Date
from project import db
import pickle as pkl

def get_post_list(post_list):
    Post_list = []

    for post in post_list:
        Post_Dict = {}

        Post_Dict['title'] = post.title
        Post_Dict['content'] = post.content[:250] + '......'
        Post_Dict['date'] = post.date
        Post_Dict['source'] = post.source
        Post_Dict['source_url'] = post.source_url
        Post_Dict['detail_url'] = post.detail_url
        Post_Dict['rate'] = post.rate

        content_list = post.follow_content.split('\t')
        follow_link = post.follow_link.split('\t')
        follow_title = []
        date_list = []
        for idx, text in enumerate(content_list):
            pattern1 = r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}.+'
            match1 = re.search(pattern1, text)

            pattern2 = r'([^：]+)：'
            match2 = re.search(pattern2, text)

            try:
                text = text.replace(match1.group(), '')
                text = text.replace(match2.group(1), '')

                text = text[:200] + '...'
                text = text.strip()

                date_list.append(match1.group().strip())

                content_list[idx] = text.strip()

                follow_title.append(match2.group(1).strip())
            except:
                pass

        Post_Dict['follows'] = zip(follow_title, content_list, follow_link, date_list)
        Post_list.append(Post_Dict)

    return Post_list

def get_news_data(database):

    news_by_date = db.session.query(
        cast(database.date, Date).label('date'),
        func.count(database.id).label('count')
    ).group_by(cast(database.date, Date)).all()

    news_count = [row.count for row in news_by_date]
    news_date = [row.date.strftime('%Y-%m') for row in news_by_date]
    news_data = sorted(zip(news_date, news_count), key=lambda x: x[0])

    inp = len(news_data)//11
    print(inp)
    news_count = []
    news_date = []
    for index, (date, count) in enumerate(news_data):
        if index % inp == 0:
            data_list = news_data[index:index+inp]
            news_date.append(date)
            news_count.append(sum([count for date, count in data_list]))

    # print(news_date)
    # print(news_count)
    return news_date, news_count


def get_weight(cate):
    word_weight = []
    with open(f'app/news/static/temp/word_weight_{cate}.pkl', 'rb') as f:
        data = pkl.load(f)

    for doc_index, doc_keywords_weights in enumerate(data):
        for keyword, weight in doc_keywords_weights:
            word_weight.append({'name': keyword, 'value': weight * 100})

    return word_weight