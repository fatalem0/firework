import unittest

from src.db import db
import json
from test.base import BaseTestCase
from test_auth import register_user
from test_user_methods import get_all_users
from test_client_methods import register_client, get_all_clients
from src.model.user import User


def register_card(self, publicUserClientId, type,token):
    return self.client.post(
        "/card/create",
        data=json.dumps(
            dict(
                publicUserClientId=publicUserClientId,
                statusConsultationActual=type,
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


def save_card_blueprint(self, public_id,token):
    return self.client.put(
        f"/card/save/blueprint/{public_id}",
        data=json.dumps(
            dict(
                comSomatic="норм",
                comSocial="норм",
                emotionReactOnco="норм",
                experiencingEmotion="норм",
                usuallyHelpEmotion="норм",
                usuallyNoHelpEmotion="норм",
                hasConnectionPsychotrauma=True,
                hasContinuousDuration=True,
                hasPersistentLowMood=True,
                hasLossInterest=True,
                hasEnergyDecline=True,
                hasDecliningAttention=True,
                hasGuilt=True,
                hasLowerSelfesteem=True,
                hasAppetiteChange=True,
                hasSleepDisturbance=True,
                hasPessimisticThoughts=True,
                hasHopelessness=True,
                hasSuicidalThoughts=True,
                hasActiveCopingSpecies=True,
                hasGoodDevelopedCoping=True,
                hasAlexithymiaPresumed=True,
                isHardToFallAsleep=True,
                hasFrequentWaking=True,
                isAwakeEarly=True,
                hasSleepDeprivation=True,
                hasIncreasedDrowsiness=True,
                isCopeWithSleepDisturbancesActual="bySelf",
                useCognBehavTherapy=True,
                useExistentialTherapy=True,
                useWorkImagesTherapy=True,
                useDecisionTherapy=True,
                useAcceptanceTherapy=True,
                useArtTherapy=True,
                useBodilyOrientedTherapy=True,
                useOtherTherapy=True,
                hasAdaptationDisorder=True,
                hasAnxietyDisorder=True,
                hasDepressionClinical=True,
                hasAcutePsyReact=True,
                hasPostDisorder=True,
                hasConclOther=True,
                hasInnerPicture=True,
                recomNeuroStudy=True,
                recomPathoStudy=True,
                recomContactSpecialist=True,
                recomPassTraining=True,
                recomHomework=True,
                recomPsychocorrection=True,
                recomAdditionalPsychometry=True,
                oncologyTime="норм",
                appetiteDisordersActual="increased",
                hasAnxiety=True,
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


def card_validate(self, public_id,token):
    return self.client.put(
        f"/card/save/card/{public_id}",
        data=json.dumps(
            dict(
                comSomatic="норм",
                comSocial="норм",
                emotionReactOnco="норм",
                experiencingEmotion="норм",
                usuallyHelpEmotion="норм",
                usuallyNoHelpEmotion="норм",
                hasConnectionPsychotrauma=True,
                hasContinuousDuration=True,
                hasPersistentLowMood=True,
                hasLossInterest=True,
                hasEnergyDecline=True,
                hasDecliningAttention=True,
                hasGuilt=True,
                hasLowerSelfesteem=True,
                hasAppetiteChange=True,
                hasSleepDisturbance=True,
                hasPessimisticThoughts=True,
                hasHopelessness=True,
                hasSuicidalThoughts=True,
                hasActiveCopingSpecies=True,
                hasGoodDevelopedCoping=True,
                hasAlexithymiaPresumed=True,
                isHardToFallAsleep=True,
                hasFrequentWaking=True,
                isAwakeEarly=True,
                hasSleepDeprivation=True,
                hasIncreasedDrowsiness=True,
                isCopeWithSleepDisturbancesActual="bySelf",
                useCognBehavTherapy=True,
                useExistentialTherapy=True,
                useWorkImagesTherapy=True,
                useDecisionTherapy=True,
                useAcceptanceTherapy=True,
                useArtTherapy=True,
                useBodilyOrientedTherapy=True,
                useOtherTherapy=True,
                hasAdaptationDisorder=True,
                hasAnxietyDisorder=True,
                hasDepressionClinical=True,
                hasAcutePsyReact=True,
                hasPostDisorder=True,
                hasConclOther=True,
                hasInnerPicture=True,
                recomNeuroStudy=True,
                recomPathoStudy=True,
                recomContactSpecialist=True,
                recomPassTraining=True,
                recomHomework=True,
                recomPsychocorrection=True,
                recomAdditionalPsychometry=True,
                oncologyTime="норм",
                appetiteDisordersActual="increased",
                hasAnxiety=True,
        )
        ),
        headers=dict(authorization=token),
        content_type="application/json",
    )


def get_all_cards(self, token):
    return self.client.get(
        "/card/",
        content_type="application/json",
        headers=dict(authorization=token)
    )


def get_a_card(self, public_id, token):
    return self.client.get(
        f"/card/{public_id}",
        content_type="application/json",
        headers=dict(authorization=token)
    )


def update_card(self, public_id, token):
    return self.client.put(
        f"/card/{public_id}",
        data=json.dumps(
            dict(
                statusConsultationActual="second",
                comPsychoEmotionNote="Лучше",
                comSomatic="Лучше",
                comSocial="Лучше",
                oncologyTime="1234",
                emotionReactOnco="Хорошее"
        )
        ),
        content_type="application/json",
        headers=dict(authorization=token)
    )


def delete_card(self, public_id, token):
    return self.client.delete(
        f"/card/{public_id}",
        content_type="application/json",
        headers=dict(authorization=token)
    )

class TestCardMethods(BaseTestCase):
    def test_card_registration_first(self):
        """Test for first card registration"""
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
            # card registration
            response = register_card(self, publicUserClientId=public_user_id, type="first",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)

    
    def test_card_registration_with_no_valid_client(self):
        """Test for cards registration with no valid client"""
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
            # card registration
            response = register_card(self, publicUserClientId="123", type="first", token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Клиент не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)


    def test_card_registration_second(self):
        """Test for second card registration"""
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
            # card first registration
            response = register_card(self, publicUserClientId=public_user_id, type="first",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # card second registration
            response = register_card(self, publicUserClientId=public_user_id, type="second",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)


    def test_card_registration_second_with_no_first_card(self):
        """Test for second card registration with no first card"""
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
            # card second registration
            response = register_card(self, publicUserClientId=public_user_id, type="second",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Первичной консультации для клиента не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 400)


    def test_card_blueprint_save(self):
        """Test for cards blueprint save"""
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
            # card first registration
            response = register_card(self, publicUserClientId=public_user_id, type="first",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            public_card_id = data["public_id"]
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # save card blueprint
            response = save_card_blueprint(self, public_id=public_card_id,token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно сохранено.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)


    def test_card_blueprint_save_without_card_creation(self):
        """Test for cards blueprint save without card creation"""
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
            # save card blueprint
            response = save_card_blueprint(self, public_id="123",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Карточки консультации не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)


    def test_card_validate(self):
        """Test for cards validate"""
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
            # card first registration
            response = register_card(self, publicUserClientId=public_user_id, type="first",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            public_card_id = data["public_id"]
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # validate card
            response = card_validate(self, public_id=public_card_id, token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно провалидировано.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)


    def test_card_validate_with_no_card(self):
        """Test for cards validate with no card"""
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
            # validate card
            response = card_validate(self, public_id="123", token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Карточки консультации не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)

    
    def test_get_all_cards(self):
        """Test for get all cards API"""
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
            # card registration
            response = register_card(self, publicUserClientId=public_user_id, type = "first",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # get all cards
            response = get_all_cards(self, data_register["Authorization"])
            data = json.loads(response.data.decode())['data']
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)

            card = data[0]
            print(card)
            self.assertTrue(card["publicUserClientId"] == public_user_id)
            self.assertTrue(card["clientFullName"] == "Иванов Иван")
            self.assertTrue(card["clientEmail"] == "test@test.com")
            self.assertTrue(card["publicSpecialistId"] == public_user_id)
            self.assertTrue(card["specialistFullName"] == "Иванов Иван")
            self.assertTrue(card["statusConsultationActual"] == "Первичная")


    def test_get_a_card_which_is_in_base(self):
        """Test for get a card which is in base"""
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
            # card registration
            response = register_card(self, publicUserClientId=public_user_id, type="first",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # get existent card public-id
            response = get_all_cards(self, data_register["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # get a card
            response = get_a_card(self, public_id, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)  


    def test_get_a_card_which_is_not_in_base(self):
        """Test for get a card which is not in base"""
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
            # get a card
            response = get_a_card(self, 123, data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)  

    
    def test_delete_card_which_is_not_in_base(self):
        """Test for card delete which is not in base"""
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
            # delete non-existent card
            response = delete_card(self, 123, data_register["Authorization"])
            data = json.loads(response.data.decode())

            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Карточки консультации не существует.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 404)

    
    def test_delete_card_which_is_in_base(self):
        """Test for card delete which is in base"""
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
            # card registration
            response = register_card(self, publicUserClientId=public_user_id, type="first",token=data_register["Authorization"])
            data = json.loads(response.data.decode())
            print(data)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно создан.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 201)
            # get existent card public-id
            response = get_all_cards(self, data_register["Authorization"])
            public_id = json.loads(response.data.decode())['data'][0]['public_id']
            # delete card
            response = delete_card(self, public_id, data_register["Authorization"])
            data = json.loads(response.data.decode())

            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Успешно удален.")
            self.assertTrue(response.content_type == "application/json")
            self.assertEqual(response.status_code, 200)