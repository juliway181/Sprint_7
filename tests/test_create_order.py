import allure
import pytest
from src.data import create_order_payload

class TestCreateOrder:

    @allure.title("Проверка создания заказа")
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order(self, create_order_model, color):
        payload = create_order_payload.copy()
        payload.update({"color": color})
        create_order_model.create_order(payload)
        create_order_model.check_status_code(201)
        create_order_model.check_order_is_created()