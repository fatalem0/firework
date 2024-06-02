import json

from test.base import BaseTestCase
from test_auth import register_user

def create_list(self, token):
    return self.client.post(
        "/test/list",
        data=json.dumps(
            dict(
                name="Новый тест",
                clientTypeActual="patient",
                stageActual="justDiagnosed",
                interval=3,
                numberOfQuestions=2
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def get_list(self, token):
    return self.client.get(
        "/test/list",
        headers=dict(authorization=token),
        content_type="application/json",
    )

def delete_list(self, list_id, token):
    return self.client.delete(
        "/test/list",
        data=json.dumps(
            dict(
                public_id=list_id
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def update_list(self, list_id, token):
    return self.client.put(
        "/test/list",
        data=json.dumps(
            dict(
                public_id=list_id,
                name="Новый тест новый",
                clientTypeActual="staff",
                stageActual="cure",
                interval=4,
                numberOfQuestions=3
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


class TestTestsListCRUDMethods(BaseTestCase):
    def test_list_create(self):
        """Test for test list create method"""
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
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_list_get(self):
        """Test for test list get method"""
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
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test list get
            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            test = json.loads(response.data.decode())['data'][0]
            print(test)
            self.assertTrue(test["name"] == "Новый тест")
            self.assertTrue(test["clientTypeActual"] == "Пациент")
            self.assertTrue(test["stageActual"] == "Только поставлен диагноз")
            self.assertTrue(test["interval"] == 3)
            self.assertTrue(test["numberOfQuestions"] == 2)

    def test_list_delete(self):
        """Test for test list delete method"""
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
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test list get
            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            list_id = json.loads(response.data.decode())['data'][0]["public_id"]
            #test list delete 
            response = delete_list(self, list_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно удален.")

            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode())['data']
            self.assertTrue(data == [])

    def test_list_update(self):
        """Test for test list update method"""
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
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test list get
            response = get_list(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            list_id = json.loads(response.data.decode())['data'][0]["public_id"]
            #test list update 
            response = update_list(self, list_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно обновлен.")

            response = get_list(self, data_register["Authorization"])
            test = json.loads(response.data.decode())['data'][0]
            print(test)
            self.assertTrue(test["name"] == "Новый тест новый")
            self.assertTrue(test["clientTypeActual"] == "Мед.Персонал")
            self.assertTrue(test["stageActual"] == "Лечение")
            self.assertTrue(test["interval"] == 4)
            self.assertTrue(test["numberOfQuestions"] == 3)


    def test_list_delete_with_invalid_test(self):
        """Test for test list delete method with invalid list id"""
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
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            #test list delete 
            response = delete_list(self, "123", data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Тест не найден")

    def test_list_update_with_invalid_test(self):
        """Test for test list update method with invalid list id"""
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
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            #test list update 
            response = update_list(self, "123", data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Тест не найден")
