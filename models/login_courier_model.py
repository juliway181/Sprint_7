import allure
from src import data, helper
from models.base_model import BaseModel


class LoginCourierAPI(BaseModel):

    @allure.step(f"Отправляем POST запрос на ручку {data.login_courier_point}")
    def login_courier(self, payloads):
        self.post_method(data.login_courier_point, json=payloads)

    @allure.step("Проверяем id пользователя")
    def check_login_successfully(self):
        assert self.get_response_body()['id'] == 427259

    @allure.step("Проверяем сообщение об ошибке Недостаточно данных для входа")
    def check_authorization_error(self):
        assert self.get_error_msg() == "Недостаточно данных для входа"

    @allure.step("Проверяем сообщение об ошибке Учетная запись не найдена")
    def check_user_not_found_error(self):
        assert self.get_error_msg() == "Учетная запись не найдена"

    @allure.step('Получаем id пользователя')
    def get_user_id(self):
        helper.register_new_courier_and_return_login_password()
        user_id = self.get_value_by_keys('id')
        return user_id