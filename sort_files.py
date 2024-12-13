file_list = ['1.txt', '2.txt', '3.txt']
files = []
for file in file_list:
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
        if data[-1] == '':
            data = data[:-1]
        current_file = (
            {'file_name': f.name,
            'lines': len(data),
            'text': data}
        )
        files.append(current_file)
sorted_files = sorted(files, key=lambda x: x['lines'])
for file in sorted_files:
    with open(('result.txt'), 'a', encoding='utf-8') as f:
        f.write(
            f'{file['file_name']}\n'
            f'{file['lines']}\n'
            f'{"\n".join(file['text'])}\n\n'
        )