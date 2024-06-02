import uuid
import datetime

from src.db import db
from src.model.user import User
from src.model.consultation_card import ConsultationCard
from typing import Dict, Tuple
from src.word import word_create


def save_new_card_blueprint(data: Dict[str, str], cookie : str) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(id=User.decode_auth_token(cookie)).first()
    client = User.query.filter_by(public_id=data["publicUserClientId"]).first()
    card = ConsultationCard.query.filter_by(publicUserClientId=data["publicUserClientId"], publicSpecialistId = user.public_id, statusConsultationActual = "first").first()
    if user:
        if client:
            midNameClient = f" {client.middleName}" if client.middleName else ""
            midNameUser = f" {user.middleName}" if user.middleName else ""
            if data["statusConsultationActual"] == "first":
                new_card = ConsultationCard(
                public_id=str(uuid.uuid4()),
                validationStatusActual = "blueprint",
                created=datetime.datetime.utcnow(),
                publicUserClientId=data["publicUserClientId"],
                clientFullName=f"{client.lastName} {client.firstName}{midNameClient}",
                clientEmail=client.email,
                publicSpecialistId=user.public_id,
                specialistFullName=f"{user.lastName} {user.firstName}{midNameUser}",
                statusConsultationActual=data["statusConsultationActual"]
                )
                save_changes(new_card)
                response_object = {
                    "status": "success",
                    "message": "Успешно создан.",
                    "public_id" : new_card.public_id,
                }
                return response_object, 201
            elif card:
                card_copy = ConsultationCard(
                public_id=str(uuid.uuid4()),
                validationStatusActual = "blueprint",
                created=datetime.datetime.utcnow(),
                publicUserClientId=data["publicUserClientId"],
                clientFullName=f"{client.lastName} {client.firstName}{midNameClient}",
                clientEmail=client.email,
                publicSpecialistId=user.public_id,
                specialistFullName=f"{user.lastName} {user.firstName}{midNameUser}",
                statusConsultationActual=data["statusConsultationActual"]
                )

                insert_card_parameters_to_entity(card = card_copy, data = card.as_dict())
                save_changes(card_copy)
                response_object = {
                    "status": "success",
                    "message": "Успешно создан.",
                    "public_id" : card_copy.public_id,
                }
                return response_object, 201
            else:
                response_object = {
                    "status": "fail",
                    "message": "Первичной консультации для клиента не существует.",
                }
                return response_object, 400
        else:
            response_object = {
                "status": "fail",
                "message": "Клиент не существует.",
            }
            return response_object, 400
    else:
        response_object = {
                "status": "fail",
                "message": "Специалист не существует.",
            }
        return response_object, 400

def save_card(data: Dict[str, str], public_id : str) -> Tuple[Dict[str, str], int]:
    card = ConsultationCard.query.filter_by(public_id = public_id).first()
    if card:
        card = insert_card_parameters_to_entity(data = data, card = card)
        save_changes(card)
        response_object = {
            "status": "success",
            "message": "Успешно сохранено.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Карточки консультации не существует.",
        }
        return response_object, 404
    

def validate_card(data: Dict[str, str], public_id : str) -> Tuple[Dict[str, str], int]:
    card = ConsultationCard.query.filter_by(public_id = public_id).first()
    if card:
        card.validationStatusActual = "validated"
        card = insert_card_parameters_to_entity(data = data, card = card)
        save_changes(card)
        response_object = {
            "status": "success",
            "message": "Успешно провалидировано.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Карточки консультации не существует.",
        }
        return response_object, 404


def get_all_cards():
    return ConsultationCard.query.all()

def get_a_card(public_id):
    return ConsultationCard.query.filter_by(public_id=public_id).first()

def delete_a_card(public_id):
    card = ConsultationCard.query.filter_by(public_id=public_id).first()
    if card:
        ConsultationCard.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Карточки консультации не существует.",
        }
        return response_object, 404
    
def save_changes(data: ConsultationCard) -> None:
    db.session.add(data)
    db.session.commit()


