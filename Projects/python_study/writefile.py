data = ['1.txt', '2.txt', '3.txt']

def new_file(files: list):
    list_of_lines = []
    for doc in data:
        with open(doc, encoding='utf-8') as file:
            new_list = file.readlines()
            new_list.insert(0, str(len(new_list)))
            new_list.insert(0, doc)
            list_of_lines += [new_list]
    list_of_lines = sorted(list_of_lines, key=len)
    with open('new_file.txt', 'wt', encoding='utf-8') as file:
        for lines in list_of_lines:
            for line in lines:
                line = line.strip()
                file.write(line + '\n')

new_file(data)