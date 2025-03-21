import allure
import pytest
from src import data

class TestCreateCourier:
    @allure.title('Проверка создания курьера с вводом всех корректных данных')
    def test_create_courier(self, create_courier_model):
        create_courier_model.create_couriers(data.create_courier_payload)
        create_courier_model.check_status_code(201)
        create_courier_model.check_user_created()

        # Логинимся под созданным курьером, чтобы получить его ID
        login_payload = {
            "login": data.create_courier_payload["login"],
            "password": data.create_courier_payload["password"]
        }
        response = create_courier_model.login(login_payload)
        courier_id = response.json()["id"]

        # Удаляем созданного курьера
        create_courier_model.delete_courier(courier_id)
        create_courier_model.check_status_code(200)

    @allure.title("Проверка вывода ошибки при создании курьера без логина или пароля")
    @pytest.mark.parametrize('params', ['login', 'password'])
    def test_create_courier_validation_error_on_empty_required_fields(self, params, create_courier_model):
        payload = data.create_courier_payload.copy()
        payload.update({params: None})
        create_courier_model.create_couriers(payload)
        create_courier_model.check_status_code(400)
        create_courier_model.check_registration_error()

    @allure.title('Проверка создания 2х одинаковых курьеров или создания курьера с логином который уже зарегистрирован')
    @pytest.mark.parametrize('payload', [data.created_courier_payload, data.duplicate_login_payload])
    def test_error_on_duplicate_courier_creation(self, payload, create_courier_model):
        create_courier_model.create_couriers(payload)
        create_courier_model.check_status_code(409)
        create_courier_model.check_duplicate_login_error()
