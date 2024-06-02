import datetime
import unittest

from src.db import db
from src.model.blacklist import BlacklistToken
import json
from test.base import BaseTestCase


def get_all_users(self, token):
    return self.client.get(
        "/user/",
        content_type="application/json",
        headers=dict(authorization=token)
    )


def get_all_clients(self, token):
    return self.client.get(
        "/client/",
        content_type="application/json",
        headers=dict(authorization=token)
    )


def register_user(self):
    return self.client.post(
        "/user/",
        data=json.dumps(
            dict(
                email="test@test.com",
                firstName="Иван",
                lastName="Иванов",
                phoneNumber="8(999)999-99-99",
                password="test",
                sexActual="male",
                blocked=False,
                userTypeActual="employer",
        )
        ),
        content_type="application/json",
    )


def register_user_with_client(self):
    return self.client.post(
        "/user/",
        data=json.dumps(
            dict(
                email="test@test.com",
                firstName="Иван",
                lastName="Иванов",
                phoneNumber="8(999)999-99-99",
                password="test",
                sexActual="male",
                blocked=False,
                userTypeActual="client",
                clients_info = dict(
                    clientTypeActual="patient",
                    diseaseLocation="Голова",
                    stageActual="justDiagnosed",
                    monthsAfterTreatment="10",
                    experienceTypeActual="positive",
                    workWithPsychologist=True,
                )
        )
        ),
        content_type="application/json",
    )


def register_user_with_client_with_no_info(self):
    return self.client.post(
        "/user/",
        data=json.dumps(
            dict(
                email="test@test.com",
                firstName="Иван",
                lastName="Иванов",
                phoneNumber="8(999)999-99-99",
                password="test",
                sexActual="male",
                blocked=False,
                userTypeActual="client"
        )
        ),
        content_type="application/json",
    )


def register_user_same_email(self):
    return self.client.post(
        "/user/",
        data=json.dumps(
            dict(
                email="test@test.com",
                firstName="Иван1",
                lastName="Иванов1",
                phoneNumber="8(999)999-99-98",
                password="test1",
                sexActual="male",
                blocked=False,
                userTypeActual="employer",
        )
        ),
        content_type="application/json",
    )


def register_user_same_phone(self):
    return self.client.post(
        "/user/",
        data=json.dumps(
            dict(
                email="test2@test.com",
                firstName="Иван2",
                lastName="Иванов2",
                phoneNumber="8(999)999-99-99",
                password="test2",
                sexActual="male",
                blocked=False,
                userTypeActual="employer",
        )
        ),
        content_type="application/json",
    )


def register_user_full(self):
    return self.client.post(
        "/user/",
        data=json.dumps(
            dict(
                email="test@test.com",
                firstName="Иван",
                lastName="Иванов",
                phoneNumber="8(999)999-99-99",
                password="test",
                sexActual="male",
                blocked=False,
                middleName="Иванович",
                userTypeActual="employer",
                statusActual="new",
                country="Россия",
                city="Москва",
                description="Что-то",
                photo="Какое-то фото"
        )
        ),
        content_type="application/json",
    )


def login_user(self):
    return self.client.post(
        "/auth/login",
        data=json.dumps(
            dict(
                email="test@test.com",
                firstName="Иван",
                lastName="Иванов",
                phoneNumber="8(999)999-99-99",
                password="test",
                sexActual="male",
                blocked=False,
                userTypeActual="employer",
        )
        ),
        content_type="application/json",
    )


class TestAuthBlueprint(BaseTestCase):
    def test_registration(self):
        """Test for user registration"""
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)

    def test_registration_full(self):
        """Test for user registration with all fields"""
        with self.client:
            response = register_user_full(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)

    def test_registration_with_already_registered_user(self):
        """Test registration with already registered email"""
        register_user(self)
        with self.client:
            response = register_user_same_email(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Пользователь с такими идентификаторами уже существует. Пожалуйста, авторизуйтесь.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)

            
    def test_registration_with_same_email(self):
        """Test registration with already registered email"""
        register_user(self)
        with self.client:
            response = register_user_same_email(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Пользователь с такими идентификаторами уже существует. Пожалуйста, авторизуйтесь.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)


    def test_registration_with_same_phone(self):
        """Test registration with already registered phone"""
        register_user(self)
        with self.client:
            response = register_user_same_phone(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Пользователь с такими идентификаторами уже существует. Пожалуйста, авторизуйтесь.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)


    def test_registration_with_client(self):
        """Test registration with same clients registration"""
        with self.client:
            response = register_user_with_client(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # get existent user public-id
            response = get_all_users(self, data["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # get all clients
            response = get_all_clients(self, data["Authorization"])
            data = json.loads(response.data.decode())['data']
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            client = data[0]
            print(client)
            self.assertTrue(client["public_user_id"] == public_id)
            self.assertTrue(client["clientFullName"] == "Иван Иванов")



    def test_registration_with_client_without_clients_info_field(self):
        """Test registration with same clients registration without clients_info field"""
        with self.client:
            response = register_user_with_client_with_no_info(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Невозможно создать клиента с данной информацией о нем.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)


    def test_registered_user_login(self):
        """Test for login of registered-user login"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # registered user login
            response = login_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Удачный вход в систему.")
            self.assertTrue(data["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

    def test_non_registered_user_login(self):
        """Test for login of non-registered user"""
        with self.client:
            response = login_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Почта или пароль не совпадают.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 401)

    def test_valid_logout(self):
        """Test for logout before token expires"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # user login
            resp_login = login_user(self)
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login["status"] == "success")
            self.assertTrue(data_login["message"] == "Удачный вход в систему.")
            self.assertTrue(data_login["Authorization"])
            self.assertTrue(resp_login.content_type == "application/json")
            self.assertEqual(resp_login.status_code, 200)
            # valid token logout
            response = self.client.post(
                "/auth/logout",
                headers=dict(
                    Authorization="Bearer "
                    + json.loads(resp_login.data.decode())["Authorization"]
                ),
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Выход из системы произведен успешно.")
            self.assertEqual(response.status_code, 200)

    def test_valid_blacklisted_token_logout(self):
        """Test for logout after a valid token gets blacklisted"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # user login
            resp_login = login_user(self)
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login["status"] == "success")
            self.assertTrue(data_login["message"] == "Удачный вход в систему.")
            self.assertTrue(data_login["Authorization"])
            self.assertTrue(resp_login.content_type == "application/json")
            self.assertEqual(resp_login.status_code, 200)
            # blacklist a valid token
            blacklist_token = BlacklistToken(
                token=json.loads(resp_login.data.decode())["Authorization"]
            )
            db.session.add(blacklist_token)
            db.session.commit()
            # blacklisted valid token logout
            response = self.client.post(
                "/auth/logout",
                headers=dict(
                    Authorization="Bearer "
                    + json.loads(resp_login.data.decode())["Authorization"]
                ),
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(
                data["message"] == "Token blacklisted. Please log in again."
            )
            self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
