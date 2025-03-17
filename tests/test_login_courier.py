import allure
import pytest
from src import data, helper


class TestLoginCourier:

    @allure.title("Проверка логина с вводом всех корректных данных")
    def test_login_courier(self, login_courier_model):
        login_courier_model.login_courier(data.login_payload)
        login_courier_model.check_status_code(200)
        login_courier_model.check_login_successfully()

    @allure.title("Проверка вывода ошибки при авторизации курьера без логина")
    def test_login_courier_validation_error_on_empty_required_login(self, login_courier_model):
        payload = data.login_payload.copy()
        payload.update({"login": None})
        login_courier_model.login_courier(payload)
        login_courier_model.check_status_code(400)
        login_courier_model.check_authorization_error()

    @allure.title("Проверка вывода ошибки при авторизации курьера без пароля")
    def test_login_courier_validation_error_on_empty_required_password(self, login_courier_model):
        payload = data.login_payload.copy()
        payload.update({"password": None})
        login_courier_model.login_courier(payload)
        login_courier_model.check_status_code(504)

    @allure.title("Проверка вывода ошибки при авторизации курьера с не верными логином и паролем")
    @pytest.mark.parametrize('params', ['login', 'password'])
    def test_invalid_login_or_password_returns_error(self, params, login_courier_model):
        payload = data.login_payload.copy()
        payload.update({params: helper.generate_random_string(7)})
        login_courier_model.login_courier(payload)
        login_courier_model.check_status_code(404)
        login_courier_model.check_user_not_found_error()