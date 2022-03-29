data = []
def write_file(file_name: str, text: str):
    with open(file_name, 'w', encoding='utf-8' ) as file:
        file.write(text)

write_file('data.txt',   )