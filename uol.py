import requests, bs4, utils


def request_uol():
    res = requests.get('https://noticias.uol.com.br/')
    r_soup = bs4.BeautifulSoup(res.text, "html.parser")
    elem_all_news = r_soup.select('.titulo')  #all news
    return elem_all_news

def get_all_news(elems_all_news):
    list_all_news = []
    for new in elems_all_news:
        if (not new.contents is None) and (len(new.contents) > 0):
            new_formatted = str(new.contents[0])
            new_formatted.strip()
            if(new_formatted not in list_all_news) and (not 'envie fotos' in new_formatted.lower()):
                list_all_news.append(new.contents[0])
    return list_all_news

def print_uol_news():
    elem_all_news = request_uol()
    elem_all_news = get_all_news(elem_all_news)
    utils.print_all_news(elem_all_news)