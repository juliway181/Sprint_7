from settings import Base_params
import allure
import requests


class BaseModel(Base_params):

    def __init__(self, response):
        self.response = response

    def post_method(self, endpoint, **kwargs):
        self.response = requests.post(f"{self.url}{endpoint}", **kwargs)
        return self.response

    def get_method(self, endpoint, **kwargs):
        self.response = requests.get(f"{self.url}{endpoint}", **kwargs)
        return self.response

    @allure.step("Получаем тело ответа")
    def get_response_body(self):
        return self.response.json()

    @allure.step("Проверяем статус код")
    def check_status_code(self, code):
        print("Response Status Code:", self.response.status_code)
        print("Response Body:", self.response.text)
        assert self.response.status_code == code

    @allure.step("Получаем сообщение об ошибке")
    def get_error_msg(self):
        message = self.response.json()['message']
        return message

    def get_value_by_keys(self, *args):
        """
           Получает значение из JSON-ответа, используя любое количество ключей и индексов.

           :param args: последовательность ключей и/или индексов для доступа к вложенным элементам
           :return: значение из JSON-ответа или None, если ключ не найден
        """

        try:
            json_data = self.response.json()

            result = json_data
            for arg in args:
                if isinstance(result, dict): # Если текущий элем, словарь то пытаемсся получить значение по ключу
                    result = result[arg]
                elif isinstance(result, list) and isinstance(arg, int):  # Если текущий элем список то пытаемсся получить значение по индексу
                    result = result[arg]
                else:
                    raise ValueError(f"Неверный тип данных или недопустимый ключ/индекс: {arg}")
            return result
        except (KeyError, IndexError, ValueError) as e:
            print(f'Ошибка: {str(e)}')
            return None

    def extract_keys(self, extract_body):
        keys = ", ".join(extract_body)
        print(f"Ключи: {keys}")
        return keys