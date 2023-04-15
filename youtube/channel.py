import os
from googleapiclient.discovery import build
from config.config import YOUTUBE_ID
import json


class Channel:
    all = []

    def __init__(self, channel_id="default"):
        self.channel_id = channel_id
        self.is_connected = False
        self.channel_name = None
        self.content = None
        self.info = None

    def connect(self):
        """connect with channel and fill self.content"""
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = YOUTUBE_ID
        # создать специальный объект для работы с API
        youtube_build = build('youtube', 'v3', developerKey=api_key)
        if youtube_build:
            self.is_connected = True
            self.content = youtube_build.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self):
        if self.is_connected:
            self.set_info()
            print(self.info)


    def set_info(self):
        if self.is_connected:
            self.info = json.dumps(self.content, indent=2, ensure_ascii=False)

    def get_title(self):
        if self.is_connected:
            print(self.content["items"][0]["snippet"]["title"])



if __name__ == '__main__':
    # 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
    # 'UC5A-Wp9ujcr5g9sYagAafEA'  # Смешарики
    # 'UC1eFXmJNkjITxPFWTy6RsWg'  # Редакция
    ch = Channel('UC5A-Wp9ujcr5g9sYagAafEA')
    ch.connect()
    ch.print_info()
    print("\n ")
    ch.get_title()



