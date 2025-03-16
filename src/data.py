import src.helper as helper


create_courier_point = '/api/v1/courier'
login_courier_point = '/api/v1/courier/login'
create_order_point = '/api/v1/orders'
order_list_point = '/api/v1/orders'



create_courier_payload = {
    "login": helper.generate_random_string(12),
    "password": helper.generate_random_string(12),
    "firstName": helper.generate_random_string(12)
}

created_courier_payload = {
    "login": helper.register_new_courier_and_return_login_password()[0],
    "password": helper.register_new_courier_and_return_login_password()[1],
    "firstName": helper.register_new_courier_and_return_login_password()[2]
}

duplicate_login_payload = {
    "login": helper.register_new_courier_and_return_login_password()[0],
    "password": 'asdn2@lsafj',
    "firstName": 'Buratino'
}

login_payload = {
    "login": "Turman225",
    "password": "123141"
}

create_order_payload = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}

orders_keys = {
                "id": int,
                "courierId": bool,
                "firstName": str,
                "lastName": str,
                "address": str,
                "metroStation": str,
                "phone": str,
                "rentTime": int,
                "deliveryDate": str,
                "track": int,
                "color": [],
                "comment": str,
                "createdAt": str,
                "updatedAt": str,
                "status": int
    }

