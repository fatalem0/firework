import unittest

from src.db import db
import json
from test.base import BaseTestCase
from test_auth import register_user
from test_user_methods import get_all_users

def register_client(self, public_user_id, token):
    return self.client.post(
        "/client/",
        data=json.dumps(
            dict(
                public_user_id=public_user_id,
                clientTypeActual="patient",
                diseaseLocation="Голова",
                stageActual="justDiagnosed",
                monthsAfterTreatment="10",
                experienceTypeActual="positive",
                workWithPsychologist=True,
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )

def get_all_clients(self, token):
    return self.client.get(
        "/client/",
        content_type="application/json",
        headers=dict(authorization=token)
    )

def get_a_client(self, public_id, token):
    return self.client.get(
        f"/client/{public_id}",
        content_type="application/json",
        headers=dict(authorization=token)
    )

def update_client(self, public_id, token):
    return self.client.put(
        f"/client/{public_id}",
        data=json.dumps(
            dict(
                clientTypeActual="staff",
                diseaseLocation="Спина",
                stageActual="cure",
                monthsAfterTreatment="15",
                workWithPsychologist=False,
                experienceTypeActual="neutral",
                experienceDescription="Только один раз работала с персоналом",
                duration="15.5"
        )
        ),
        content_type="application/json",
        headers=dict(authorization=token)
    )

def delete_client(self, public_id, token):
    return self.client.delete(
        f"/client/{public_id}",
        content_type="application/json",
        headers=dict(authorization=token)
    )

class TestCLientMethods(BaseTestCase):
    def test_client_registration(self):
        """Test for clients registration"""
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
            # get existent user public-id
            response = get_all_users(self, data_register["Authorization"])
            public_user_id = json.loads(response.data.decode())['data'][0]['public_id']
            # client registration
            response = register_client(self, public_user_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно зарегестрирован.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)

    def test_client_registration_with_no_valid_public_user_id(self):
        """Test for clients registration with no valid public user id"""
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
            # client registration
            response = register_client(self, "1234", data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Пользователь не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)

    def test_get_all_clients(self):
        """Test for get all clients API"""
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
            # get existent user public-id
            response = get_all_users(self, data_register["Authorization"])
            public_user_id = json.loads(response.data.decode())['data'][0]['public_id']
            userCreated = json.loads(response.data.decode())['data'][0]['created']
            userEmail = json.loads(response.data.decode())['data'][0]['email']
            # client registration
            response = register_client(self, public_user_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно зарегестрирован.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # get all clients
            response = get_all_clients(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            client = data[0]
            print(client)
            self.assertTrue(client["public_user_id"] == public_user_id)
            self.assertTrue(client["clientEmail"] == userEmail)
            self.assertTrue(client["clientFullName"] == "Иванов Иван")
            self.assertTrue(client["clientCreated"] == userCreated)
            self.assertTrue(client["clientTypeActual"] == "Пациент")
            self.assertTrue(client["diseaseLocation"] == "Голова")
            self.assertTrue(client["stageActual"] == "Только поставлен диагноз")
            self.assertTrue(client["monthsAfterTreatment"] == "10")
            self.assertTrue(client["workWithPsychologist"])
            self.assertTrue(client["experienceTypeActual"] == "Положительный")

    def test_get_a_client_which_is_in_base(self):
        """Test for get a client which is in base"""
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
            # get existent user public-id
            response = get_all_users(self, data_register["Authorization"])
            public_user_id = json.loads(response.data.decode())['data'][0]['public_id']
            # client registration
            response = register_client(self, public_user_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно зарегестрирован.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # get existent client public-id
            response = get_all_clients(self, data_register["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # get a client
            response = get_a_client(self, public_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)    

    def test_get_a_client_which_is_not_in_base(self):
        """Test for get a client which is not in base"""
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
            # get a non-existent client
            response = get_a_client(self, 1234, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404) 


    def test_update_a_client_which_is_in_base(self):
        """Test for update a client which is in base"""
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
            # get existent user public-id
            response = get_all_users(self, data_register["Authorization"])
            public_user_id = json.loads(response.data.decode())['data'][0]['public_id']
            # client registration
            response = register_client(self, public_user_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно зарегестрирован.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # get existent client public-id
            response = get_all_clients(self, data_register["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # update a client
            response = update_client(self, public_id, data_register["Authorization"])
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200) 
            # get a client
            response = get_a_client(self, public_id, data_register["Authorization"])
            client = json.loads(response.data.decode())
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
            print(client)
            self.assertTrue(client["clientTypeActual"] == "Мед.Персонал")
            self.assertTrue(client["diseaseLocation"] == "Спина")
            self.assertTrue(client["stageActual"] == "Лечение")
            self.assertTrue(client["monthsAfterTreatment"] == "15")
            self.assertFalse(client["workWithPsychologist"])
            self.assertTrue(client["experienceTypeActual"] == "Нейтральный")
            self.assertTrue(client["experienceDescription"] == "Только один раз работала с персоналом")
            self.assertTrue(client["duration"] == "15.5")

    def test_update_a_client_which_is_not_in_base(self):
        """Test for update a client which is not in base"""
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
            # update a non-existent client
            response = update_client(self, 1234, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Клиент не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)

    def test_delete_client_which_is_not_in_base(self):
        """Test for user delete which is not in base"""
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
            # delete non-existent client
            response = delete_client(self, 123, data_register["Authorization"])
            data = json.loads(response.data.decode())

            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Клиент не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)

    
    def test_delete_client_which_is_in_base(self):
        """Test for user delete which is in base"""
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
            # get existent user public-id
            response = get_all_users(self, data_register["Authorization"])
            public_user_id = json.loads(response.data.decode())['data'][0]['public_id']
            # client registration
            response = register_client(self, public_user_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно зарегестрирован.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # get existent client public-id
            response = get_all_clients(self, data_register["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # delete client
            response = delete_client(self, public_id, data_register["Authorization"])
            data = json.loads(response.data.decode())

            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно удален.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)
               


if __name__ == "__main__":
    unittest.main()