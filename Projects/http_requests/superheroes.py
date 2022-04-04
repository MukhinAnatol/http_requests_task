import requests
from pprint import pprint
Token = '2619421814940190'

class Superhero_searcher:
    def __init__(self, token):
        self.token = token

    def find_hero_id(self, hero_name: str):
        url = f'https://superheroapi.com/api/{self.token}/search/{hero_name}'
        response = requests.get(url)
        result = response.json()
        list = result['results']
        #pprint(list)
        for item in list:
            for key, value in item.items():
                if 'id' == key:
                    pprint(item['id'])
                    return item['id']

    def get_hero_stats(self, hero_name: str, stat):
        url = f'https://superheroapi.com/api/{self.token}/{self.find_hero_id}/powerstats/{stat}'
        response = requests.get(url)
        result = response.json()
        pprint(result)
        return result

    #def find_superhero_stats(self, ):

Searcher = Superhero_searcher(Token)
Searcher.find_hero_id('Hulk')
Searcher.get_hero_stats('Hulk', 'Intelligence')

#.find_superhero_id('Captain America')
#Searcher.find_superhero_id('Thanos')

