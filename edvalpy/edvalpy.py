import os
import requests
from io import BytesIO
from zipfile import ZipFile
from .helpers.dates import get_sync_dates


class Sync:
    def __init__(self, config, session):
        self.zip = None
        self.name = config["sisCode"]
        self._config = config
        self._session = session
        self._base_download_url = "https://my.edval.education/files/{}"
        self._base_url = "https://my.edval.education/api/v1/daily/syncBasic/1"

    def __repr__(self):
        return f"{self._config['sisCode']} ({self._config['syncConfigCode']})"

    def __str__(self):
        return self._config["sisCode"]

    def download(self):
        resp = self._session.post(
            self._base_url.format(self._config["syncConfigCode"]), data=get_sync_dates()
        )
        if resp.json().get("data"):
            zip_file = self._session.get(
                self._base_download_url.format(resp.json()["data"]["id"]),
                data=get_sync_dates(),
            )
            self.zip = ZipFile(BytesIO(zip_file.content))

    def files(self):
        if not self.zip:
            self.download()
        if self.zip:
            return self.zip.namelist()

    def get_file(self, file_name):
        if not self.zip:
            self.download()
        with self.zip.open(file_name) as my_file:
            return BytesIO(my_file.read())

    def save_file(self, file_name, file_path=None):
        my_file = self.get_file(file_name)
        if not file_path:
            file_path = os.getcwd()
        if my_file:
            with open(os.path.join(file_path, file_name), "wb") as f:
                f.write(my_file.getvalue())


class Edval:
    def __init__(self, token):
        self._login_url = "https://my.edval.education/api/auth/login"
        self._configs_url = "https://my.edval.education/api/v1/daily/sync/configs"
        self.session = requests.session()
        self.login(token)
        self.get_configs()

    def __getattr__(self, key):
        return [c for c in self.configs if c.name == key][0]

    def login(self, token):
        data = {"webCode": token, "rememberMe": "false"}
        req = self.session.post(self._login_url, json=data)
        return req

    def get_configs(self):
        req = self.session.get(self._configs_url)
        self._configs = req.json()["data"]

    @property
    def configs(self):
        return [Sync(config, self.session) for config in self._configs]


if __name__ == "__main__":
    pass
