import requests, bs4, utils


def request_ig():
    res = requests.get('http://ultimosegundo.ig.com.br/')
    r_soup = bs4.BeautifulSoup(res.text, "html.parser")
    elem_all_news = r_soup.select('.ig-component-title')  #all news
    return elem_all_news

def get_all_news(elem_all_news):
    list_formatted_news = []
    for n in elem_all_news:
        if len(elem_all_news) > 0:
            title = str(n.contents[0])
            list_formatted_news.append(title)
    return list_formatted_news

def print_ig_news():
    elem_all_news = request_ig()
    elem_all_news = get_all_news(elem_all_news)
    utils.print_all_news(elem_all_news)