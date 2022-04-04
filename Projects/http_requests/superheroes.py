import requests
from pprint import pprint

class Superhero:
    def __init__(self, hero_name, token):
        self.hero_name = hero_name
        self.token = token

    def get_hero_stat(self):
        url = f'https://superheroapi.com/api/{self.token}/search/{self.hero_name}'
        response = requests.get(url)
        result = response.json()['results'][0]
        #pprint(result)
        hero_stat = 'intelligence'
        stat = result['powerstats'][hero_stat]
        #pprint(stat)
        return stat

    def compare_stat(self, heroes_list: list):
        heroes_stats = {}
        stat = self.get_hero_stat()
        heroes_stats[self.hero_name] = int(stat)
        for hero in heroes_list:
            if isinstance(hero, Superhero):
                heroes_stats[hero.hero_name] = int(hero.get_hero_stat())
                max_val = list(max(heroes_stats.items(), key=lambda x: x[1]))
                return f'{max_val[0]} - самый умный герой с показателем интелекта {max_val[1]}.'



