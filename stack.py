import requests
from datetime import datetime, timedelta
from pprint import pprint


def get_questions(date_from, date_to, tags):
    base_url = 'https://api.stackexchange.com/'
    params = {
        'order': 'desc',
        'sort': 'activity',
        'tagged': tags,
        'site': 'stackoverflow',
        'fromdate': str(int(datetime.timestamp(date_from))),
        'todate': str(int(datetime.timestamp(date_to)))
    }
    resp = requests.get(base_url + f'/2.3/search/advanced', params=params)
    return resp.json()


if __name__ == '__main__':
    today = datetime.today()
    two_days_before = today - timedelta(days=2)

    get_questions(two_days_before, today, 'Python')
    pass
