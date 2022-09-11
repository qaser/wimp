import random
from urllib.request import urlopen

from bs4 import BeautifulSoup

import utils.constants as const


def scrap_history_day():
    source_site = urlopen(const.URL_HISTORY_DAY)
    soup = BeautifulSoup(source_site.read(), "html.parser")
    events = soup.find_all(class_='masonry-item')
    num_events = len(events)
    random_event_num = random.randint(0, num_events)
    header = soup.find_all(
        class_='masonry-item'
    )[random_event_num].find_all('h3')[0].get_text().replace('\n', '')
    event = soup.find_all(
        class_='masonry-item'
    )[random_event_num].find_all('p')[0].get_text().replace(
        'Читать полностьюОбсудить на форуме',
        '...'
    )
    link = soup.find_all(
        class_='masonry-item'
    )[random_event_num].find_all('a')[0]['href']
    return (
        'Этот день в истории:\n'
        f'{header}.\n'
        f'{event} \n'
        f'Узнать больше: {const.URL_HISTORY_DAY}{link}'
    )
