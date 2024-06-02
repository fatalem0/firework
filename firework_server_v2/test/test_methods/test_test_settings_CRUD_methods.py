import json

from test.base import BaseTestCase
from test_auth import register_user
from test_test_list_CRUD_methods import get_list, create_list

def create_settings(self, test_id, token):
    return self.client.post(
        "/test/settings",
        data=json.dumps(
            dict(
                test_id = test_id,
                stressLevelActual="yellow",
                minCount=0,
                maxCount=1,
                description="Описание",
                recommendation="Рекомендации"
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def get_settings(self, token):
    return self.client.get(
        "/test/settings",
        headers=dict(authorization=token),
        content_type="application/json",
    )

def delete_settings(self, settings_id, token):
    return self.client.delete(
        "/test/settings",
        data=json.dumps(
            dict(
                public_id=settings_id
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def update_settings(self, settings_id, test_id, token):
    return self.client.put(
        "/test/settings",
        data=json.dumps(
            dict(
                public_id=settings_id,
                test_id = test_id,
                stressLevelActual="red",
                minCount=1,
                maxCount=2,
                description="Описание новое",
                recommendation="Рекомендации новое"
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


class TestTestsSettingsCRUDMethods(BaseTestCase):
    def test_settings_create(self):
        """Test for test settings create method"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # test list registration
            response = create_list(self, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            #test_id get
            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            test_id = json.loads(response.data.decode())['data'][0]["public_id"]
            # test settings registration
            response = create_settings(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_settings_get(self):
        """Test for test settings get method"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # test list registration
            response = create_list(self, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            #test_id get
            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            test_id = json.loads(response.data.decode())['data'][0]["public_id"]
            # test settings registration
            response = create_settings(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test settings get
            response = get_settings(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            test = json.loads(response.data.decode())['data'][0]
            print(test)
            self.assertTrue(test["test_id"] == test_id)
            self.assertTrue(test["stressLevelActual"] == "Желтый")
            self.assertTrue(test["minCount"] == 0)
            self.assertTrue(test["maxCount"] == 1)
            self.assertTrue(test["description"] == "Описание")
            self.assertTrue(test["recommendation"] == "Рекомендации")


    def test_settings_delete(self):
        """Test for test settings delete method"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # test list registration
            response = create_list(self, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            #test_id get
            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            test_id = json.loads(response.data.decode())['data'][0]["public_id"]
            # test settings registration
            response = create_settings(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test settings get
            response = get_settings(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            settings_id = json.loads(response.data.decode())['data'][0]["public_id"]
            #test settings delete 
            response = delete_settings(self, settings_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно удален.")

            response = get_settings(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode())['data']
            self.assertTrue(data == [])

    def test_settings_update(self):
        """Test for test settings update method"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # test list registration
            response = create_list(self, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            #test_id get
            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            test_id = json.loads(response.data.decode())['data'][0]["public_id"]
            # test settings registration
            response = create_settings(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test settings get
            response = get_settings(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            settings_id = json.loads(response.data.decode())['data'][0]["public_id"]
            print(json.loads(response.data.decode())['data'][0])
            #test settings update 
            response = update_settings(self, settings_id, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно обновлен.")

            response = get_settings(self, data_register["Authorization"])
            test = json.loads(response.data.decode())['data'][0]
            print(test)
            self.assertTrue(test["test_id"] == test_id)
            self.assertTrue(test["stressLevelActual"] == "Красный")
            self.assertTrue(test["minCount"] == 1)
            self.assertTrue(test["maxCount"] == 2)
            self.assertTrue(test["description"] == "Описание новое")
            self.assertTrue(test["recommendation"] == "Рекомендации новое")


    def test_settings_delete_with_invalid_test(self):
        """Test for test settings delete method with invalid question id"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            #test question delete 
            response = delete_settings(self, "123", data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Настроек теста не найдено.")

    def test_settings_update_with_invalid_test(self):
        """Test for test question update method with invalid question id"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # test list registration
            response = create_list(self, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            #test_id get
            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            test_id = json.loads(response.data.decode())['data'][0]["public_id"]
            #test settings update 
            response = update_settings(self, "123", test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Настроек теста не найдено.")
