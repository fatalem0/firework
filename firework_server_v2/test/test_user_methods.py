import datetime
import unittest

from src.db import db
from src.model.blacklist import BlacklistToken
import json
from test.base import BaseTestCase
from test_auth import register_user, login_user, register_user_full


def get_all_users(self, token):
    return self.client.get(
        "/user/",
        content_type="application/json",
        headers=dict(authorization=token)
    )

def update_user(self, public_id, token):
    return self.client.put(
        f"/user/{public_id}",
        data=json.dumps(
            dict(
                firstName="Мария",
                lastName="Петрова",
                sexActual="female",
                middleName="Петровна",
                userTypeActual="employer",
                statusActual="active",
                country="Казахстан",
                city="Астана",
                description="Что-то новое",
                photo="Какое-то фото новое"
        )
        ),
        content_type="application/json",
        headers=dict(authorization=token)
    )


def update_one_field(self, public_id, token):
    return self.client.put(
        f"/user/{public_id}",
        data=json.dumps(
            dict(
                password="test2"
        )
        ),
        content_type="application/json",
        headers=dict(authorization=token)
    )


def delete_user(self, public_id, token):
    return self.client.delete(
        f"/user/{public_id}",
        content_type="application/json",
        headers=dict(authorization=token)
    )

class TestUserMethods(BaseTestCase):
    def test_get_all_users(self):
        """Test for get list users"""
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # get all users
            response = get_all_users(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            user = data[0]
            self.assertTrue(user["firstName"] == "Иван")
            self.assertTrue(user["lastName"] == "Иванов")
            self.assertTrue(user["email"] == "test@test.com")
            self.assertTrue(user["phoneNumber"] == "8(999)999-99-99")
            self.assertTrue(user["sexActual"] == "Мужской")
            self.assertTrue(user["userTypeActual"] == "Сотрудник")
            self.assertFalse(user["blocked"])


    
    def test_update_user_which_is_not_in_base(self):
        """Test for user update which is not in base"""
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
            # non-existent user update
            response = update_user(self, "123", data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Пользователь не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)

    def test_update_user_which_is_in_base(self):
        """Test for user update which is in base"""
        with self.client:
            # user registration
            resp_register = register_user_full(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # get existent user public-id
            response = get_all_users(self, data_register["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # non-existent user update
            response = update_user(self, public_id, data_register["Authorization"])
            data = json.loads(response.data.decode())

            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно обновлен.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            response = get_all_users(self, data_register["Authorization"])
            user = json.loads(response.data.decode())['data'][0]
            print(user)
            self.assertTrue(user["firstName"] == "Мария")
            self.assertTrue(user["lastName"] == "Петрова")
            self.assertTrue(user["sexActual"] == "Женский")
            self.assertTrue(user["middleName"] == "Петровна")
            self.assertTrue(user["userTypeActual"] == "Сотрудник")
            self.assertTrue(user["statusActual"] == "ACTIVE")
            self.assertTrue(user["country"] == "Казахстан")
            self.assertTrue(user["city"] == "Астана")
            self.assertTrue(user["description"] == "Что-то новое")
            self.assertTrue(user["photo"] == "Какое-то фото новое")
    
    
    def test_update_user_one_field(self):
        """Test for user update one field"""
        with self.client:
            # user registration
            resp_register = register_user_full(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # get existent user public-id
            response = get_all_users(self, data_register["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # non-existent user update
            response = update_one_field(self, public_id, data_register["Authorization"])
            data = json.loads(response.data.decode())

            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно обновлен.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            response = get_all_users(self, data_register["Authorization"])
            user = json.loads(response.data.decode())['data'][0]
            print(user)
            self.assertTrue(user["firstName"] == "Иван")
            self.assertTrue(user["lastName"] == "Иванов")
            self.assertTrue(user["email"] == "test@test.com")
            self.assertTrue(user["phoneNumber"] == "8(999)999-99-99")
            self.assertTrue(user["sexActual"] == "Мужской")
            self.assertTrue(user["userTypeActual"] == "Сотрудник")
            self.assertFalse(user["blocked"])


    def test_delete_user_which_is_not_in_base(self):
        """Test for user delete which is not in base"""
        with self.client:
            # user registration
            resp_register = register_user_full(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # delete a user
            response = delete_user(self, 123, data_register["Authorization"])
            data = json.loads(response.data.decode())

            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Пользователь не найден.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)


    def test_delete_user_which_is_in_base(self):
        """Test for user delete which is in base"""
        with self.client:
            # user registration
            resp_register = register_user_full(self)
            data_register = json.loads(resp_register.data.decode())
            print(data_register)
            self.assertTrue(data_register["status"] == "success")
            self.assertTrue(data_register["message"] == "Успешно зарегестрирован.")
            self.assertTrue(data_register["Authorization"])
            self.assertTrue(resp_register.content_type == "application/json")
            self.assertEqual(resp_register.status_code, 201)
            # get existent user public-id
            response = get_all_users(self, data_register["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # non-existent user delete
            response = delete_user(self, public_id, data_register["Authorization"])
            print(response)
            data = json.loads(response.data.decode())
            

            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно удален.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
