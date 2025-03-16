import os
from dotenv import load_dotenv


# Загрузить переменные окружения из файла .env
class Base_params():

    load_dotenv()
    url = os.getenv("URL")

    @property
    def dev_url(self):
        return Base_params.url