import requests
import os

BASE_URL = 'http://127.0.0.1:8080'
FILENAME = 'photo.jpg'

upload_url = f"{BASE_URL}/upload"

with open(FILENAME, 'rb') as file:
    files = {'image': file}
    response = requests.post(upload_url, files=files)

if response.status_code != 201:
    raise Exception(response.content)

get_url = f"{BASE_URL}/image/{FILENAME}"
headers = {'Content-Type': 'image'}
response = requests.get(get_url, headers=headers)

if response.status_code != 200:
    raise Exception(response.content)

with open(f'new_{FILENAME}', 'wb') as file:
    file.write(response.content)

delete_url = f"{BASE_URL}/delete/{FILENAME}"
response = requests.delete(delete_url)

if response.status_code == 200:
    print('Дані успішно видалено')
else:
    print('Помилка. Статус-код:', response.status_code)
