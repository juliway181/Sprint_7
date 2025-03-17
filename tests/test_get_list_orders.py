import allure


class TestGetListOrder:

    @allure.title("Проверка получения списка заказов")
    def test_get_list_orders(self, get_list_order_model):
        get_list_order_model.get_list_orders()
        get_list_order_model.check_status_code(200)
        get_list_order_model.check_orders_keys()