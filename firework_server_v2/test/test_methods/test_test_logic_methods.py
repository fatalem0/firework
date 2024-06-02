import json

from test.base import BaseTestCase
from test_auth import register_user
from test_test_list_CRUD_methods import get_list, create_list
from test_test_question_CRUD_methods import get_question, create_question
from test_test_answer_CRUD_methods import get_answer, create_answer
from test_test_settings_CRUD_methods import create_settings
from test_user_methods import get_all_users

def create_answer2(self, test_question_id, token):
    return self.client.post(
        "/test/answeradd",
        data=json.dumps(
            dict(
                test_question_id = test_question_id,
                answerNumber=2,
                score=0,
                answerText="Текст ответа два"
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


def get_log(self, token):
    return self.client.get(
        "/test/logs",
        headers=dict(authorization=token),
        content_type="application/json",
    )


def get_result(self, token):
    return self.client.get(
        "/test/result",
        headers=dict(authorization=token),
        content_type="application/json",
    )


def open_test(self, test_id,token):
    return self.client.post(
        "/test/open",
        data=json.dumps(
            dict(
                email = "test@test.com",
                test_id=test_id,
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


def answer(self, user_id, test_id, test_question_id, token):
    return self.client.post(
        "/test/answer",
        data=json.dumps(
            dict(
                user_id =  user_id,
                test_id =  test_id,
                test_question_id = test_question_id,
                answerNumber = [1],
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


def result(self, public_id, token):
    return self.client.post(
        f"/test/end/{public_id}",
        content_type="application/json",
        headers=dict(authorization=token)
    )


class TestTestsLogicMethods(BaseTestCase):
    def test_open_with_creation_result_and_log(self):
        """Test for test open method with result and log creation"""
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
            # test answer registration
            response = create_answer2(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # get user id
            response = get_all_users(self, data_register["Authorization"])
            user_id = json.loads(response.data.decode())["data"][0]["public_id"]

            # test open method
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            # check for return
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["user_id"] == user_id)
            self.assertTrue(data["test_id"] == test_id)
            self.assertTrue(data["name"] == "Новый тест")
            self.assertTrue(data["questionNumber"] == 1)
            self.assertTrue(data["numberOfQuestions"] == 2)
            self.assertTrue(data["test_question_id"] == test_question_id)
            self.assertTrue(data["title"] == "Первый вопрос")
            self.assertTrue(data["questionTypeActual"] == "Radio Button")

            ans1 = data["test_answers"][0]
            self.assertTrue(ans1["answerNumber"] == 1)
            self.assertTrue(ans1["score"] == 1)
            self.assertTrue(ans1["answerText"] == "Текст ответа")
            ans2 = data["test_answers"][1]
            self.assertTrue(ans2["answerNumber"] == 2)
            self.assertTrue(ans2["score"] == 0)
            self.assertTrue(ans2["answerText"] == "Текст ответа два")
            # check for log creation
            response = get_log(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data'][0]
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["user_id"] == user_id)
            self.assertTrue(data["test_id"] == test_id)
            self.assertTrue(data["testAnswersNumbers"] == None)
            self.assertTrue(data["gettedScore"] == 0)
            self.assertTrue(data["dateEnd"] == None)
            self.assertTrue(data["questionNumber"] == 1)
            # check for result creation
            response = get_result(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data'][0]
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["user_id"] == user_id)
            self.assertTrue(data["test_id"] == test_id)
            self.assertTrue(data["total"] == 0)


    def test_open_with_existing_result_and_log(self):
        """Test for test open method with existing result and log"""
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
            # test answer registration
            response = create_answer2(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # get user id
            response = get_all_users(self, data_register["Authorization"])
            user_id = json.loads(response.data.decode())["data"][0]["public_id"]

            # test open method first
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test open method second
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # check for return
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["user_id"] == user_id)
            self.assertTrue(data["test_id"] == test_id)
            self.assertTrue(data["name"] == "Новый тест")
            self.assertTrue(data["questionNumber"] == 1)
            self.assertTrue(data["numberOfQuestions"] == 2)
            self.assertTrue(data["test_question_id"] == test_question_id)
            self.assertTrue(data["title"] == "Первый вопрос")
            self.assertTrue(data["questionTypeActual"] == "Radio Button")

            ans1 = data["test_answers"][0]
            self.assertTrue(ans1["answerNumber"] == 1)
            self.assertTrue(ans1["score"] == 1)
            self.assertTrue(ans1["answerText"] == "Текст ответа")
            ans2 = data["test_answers"][1]
            self.assertTrue(ans2["answerNumber"] == 2)
            self.assertTrue(ans2["score"] == 0)
            self.assertTrue(ans2["answerText"] == "Текст ответа два")

            # check for log creation
            response = get_log(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data'][0]
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["user_id"] == user_id)
            self.assertTrue(data["test_id"] == test_id)
            self.assertTrue(data["testAnswersNumbers"] == None)
            self.assertTrue(data["gettedScore"] == 0)
            self.assertTrue(data["dateEnd"] == None)
            self.assertTrue(data["questionNumber"] == 1)
            # check for result creation
            response = get_result(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data'][0]
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["user_id"] == user_id)
            self.assertTrue(data["test_id"] == test_id)
            self.assertTrue(data["total"] == 0)




    def test_answer(self):
        """Test for test answer on test method"""
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
            test_answer_id = json.loads(response.data.decode())['data'][0]["public_id"]
            # test answer registration
            response = create_answer2(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # get user id
            response = get_all_users(self, data_register["Authorization"])
            user_id = json.loads(response.data.decode())["data"][0]["public_id"]

            # test open method first
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            # test answer method
            response = answer(self, user_id, test_id, test_question_id ,data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Ответ принят.")
            # check for log update
            response = get_log(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data'][0]
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["user_id"] == user_id)
            self.assertTrue(data["test_id"] == test_id)
            self.assertTrue(data["testAnswersNumbers"] == str(1))
            self.assertTrue(data["gettedScore"] == 1)
            self.assertTrue(data["questionNumber"] == 1)

    def test_answer_update_with_invalid_user(self):
        """Test for test answer on test with invalid user_id method"""
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
            # test answer registration
            response = create_answer2(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # get user id
            response = get_all_users(self, data_register["Authorization"])
            user_id = json.loads(response.data.decode())["data"][0]["public_id"]

            # test open method first
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            # test answer method
            response = answer(self, "123", test_id, test_question_id ,data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Лог теста не найден.")


    def test_answer_update_with_invalid_test(self):
        """Test for test answer on test with invalid test_id method"""
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
            # test answer registration
            response = create_answer2(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # get user id
            response = get_all_users(self, data_register["Authorization"])
            user_id = json.loads(response.data.decode())["data"][0]["public_id"]

            # test open method first
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            # test answer method
            response = answer(self, user_id, "123", test_question_id ,data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Лог теста не найден.")


    def test_answer_update_with_invalid_question(self):
        """Test for test answer on test with invalid test_question_id method"""
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
            # test answer registration
            response = create_answer2(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # get user id
            response = get_all_users(self, data_register["Authorization"])
            user_id = json.loads(response.data.decode())["data"][0]["public_id"]

            # test open method first
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            # test answer method
            response = answer(self, user_id, test_id, "123" ,data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Ответ не найден.")


    def test_result(self):
        """Test for test result method"""
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
            # test answer registration
            response = create_answer2(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # get user id
            response = get_all_users(self, data_register["Authorization"])
            user_id = json.loads(response.data.decode())["data"][0]["public_id"]

            # test open method first
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            # test answer method
            response = answer(self, user_id, test_id, test_question_id ,data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Ответ принят.")
            # get result_id
            response = get_result(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data'][0]
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            result_id = data["public_id"]
            # create settings
            response = create_settings(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # test result method
            response = result(self, result_id, data_register["Authorization"])
            data = json.loads(response.data.decode())["data"]
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["description"] == "Описание")
            self.assertTrue(data["recommendation"] == "Рекомендации")
            self.assertTrue(data["total"] == 1)


    def test_result_with_invalid_result(self):
        """Test for test result with invalid result_id method"""
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
            # test result method
            response = result(self, "123", data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)

    
    def test_result_with_no_settings_result(self):
        """Test for test result with no settings method"""
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
            # test answer registration
            response = create_answer2(self, test_question_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            # get user id
            response = get_all_users(self, data_register["Authorization"])
            user_id = json.loads(response.data.decode())["data"][0]["public_id"]

            # test open method first
            response = open_test(self, test_id, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            # test answer method
            response = answer(self, user_id, test_id, test_question_id ,data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Ответ принят.")
            # get result_id
            response = get_result(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data'][0]
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            result_id = data["public_id"]
            # test result method
            response = result(self, result_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data["message"] == "Настроек теста не найдено.")
