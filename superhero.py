import requests


def get_smartest_hero(heroes):
    url = 'https://akabab.github.io/superhero-api/api'
    intelligent = len(heroes) * [0]
    all_heroes = requests.get(url + f'/all.json').json()
    sorted_heroes = max(filter(lambda hero: hero['name'] in heroes, all_heroes),
                        key=lambda x: x['powerstats']['intelligence'])
    return sorted_heroes['name']


if __name__ == '__main__':
    superheros = ['Hulk', 'Captain America', 'Thanos']
    print(get_smartest_hero(superheros))

