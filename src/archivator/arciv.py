import os
import zipfile


def arc():
    os.chdir('./data')
    print(os.listdir())

    zip_file = zipfile.ZipFile('Архив содержимого.zip', 'w')

    for root, dirs, files in os.walk('Данные'):
        for file in files:
            zip_file.write(os.path.join(root, file))

    zip_file.close()
    print(os.listdir())

arc()
