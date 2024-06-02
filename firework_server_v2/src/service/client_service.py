import uuid

from src.db import db
from src.model.client import Client
from src.model.user import User
from src.model.clients_cure import ClientsCure
from src.model.clients_recomendations import ClientsRecomendations
from typing import Dict, Tuple


def save_new_client(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(public_id=data["public_user_id"]).first()
    client = Client.query.filter_by(public_user_id=data["public_user_id"]).first()
    if user:
        if not client:
            midNameUser = f" {user.middleName}" if user.middleName else ""
            new_client = Client(
                public_id=str(uuid.uuid4()),
                public_user_id=data["public_user_id"],
                clientEmail=user.email,
                clientFullName=f"{user.lastName} {user.firstName}{midNameUser}",
                clientCreated=user.created,
                clientTypeActual=data["clientTypeActual"],
                diseaseLocation=data["diseaseLocation"],
                stageActual=data["stageActual"],
                monthsAfterTreatment=data["monthsAfterTreatment"],
                workWithPsychologist=data["workWithPsychologist"],
                experienceTypeActual=data["experienceTypeActual"],
                experienceDescription=data.get("experienceDescription"),
                duration=data.get("duration")
            )
            save_changes(new_client)
            response_object = {
                "status": "success",
                "message": "Успешно зарегестрирован.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Клиент для этого пользователя уже существует.",
            }
            return response_object, 400
    else:
        response_object = {
                "status": "fail",
                "message": "Пользователь не существует.",
            }
        return response_object, 400


def update_client(data: Dict[str, str], public_id : str) -> Tuple[Dict[str, str], int]:
    client = Client.query.filter_by(public_id=public_id).first()
    if client:
        client.clientTypeActual=data.get("clientTypeActual") if data.get("clientTypeActual") else client.clientTypeActual
        client.diseaseLocation=data.get("diseaseLocation") if data.get("diseaseLocation") else client.diseaseLocation
        client.stageActual=data.get("stageActual") if data.get("stageActual") else client.stageActual
        client.monthsAfterTreatment=data.get("monthsAfterTreatment") if data.get("monthsAfterTreatment") else client.monthsAfterTreatment
        client.workWithPsychologist=data.get("workWithPsychologist") if data.get("workWithPsychologist") is not None else client.workWithPsychologist
        client.experienceTypeActual=data.get("experienceTypeActual") if data.get("experienceTypeActual") else client.experienceTypeActual
        client.experienceDescription=data.get("experienceDescription") if data.get("experienceDescription") else client.experienceDescription
        client.duration=data.get("duration") if data.get("duration") else client.duration

        save_changes(client)
        response_object = {
            "status": "success",
            "message": "Успешно обновлен.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Клиент не существует.",
        }
        return response_object, 404

def get_all_clients():
    return Client.query.all()

def get_a_client(public_id):
    client = Client.query.filter_by(public_id=public_id).first()
    if client:
        response_object = vars(client)
        cureTypes = ClientsCure.query.filter_by(public_client_id=public_id).all()
        response_object["cureType"] = []
        for cure in cureTypes:
            response_object["cureType"].append(cure.cureType.value)
        
        recomendationTypes = ClientsRecomendations.query.filter_by(public_client_id=public_id).all()
        response_object["recomendationType"] = []
        for recomendation in recomendationTypes:
            response_object["recomendationType"].append(recomendation.recomendationType.value)
            if recomendation.recomendationType.value == 'Другое':
                response_object["recomendationDescription"] = recomendation.recomendationDescription

        return response_object
    else:
        return None

def delete_a_client(public_id):
    client = Client.query.filter_by(public_id=public_id).first()
    if client:
        Client.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Клиент не существует.",
        }
        return response_object, 404
    
def save_changes(data: Client) -> None:
    db.session.add(data)
    db.session.commit()
