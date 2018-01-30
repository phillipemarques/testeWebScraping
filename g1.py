import requests, bs4, utils


def request_g1():
    res = requests.get('http://g1.globo.com/')
    r_soup = bs4.BeautifulSoup(res.text, "html.parser")
    elem_all_news = r_soup.select('.gui-color-primary')  #all news
    return elem_all_news

def is_trash(text):
    if ('mande seu vídeo' or 'envie seu vídeo' or 'previsão do tempo') in text.lower():
        return True
    if text.isspace():
        return True
    return False

def get_all_news(elems_all_news):
    list_formatted_news = []
    for n in elems_all_news:
        if len(n.contents) > 0:
            title = str(n.contents[0])
            formatted_title = title.strip()
            if (not formatted_title in list_formatted_news) and ('card-opiniao-quote-subtitle' not in formatted_title)\
                    and (not is_trash(formatted_title)):
                list_formatted_news.append(formatted_title)
    return list_formatted_news

def print_g1_news():
    elemAllNews = request_g1()
    elemAllNews = get_all_news(elemAllNews)
    utils.print_all_news(elemAllNews)