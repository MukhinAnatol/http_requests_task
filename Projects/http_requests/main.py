from Ya_disc_upload import YaUploader
from superheroes import Superhero

with open('token_ya_disc.txt', 'r') as f:
    Ya_Token = f.read().strip()


if __name__ == '__main__':
   #Задача №1
    SH_Token = '2619421814940190'
    Hulk = Superhero('Hulk', SH_Token)
    Captain = Superhero('Captain America', SH_Token)
    Thanos = Superhero('Thanos', SH_Token)
    print(Hulk.compare_stat([Captain, Thanos]))
    #Задача №2
    file_on_PC = 'C:\\Users\docs\photo.jpg'
    file_on_disk = "test_path/photo.jpg"
    Ya_disk_uploader = YaUploader(Ya_Token)
    Ya_disk_uploader.upload(file_on_disk, file_on_PC)