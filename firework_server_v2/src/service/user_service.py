import uuid
import datetime

from src.db import db
from src.model.user import User
from src.model.client import Client
from src.model.clients_cure import ClientsCure
from src.model.clients_recomendations import ClientsRecomendations
from src.model.enums import cureTypeEnum, recomendationTypeEnum
from src.model.notifications.aggrements import Aggrements
from typing import Dict, Tuple


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user_by_email = User.query.filter_by(email=data["email"]).first()
    user_by_phone = User.query.filter_by(phoneNumber=data["phoneNumber"]).first()
    if not user_by_email and not user_by_phone:
        new_user = User(
            public_id=str(uuid.uuid4()),
            firstName=data["firstName"],
            lastName=data["lastName"],
            middleName=data.get("middleName"),
            userTypeActual=data.get("userTypeActual"),
            statusActual=data.get("statusActual"),
            phoneNumber=data["phoneNumber"],
            email=data["email"],
            sexActual=data["sexActual"],
            country=data.get("country"),
            city=data.get("city"),
            blocked=False,
            password=data["password"],
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow(),
            description=data.get("description"),
            photo=data.get("photo"),
            admin = True
        )
        save_changes(new_user)

        new_aggrement = Aggrements(
            public_id=str(uuid.uuid4()),
            user_id = new_user.public_id,
            hasTGAggrement = data["hasTGAggrement"],
            hasMailAggrement = data["hasMailAggrement"]
        )
        save_changes(new_aggrement)

        if data.get("userTypeActual") == "client":
            if data.get("clients_info"):
                midNameUser = f" {new_user.middleName}" if new_user.middleName else ""
                new_client = Client(
                    public_id=str(uuid.uuid4()),
                    public_user_id=new_user.public_id,
                    clientEmail=new_user.email,
                    clientFullName=f"{new_user.firstName} {new_user.lastName}{midNameUser}",
                    clientCreated=new_user.created,
                    clientTypeActual=data.get("clients_info").get("clientTypeActual"),
                    diseaseLocation=data.get("clients_info").get("diseaseLocation"),
                    stageActual=data.get("clients_info").get("stageActual"),
                    monthsAfterTreatment=data.get("clients_info").get("monthsAfterTreatment"),
                    workWithPsychologist=data.get("clients_info").get("workWithPsychologist"),
                    experienceTypeActual=data.get("clients_info").get("experienceTypeActual"),
                    experienceDescription=data.get("clients_info").get("experienceDescription"),
                    duration=data.get("clients_info").get("duration")
                )
                save_changes(new_client)
                cureTypes = data.get("clients_info").get("cureType")
                if cureTypes:
                    for cure in cureTypes:
                        new_cure = ClientsCure(
                            public_id=str(uuid.uuid4()),
                            public_client_id=new_client.public_id,
                            cureType = cureTypeEnum(cure).name
                        )
                        save_changes(new_cure)
                recomendationTypes = data.get("clients_info").get("recomendationType")
                if recomendationTypes:
                    for recomendation in recomendationTypes:
                        if recomendation == 'Другое':
                            new_recomendation = ClientsRecomendations(
                                public_id=str(uuid.uuid4()),
                                public_client_id=new_client.public_id,
                                recomendationType = recomendationTypeEnum(recomendation).name,
                                recomendationDescription = data.get("clients_info").get("recomendationDescription")
                            )
                        else:
                            new_recomendation = ClientsRecomendations(
                                public_id=str(uuid.uuid4()),
                                public_client_id=new_client.public_id,
                                recomendationType = recomendationTypeEnum(recomendation).name
                            )
                        save_changes(new_recomendation)
            else:
                response_object = {
                "status": "fail",
                "message": "Невозможно создать клиента с данной информацией о нем.",
                }
                return response_object, 400
        return generate_token(new_user)
    else:
        response_object = {
            "status": "fail",
            "message": "Пользователь с такими идентификаторами уже существует. Пожалуйста, авторизуйтесь.",
        }
        return response_object, 400
    

def update_user(data: Dict[str, str], user : User) -> Tuple[Dict[str, str], int]:
    if user:
        user.firstName=data.get("firstName") if data.get("firstName") else user.firstName
        user.lastName=data.get("lastName") if data.get("lastName") else user.lastName
        user.middleName=data.get("middleName") if data.get("middleName") else user.middleName
        user.sexActual=data.get("sexActual") if data.get("sexActual") else user.sexActual
        user.userTypeActual=data.get("userTypeActual") if data.get("userTypeActual") else user.userTypeActual
        user.statusActual=data.get("statusActual") if data.get("statusActual") else user.statusActual
        user.country=data.get("country") if data.get("country") else user.firstName
        user.city=data.get("city") if data.get("city") else user.city
        user.updated=datetime.datetime.utcnow()
        user.description=data.get("description") if data.get("description") else user.description
        user.photo=data.get("photo") if data.get("photo") else user.photo

        save_changes(user)
        response_object = {
            "status": "success",
            "message": "Успешно обновлен.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Пользователь не существует.",
        }
        return response_object, 404


def get_all_users():
    return User.query.all()

def delete_a_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if user:
        User.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Пользователь не найден.",
        }
        return response_object, 404

def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user: User) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            "status": "success",
            "message": "Успешно зарегестрирован.",
            "Authorization": auth_token,
        }
        return response_object, 201
    except Exception as e:
        print(e)
        response_object = {
            "status": "fail",
            "message": "Возникла ошибка. Попробуйте снова.",
        }
        return response_object, 401


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()
