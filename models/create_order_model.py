import allure
from src import data
from models.base_model import BaseModel


class CreateOrderAPI(BaseModel):

    @allure.step(f"Отправляем POST запрос на ручку {data.create_order_point}")
    def create_order(self, payloads):
        self.post_method(data.create_order_point, json=payloads)

    @allure.step("Проверяем наличие ключа 'track'")
    def check_order_is_created(self):
        assert 'track' in self.get_response_body()