import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.base_url = 'https://cloud-api.yandex.net'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)
        params = {
            'path': file_name,
            'overwrite': 'true'
        }
        with open(file_path, 'rb') as f:
            resp = requests.get(self.base_url + f'/v1/disk/resources/upload',
                                params=params,
                                headers=self.get_headers())
            try:
                return requests.post(resp.json()['href'], files={'file': f})
            except KeyError:
                return resp.json()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'superhero.py'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)

