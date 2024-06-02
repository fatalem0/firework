import json

from test.base import BaseTestCase
from test_auth import register_user
from test_test_list_CRUD_methods import get_list, create_list

def create_question(self, test_id, token):
    return self.client.post(
        "/test/question",
        data=json.dumps(
            dict(
                test_id = test_id,
                questionNumber=1,
                title="Первый вопрос",
                questionTypeActual="radio"
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def get_question(self, token):
    return self.client.get(
        "/test/question",
        headers=dict(authorization=token),
        content_type="application/json",
    )

def delete_question(self, question_id, token):
    return self.client.delete(
        "/test/question",
        data=json.dumps(
            dict(
                public_id=question_id
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def update_question(self, question_id, test_id, token):
    return self.client.put(
        "/test/question",
        data=json.dumps(
            dict(
                public_id=question_id,
                test_id = test_id,
                questionNumber=2,
                title="Второй вопрос",
                questionTypeActual="checkbox"
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


class TestTestsQuestionCRUDMethods(BaseTestCase):
    def test_question_create(self):
        """Test for test question create method"""
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
            # test question registration
            response = create_question(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_question_get(self):
        """Test for test question get method"""
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
            # test question registration
            response = create_question(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test question get
            response = get_question(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            test = json.loads(response.data.decode())['data'][0]
            print(test)
            self.assertTrue(test["test_id"] == test_id)
            self.assertTrue(test["questionNumber"] == 1)
            self.assertTrue(test["title"] == "Первый вопрос")
            self.assertTrue(test["questionTypeActual"] == "Radio Button")

    def test_question_delete(self):
        """Test for test question delete method"""
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
            # test question registration
            response = create_question(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test question get
            response = get_question(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            question_id = json.loads(response.data.decode())['data'][0]["public_id"]
            #test question delete 
            response = delete_question(self, question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно удален.")

            response = get_question(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode())['data']
            self.assertTrue(data == [])

    def test_question_update(self):
        """Test for test question update method"""
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
            # test question registration
            response = create_question(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test question get
            response = get_question(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            question_id = json.loads(response.data.decode())['data'][0]["public_id"]
            print(json.loads(response.data.decode())['data'][0])
            #test question update 
            response = update_question(self, question_id, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно обновлен.")

            response = get_question(self, data_register["Authorization"])
            test = json.loads(response.data.decode())['data'][0]
            print(test)
            self.assertTrue(test["test_id"] == test_id)
            self.assertTrue(test["questionNumber"] == 2)
            self.assertTrue(test["title"] == "Второй вопрос")
            self.assertTrue(test["questionTypeActual"] == "Checkbox")


    def test_question_delete_with_invalid_test(self):
        """Test for test question delete method with invalid question id"""
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
            response = delete_question(self, "123", data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Вопрос не найден.")

    def test_question_update_with_invalid_test(self):
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
            #test question update 
            response = update_question(self, "123", test_id,data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Вопрос не найден.")
