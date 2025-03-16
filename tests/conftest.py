import pytest
import requests
from models.create_couriers_model import CreateCouriersAPI
from models.login_courier_model import LoginCourierAPI
from models.create_order_model import CreateOrderAPI
from models.get_list_orders_model import GetListOrderAPI

@pytest.fixture()
def create_courier_model():
    response = requests
    courier_model = CreateCouriersAPI(response)
    return courier_model


@pytest.fixture()
def login_courier_model():
    response = requests
    login_model = LoginCourierAPI(response)
    return login_model

@pytest.fixture()
def create_order_model():
    response = requests
    create_order_model = CreateOrderAPI(response)
    return create_order_model

@pytest.fixture()
def get_list_order_model():
    response = requests
    get_lst_model = GetListOrderAPI(response)
    return get_lst_model
