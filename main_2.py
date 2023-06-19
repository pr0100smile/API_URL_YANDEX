import requests
import os

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        up_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": "TestAPI/MacOS.jpg", "overwrite": "True"}
        response = requests.get(up_url, headers=headers, params=params).json()
        url_for_upload = response.get('href', '')
        response2 = requests.put(url_for_upload, data=open(file_path, 'rb'))
        response2.raise_for_status()
        if response2.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {response2.status_code}"

if __name__ == '__main__':
    path_to_file = os.path.abspath('MacOS.jpg')
    token = 'OAuth CENSORED' #Токен
    uploader = YaUploader(token)
    print(f"Загружаем файл {path_to_file} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)

