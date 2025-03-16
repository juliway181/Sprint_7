import allure
from src import data as data
from models.base_model import BaseModel

class GetListOrderAPI(BaseModel):

    def get_list_orders(self, **kwargs):
        self.get_method(data.order_list_point, **kwargs)

    def check_orders_keys(self):
        actual_response = self.extract_keys(self.get_value_by_keys('orders', 0))
        expected_keys = self.extract_keys(data.orders_keys)
        assert actual_response == expected_keys

