import allure
from src import data as data
from models.base_model import BaseModel


class CreateCouriersAPI(BaseModel):

    @allure.step(f"Отправляем POST запрос на ручку {data.create_courier_point}")
    def create_couriers(self, payloads):
        self.post_method(data.create_courier_point, data=payloads)

    @allure.step("Проверяем сообщение о успешном создании пользователя")
    def check_user_created(self):
        assert self.get_response_body() == {"ok":True}

    @allure.step("Проверяем сообщение об ошибке")
    def check_registration_error(self):
        assert self.get_error_msg() == "Недостаточно данных для создания учетной записи"

    @allure.step("Проверяем сообщение об ошибке")
    def check_duplicate_login_error(self):
        assert self.get_error_msg() == "Этот логин уже используется. Попробуйте другой."