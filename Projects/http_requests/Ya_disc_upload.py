import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_url (self, file_path: str):
        params = {
            "path": file_path,
            'overwrite': 'true'
        }
        headers = self.get_headers()
        url_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = requests.get(url_for_upload, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str, file_name: str):
        href = self.get_url(file_path=file_path).get('href')
        upload = requests.put(href, data=open(file_name, 'rb'))
        upload.raise_for_status()
        if upload.status_code == 201:
            print("Success")