def insert_card_parameters_to_entity(data: Dict[str, str], card: ConsultationCard) -> ConsultationCard:

    card.comPsychoEmotionNote=data.get("comPsychoEmotionNote")
    card.comSomatic=data.get("comSomatic")
    card.comSocial=data.get("comSocial")
    card.oncologyTime=data.get("oncologyTime")
    card.emotionReactOnco=data.get("emotionReactOnco")
    card.experiencingEmotion=data.get("experiencingEmotion")
    card.usuallyHelpEmotion=data.get("usuallyHelpEmotion")
    card.usuallyNoHelpEmotion=data.get("usuallyNoHelpEmotion")
    card.hasConnectionPsychotrauma=data.get("hasConnectionPsychotrauma")
    card.connectionPsychotraumaNote=data.get("connectionPsychotraumaNote")
    card.featuresConversationsNote=data.get("featuresConversationsNote")
    card.hasAnxiety=data.get("hasAnxiety")
    card.hasContinuousDuration=data.get("hasContinuousDuration")
    card.hasPersistentLowMood=data.get("hasPersistentLowMood")
    card.hasLossInterest=data.get("hasLossInterest")
    card.hasEnergyDecline=data.get("hasEnergyDecline")
    card.hasDecliningAttention=data.get("hasDecliningAttention")
    card.hasGuilt=data.get("hasGuilt")
    card.hasLowerSelfesteem=data.get("hasLowerSelfesteem")
    card.hasAppetiteChange=data.get("hasAppetiteChange")
    card.hasSleepDisturbance=data.get("hasSleepDisturbance")
    card.hasPessimisticThoughts=data.get("hasPessimisticThoughts")
    card.hasHopelessness=data.get("hasHopelessness")
    card.hasSuicidalThoughts=data.get("hasSuicidalThoughts")
    card.symptomAtRelationshipNote=data.get("symptomAtRelationshipNote")
    card.suicidalThoughtsNote=data.get("suicidalThoughtsNote")
    card.opinionPersonIllnessNote=data.get("opinionPersonIllnessNote")
    card.opinionOnsetOfDiseaseNote=data.get("opinionOnsetOfDiseaseNote")
    card.opinionTreatmentNote=data.get("opinionTreatmentNote")
    card.opinionFutureNote=data.get("opinionFutureNote")
    card.copingHostsNote=data.get("copingHostsNote")
    card.hasActiveCopingSpecies=data.get("hasActiveCopingSpecies")
    card.hasGoodDevelopedCoping=data.get("hasGoodDevelopedCoping")
    card.copingNote=data.get("copingNote")
    card.hasAlexithymiaPresumed=data.get("hasAlexithymiaPresumed")
    card.alexithymiaPresumedNote=data.get("alexithymiaPresumedNote")
    card.alexithymiaNoPresumedNote=data.get("alexithymiaNoPresumedNote")
    card.alexithymiaNote=data.get("alexithymiaNote")
    card.isHardToFallAsleep=data.get("isHardToFallAsleep")
    card.hasFrequentWaking=data.get("hasFrequentWaking")
    card.isAwakeEarly=data.get("isAwakeEarly")
    card.earlyAwakeningNote=data.get("earlyAwakeningNote")
    card.hasSleepDeprivation=data.get("hasSleepDeprivation")
    card.hasIncreasedDrowsiness=data.get("hasIncreasedDrowsiness")
    card.isCopeWithSleepDisturbancesActual=data.get("isCopeWithSleepDisturbancesActual")
    card.sleepNote=data.get("sleepNote")
    card.appetiteDisordersActual=data.get("appetiteDisordersActual")
    card.appetiteRegulationActionNote=data.get("appetiteRegulationActionNote")
    card.cognUnderstandingOfInfoNote=data.get("cognUnderstandingOfInfoNote")
    card.cognMemoizationOfInfoNote=data.get("cognMemoizationOfInfoNote")
    card.cognSpeechNote=data.get("cognSpeechNote")
    card.cognPraxisNote=data.get("cognPraxisNote")
    card.cognSocIntelligenceNote=data.get("cognSocIntelligenceNote")
    card.useCognBehavTherapy=data.get("useCognBehavTherapy")
    card.useExistentialTherapy=data.get("useExistentialTherapy")
    card.useWorkImagesTherapy=data.get("useWorkImagesTherapy")
    card.useDecisionTherapy=data.get("useDecisionTherapy")
    card.useAcceptanceTherapy=data.get("useAcceptanceTherapy")
    card.useArtTherapy=data.get("useArtTherapy")
    card.useBodilyOrientedTherapy=data.get("useBodilyOrientedTherapy")
    card.useOtherTherapy=data.get("useOtherTherapy")
    card.useOtherTherapyNote=data.get("useOtherTherapyNote")
    card.conclNotes=data.get("conclNotes")
    card.hasAdaptationDisorder=data.get("hasAdaptationDisorder")
    card.hasAnxietyDisorder=data.get("hasAnxietyDisorder")
    card.hasDepressionClinical=data.get("hasDepressionClinical")
    card.hasAcutePsyReact=data.get("hasAcutePsyReact")
    card.hasPostDisorder=data.get("hasPostDisorder")
    card.hasConclOther=data.get("hasConclOther")
    card.conclOtherNote=data.get("conclOtherNote")
    card.conclFirstPlanNote=data.get("conclFirstPlanNote")
    card.conclOnBackgroundNote=data.get("conclOnBackgroundNote")
    card.hasInnerPicture=data.get("hasInnerPicture")
    card.conclTargetNote=data.get("conclTargetNote")
    card.recomNeuroStudy=data.get("recomNeuroStudy")
    card.recomPathoStudy=data.get("recomPathoStudy")
    card.recomContactSpecialist=data.get("recomContactSpecialist")
    card.recomPassTraining=data.get("recomPassTraining")
    card.recomPassTrainingNote=data.get("recomPassTrainingNote")
    card.recomHomework=data.get("recomHomework")
    card.recomHomeworkNote=data.get("recomHomeworkNote")
    card.recomPsychocorrection=data.get("recomPsychocorrection")
    card.recomAdditionalPsychometry=data.get("recomAdditionalPsychometry")
    card.recomAdditionalPsychometryNote=data.get("recomAdditionalPsychometryNote")

    return card
    
def get_card_as_word(public_id : str):
    card = ConsultationCard.query.filter_by(public_id=public_id).first()
    if card:
        client = User.query.filter_by(public_id = card.publicUserClientId).first()
        f = word_create(card, client)
        return f
    return None
