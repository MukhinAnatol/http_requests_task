from pprint import pprint

import requests

from

from Ya_disc_upload import YaUploader

with open('token_ya_disc.txt', 'r') as f:
    Token = f.read().strip()
    print(type(Token))

if __name__ == '__main__':
    path_to_file = 'C:\\Users\docs\photo.jpg'
    file = "test_path/photo.jpg"
    Ya_disk_uploader = YaUploader(Token)
    Ya_disk_uploader.upload(file, path_to_file)