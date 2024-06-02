import json

from test.base import BaseTestCase
from test_auth import register_user
from test_test_list_CRUD_methods import get_list, create_list
from test_test_question_CRUD_methods import get_question,create_question

def create_answer(self, test_question_id, token):
    return self.client.post(
        "/test/answeradd",
        data=json.dumps(
            dict(
                test_question_id = test_question_id,
                answerNumber=1,
                score=1,
                answerText="Текст ответа"
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def get_answer(self, token):
    return self.client.get(
        "/test/answeradd",
        headers=dict(authorization=token),
        content_type="application/json",
    )

def delete_answer(self, answer_id, token):
    return self.client.delete(
        "/test/answeradd",
        data=json.dumps(
            dict(
                public_id=answer_id
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def update_answer(self, answer_id, test_question_id, token):
    return self.client.put(
        "/test/answeradd",
        data=json.dumps(
            dict(
                public_id=answer_id,
                test_id = test_question_id,
                answerNumber=2,
                score=0,
                answerText="Текст ответа новый"
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


class TestTestsAnswerCRUDMethods(BaseTestCase):
    def test_answer_create(self):
        """Test for test answer create method"""
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
            test_question_id = json.loads(response.data.decode())['data'][0]['public_id']
            # test answer registration
            response = create_answer(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_answer_get(self):
        """Test for test answer get method"""
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
            test_question_id = json.loads(response.data.decode())['data'][0]['public_id']
            # test answer registration
            response = create_answer(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test answer get
            response = get_answer(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            test = json.loads(response.data.decode())['data'][0]
            print(test)
            self.assertTrue(test["test_question_id"] == test_question_id)
            self.assertTrue(test["answerNumber"] == 1)
            self.assertTrue(test["score"] == 1)
            self.assertTrue(test["answerText"] == "Текст ответа")

    def test_answer_delete(self):
        """Test for test answer delete method"""
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
            test_question_id = json.loads(response.data.decode())['data'][0]["public_id"]
            # test answer registration
            response = create_answer(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test answer get
            response = get_answer(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            answer_id = json.loads(response.data.decode())['data'][0]["public_id"]
            #test answer delete 
            response = delete_answer(self, answer_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно удален.")

            response = get_answer(self, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode())['data']
            self.assertTrue(data == [])

    def test_answer_update(self):
        """Test for test answer update method"""
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
            test_question_id = json.loads(response.data.decode())['data'][0]["public_id"]
            # test answer registration
            response = create_answer(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test answer get
            response = get_answer(self,data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            answer_id = json.loads(response.data.decode())['data'][0]["public_id"]
            #test question update 
            response = update_answer(self, answer_id, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно обновлен.")

            response = get_answer(self, data_register["Authorization"])
            test = json.loads(response.data.decode())['data'][0]
            print(test)
            self.assertTrue(test["test_question_id"] == test_question_id)
            self.assertTrue(test["answerNumber"] == 2)
            self.assertTrue(test["score"] == 0)
            self.assertTrue(test["answerText"] == "Текст ответа новый")


    def test_answer_delete_with_invalid_test(self):
        """Test for test answer delete method with invalid answer id"""
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
            #test answer delete 
            response = delete_answer(self, "123", data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Ответ не найден.")

    def test_answer_update_with_invalid_test(self):
        """Test for test answer update method with invalid answer id"""
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
            test_question_id = json.loads(response.data.decode())['data'][0]["public_id"]
            #test answer update 
            response = update_answer(self, "123", test_question_id,data_register["Authorization"])
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Ответ не найден.")
