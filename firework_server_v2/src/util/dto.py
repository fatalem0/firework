from flask_restx import Namespace, fields


class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'

class NullableBoolean(fields.Boolean):
    __schema_type__ = ['boolean', 'null']
    __schema_example__ = 'nullable boolean'

class UserDto:
    api = Namespace("user", description="user related operations")
    user_return = api.model(
        "user_return",
        {
            "public_id": fields.String(description="user Identifier"),
            "firstName": fields.String(required=True, description="user firstName"),       
            "lastName": fields.String(required=True, description="user lastName"), 
            "middleName": fields.String(description="user middleName"), 
            "userTypeActual": fields.String(required=True, description="user Type", enum = ["client", "employer"]),
            "statusActual": fields.String(description="user status", enum = ["new", "failed_val", "success_val", "active", "blocked", "archive"]),
            "email": fields.String(required=True, description="user email address"),
            "phoneNumber": fields.String(description="user phone number"),
            "sexActual": fields.String(description="user sex", enum = ["male", "female"], required=True),
            "country": fields.String(description="users country"), 
            "city": fields.String(description="users city"), 
            "blocked": fields.Boolean(description="is user blocked"), 
            "created": fields.String(description="when user was created"),
            "updated": fields.String(description="when user was updated"),
            "password": fields.String(required=True, description="user password"), 
            "description": fields.String(description="users description"), 
            "photo": fields.String(description="users photo"), 
        },
    )
    user_create = api.model(
        "user_create",
        {
            "firstName": fields.String(required=True, description="user firstName"),       
            "lastName": fields.String(required=True, description="user lastName"), 
            "middleName": fields.String(description="user middleName"), 
            "userTypeActual": fields.String(required=True, description="user Type", enum = ["client", "employer"]),
            "statusActual": fields.String(description="user status", enum = ["new", "failed_val", "success_val", "active", "blocked", "archive"]),
            "email": fields.String(required=True, description="user email address"),
            "phoneNumber": fields.String(description="user phone number"),
            "sexActual": fields.String(description="user sex", enum = ["male", "female"], required=True),
            "country": fields.String(description="users country"), 
            "city": fields.String(description="users city"), 
            "blocked": fields.Boolean(description="is user blocked"),
            "password": fields.String(required=True, description="user password"), 
            "description": fields.String(description="users description"), 
            "photo": fields.String(description="users photo"), 
        },
    )
    user_update = api.model(
        "user_update",
        {
            "firstName": fields.String(description="user firstName"),       
            "lastName": fields.String(description="user lastName"), 
            "middleName": fields.String(description="user middleName"), 
            "email": fields.String(description="user email address"),
            "phoneNumber": fields.String(description="user phone number"),
            "password": fields.String(description="user password"), 
            "sexActual": fields.String(description="user sex", enum = ["male", "female"]),
            "userTypeActual": fields.String(description="user Type", enum = ["client", "employer"]),
            "statusActual": fields.String(description="user status", enum = ["new", "failed_val", "success_val", "active", "blocked", "archive"]),
            "country": fields.String(description="users country"), 
            "city": fields.String(description="users city"), 
            "blocked": fields.Boolean(description="is user blocked"), 
            "description": fields.String(description="users description"), 
            "photo": fields.String(description="users photo"), 
        },
    )
    client_create_for_user = api.model(
        "client_create_for_user",
        {
            "clientTypeActual": fields.String(required=True, description="client Type", enum = ["patient", "staff", "relatives"]), 
            "diseaseLocation": fields.String(description="clients diseaseLocation"),
            "stageActual": fields.String(description="clients stage of disease", enum = ["justDiagnosed", "cure", "therapy", "remission", "palliativeCare"]),
            "monthsAfterTreatment": fields.String(description="months after clients treatment"),
            "workWithPsychologist": fields.Boolean( description="Had client worked with psychologist"),
            "experienceTypeActual": fields.String(description="clients experience", enum = ["positive", "neutral", "negative"]),
            "experienceDescription": fields.String(description="clients experience description"), 
            "duration": fields.String(description="clients cure duration"),
            "cureType": fields.List(fields.String(description="clients cure types", enum = ["Химеотерапия", "Лучевая терапия", "Операция", "Таргетная терапия", "Гормонотерапия", "Паллиативное лечение"])),
            "recomendationType": fields.List(fields.String(description="clients recomendation types", enum = [
                "Информацию о том, как справляться с эмоциями", 
                "Упражнения, чтобы самому приводить себя в норму", 
                "Группу поддержки", 
                "Индивидуальную работу с психологом", 
                "Другое"])),
            "recomendationDescription": fields.String(description="clients recomendation description"),
        },
    )
    user_create_with_client = api.model(
        "user_update",
        {
            "firstName": fields.String(description="user firstName"),       
            "lastName": fields.String(description="user lastName"), 
            "middleName": fields.String(description="user middleName"), 
            "email": fields.String(description="user email address"),
            "phoneNumber": fields.String(description="user phone number"),
            "password": fields.String(description="user password"), 
            "sexActual": fields.String(description="user sex", enum = ["male", "female"]),
            "userTypeActual": fields.String(description="user Type", enum = ["client", "employer"]),
            "statusActual": fields.String(description="user status", enum = ["new", "failed_val", "success_val", "active", "blocked", "archive"]),
            "country": fields.String(description="users country"), 
            "city": fields.String(description="users city"), 
            "blocked": fields.Boolean(description="is user blocked"), 
            "description": fields.String(description="users description"), 
            "photo": fields.String(description="users photo"),
            "hasTGAggrement": fields.Boolean(description = "user has agreement fo sending Telegram notifications", required = True),
            "hasMailAggrement": fields.Boolean(description = "user has agreement fo sending mail notifications", required = True),
            "clients_info": fields.Nested(client_create_for_user, description="users info for creating client")
        },
    )


class ClientDto:
    api = Namespace("client", description="client related operations")
    client_return = api.model(
        "client_return",
        {
            "public_id": fields.String(description="client Identifier"),
            "public_user_id": fields.String(required=True, description="user Identifier referenced to client"),
            "clientEmail" : fields.String(required=True, description="user email referenced to client"),
            "clientFullName": fields.String(description="user FCs referenced to client"),
            "clientCreated": fields.String(description="user creation time referenced to client"),
            "clientTypeActual": fields.String(required=True, description="client Type", enum = ["patient", "staff", "relatives"]), 
            "diseaseLocation": fields.String(description="clients diseaseLocation"),
            "stageActual": fields.String(required=True, description="clients stage of disease", enum = ["justDiagnosed", "cure", "therapy", "remission", "palliativeCare"]),
            "monthsAfterTreatment": fields.String(description="months after clients treatment"),
            "workWithPsychologist": fields.Boolean( description="Had client worked with psychologist"),
            "experienceTypeActual": fields.String(description="clients experience", enum = ["positive", "neutral", "negative"]),
            "experienceDescription": fields.String(description="clients experience description"), 
            "duration": fields.String(description="clients cure duration"),
            "cureType": fields.List(fields.String(description="clients cure types", enum = ["Химеотерапия", "Лучевая терапия", "Операция", "Таргетная терапия", "Гормонотерапия", "Паллиативное лечение"])),
            "recomendationType": fields.List(fields.String(description="clients recomendation types", enum = [
                "Информацию о том, как справляться с эмоциями", 
                "Упражнения, чтобы самому приводить себя в норму", 
                "Группу поддержки", 
                "Индивидуальную работу с психологом", 
                "Другое"], 
                as_list = True)),
            "recomendationDescription": fields.String(description="clients recomendation description"),
        },
    )
    client_return_all = api.model(
        "client_return",
        {
            "public_id": fields.String(description="client Identifier"),
            "public_user_id": fields.String(required=True, description="user Identifier referenced to client"),
            "clientEmail" : fields.String(required=True, description="user email referenced to client"),
            "clientFullName": fields.String(description="user FCs referenced to client"),
            "clientCreated": fields.String(description="user creation time referenced to client"),
            "clientTypeActual": fields.String(required=True, description="client Type", enum = ["patient", "staff", "relatives"]), 
            "diseaseLocation": fields.String(description="clients diseaseLocation"),
            "stageActual": fields.String(required=True, description="clients stage of disease", enum = ["justDiagnosed", "cure", "therapy", "remission", "palliativeCare"]), 
            "monthsAfterTreatment": fields.String(description="months after clients treatment"),
            "workWithPsychologist": fields.Boolean( description="Had client worked with psychologist"),
            "experienceTypeActual": fields.String(description="clients experience", enum = ["positive", "neutral", "negative"]),
            "experienceDescription": fields.String(description="clients experience description"), 
            "duration": fields.String(description="clients cure duration"),
        },
    )
    client_create = api.model(
        "client_create",
        {
            "public_user_id": fields.String(required=True, description="user Identifier referenced to client"),
            "clientTypeActual": fields.String(required=True, description="client Type", enum = ["patient", "staff", "relatives"]), 
            "diseaseLocation": fields.String(description="clients diseaseLocation"),
            "stageActual": fields.String(required=True, description="clients stage of disease", enum = ["justDiagnosed", "cure", "therapy", "remission", "palliativeCare"]), 
            "monthsAfterTreatment": fields.String(description="months after clients treatment"),
            "workWithPsychologist": fields.Boolean( description="Had client worked with psychologist"),
            "experienceTypeActual": fields.String(description="clients experience", enum = ["positive", "neutral", "negative"]),
            "experienceDescription": fields.String(description="clients experience description"), 
            "duration": fields.String(description="clients cure duration"),
        },
    )
    client_update = api.model(
        "client_update",
        {
            "clientTypeActual": fields.String(description="client Type", enum = ["patient", "staff", "relatives"]), 
            "diseaseLocation": fields.String(description="clients diseaseLocation"), 
            "stageActual": fields.String(description="clients stage of disease", enum = ["justDiagnosed", "cure", "therapy", "remission", "palliativeCare"]), 
            "monthsAfterTreatment": fields.String(description="months after clients treatment"), 
            "workWithPsychologist": fields.Boolean(description="Had client worked with psychologist"), 
            "experienceTypeActual": fields.String(description="clients experience", enum = ["positive", "neutral", "negative"]), 
            "experienceDescription": fields.String(description="clients experience description"), 
            "duration": fields.String(description="clients cure duration"),
        },
    )


class ConsultationCardDto:
    api = Namespace("consultation_card", description="consultation card related operations")
    consultation_card_return = api.model(
        "consultation_card_return",
        {
            "public_id": fields.String(required=True, description="consultation_card Identifier"),
            "validationStatusActual": fields.String(required=True, description="card validation status", enum=['blueprint', 'validated']),
            "created": fields.String(required=True, description="when card was created"),
            "clientFullName": fields.String(required=True, description="clients Full Name"),
            "specialistFullName": fields.String(required=True, description="specialists Full Name"),
            "clientEmail": fields.String(required=True, description="clients Email"),
            "publicUserClientId": fields.String(required=True, description="user Identifier referenced to cards client"),
            "publicSpecialistId": fields.String(required=True, description="specialist Identifier referenced to card"),
            "statusConsultationActual": fields.String(required=True, description="Status of consultation", enum=['first', 'second']),
            # Жалобы пациента
            "comPsychoEmotionNote": NullableString(description="clients comPsychoEmotionNote"), 
            "comSomatic": fields.String(required=True, description="clients comSomatic"), 
            "comSocial": fields.String(required=True, description="clients comSocial"), 
            # Анамнез заболевания
            "oncologyTime": fields.String(required=True, description="clients oncologyTime"), 
            "emotionReactOnco": fields.String(required=True, description="clients emotionReactOnco"), 
            "experiencingEmotion": fields.String(required=True, description="clients experiencingEmotion"), 
            "usuallyHelpEmotion": fields.String(required=True, description="clients usuallyHelpEmotion"), 
            "usuallyNoHelpEmotion": fields.String(required=True, description="clients usuallyNoHelpEmotion"), 
            "hasConnectionPsychotrauma": fields.Boolean(required=True, description="clients hasConnectionPsychotrauma"), 
            "connectionPsychotraumaNote": NullableString(description="clients connectionPsychotraumaNote"), 
            # Раздел “Объективный статус”
            "featuresConversationsNote": NullableString(description="clients featuresConversationsNote"), 
            "hasAnxiety": fields.Boolean(required=True, description="clients hasAnxiety"), 
            # Подраздел “Депрессивные симптомы”
            "hasContinuousDuration": fields.Boolean(required=True, description="clients hasContinuousDuration"), 
            "hasPersistentLowMood": fields.Boolean(required=True, description="clients hasPersistentLowMood"), 
            "hasLossInterest": fields.Boolean(required=True, description="clients hasLossInterest"), 
            "hasEnergyDecline": fields.Boolean(required=True, description="clients hasEnergyDecline"), 
            "hasDecliningAttention": fields.Boolean(required=True, description="clients hasDecliningAttention"), 
            "hasGuilt": fields.Boolean(required=True, description="clients hasGuilt"), 
            "hasLowerSelfesteem": fields.Boolean(required=True, description="clients hasLowerSelfesteem"), 
            "hasAppetiteChange": fields.Boolean(required=True, description="clients hasAppetiteChange"), 
            "hasSleepDisturbance": fields.Boolean(required=True, description="clients hasSleepDisturbance"), 
            "hasPessimisticThoughts": fields.Boolean(required=True, description="clients hasPessimisticThoughts"), 
            "hasHopelessness": fields.Boolean(required=True, description="clients hasHopelessness"), 
            "hasSuicidalThoughts": fields.Boolean(required=True, description="clients hasSuicidalThoughts"), 
            "symptomAtRelationshipNote": NullableString(description="clients symptomAtRelationshipNote"), 
            "suicidalThoughtsNote": NullableString(description="clients suicidalThoughtsNote"), 
            # Раздел “Внутренняя картина болезни”
            "opinionPersonIllnessNote": NullableString(description="clients opinionPersonIllnessNote"), 
            "opinionOnsetOfDiseaseNote": NullableString(description="clients opinionOnsetOfDiseaseNote"),
            "opinionTreatmentNote": NullableString(description="clients opinionTreatmentNote"),
            "opinionFutureNote": NullableString(description="clients opinionFutureNote"),
            # Подраздел “Копинги”
            "copingHostsNote": NullableString(description="clients copingHostsNote"), 
            "hasActiveCopingSpecies": fields.Boolean(required=True, description="clients hasActiveCopingSpecies"),
            "hasGoodDevelopedCoping": fields.Boolean(required=True, description="clients hasGoodDevelopedCoping"),
            "copingNote": NullableString(description="clients copingNote"),
            # Подраздел “Алекситимия”
            "hasAlexithymiaPresumed": fields.Boolean(required=True, description="clients hasAlexithymiaPresumed"), 
            "alexithymiaPresumedNote": NullableString(description="clients alexithymiaPresumedNote"),
            "alexithymiaNoPresumedNote": NullableString(description="clients alexithymiaNoPresumedNote"),
            "alexithymiaNote": NullableString(description="clients alexithymiaNote"),
            # Раздел “Нарушение сна”
            "isHardToFallAsleep": fields.Boolean(required=True, description="clients isHardToFallAsleep"), 
            "hasFrequentWaking": fields.Boolean(required=True, description="clients hasFrequentWaking"),
            "isAwakeEarly": fields.Boolean(required=True, description="clients isAwakeEarly"),
            "earlyAwakeningNote": NullableString(description="clients earlyAwakeningNote"),
            "hasSleepDeprivation": fields.Boolean(required=True, description="clients hasSleepDeprivation"),
            "hasIncreasedDrowsiness": fields.Boolean(required=True, description="clients hasIncreasedDrowsiness"),
            "isCopeWithSleepDisturbancesActual": fields.String(required=True, description="clients isCopeWithSleepDisturbances", enum=[
                "bySelf",
                "withMedicine",
                "cantСope"
            ]),
            "sleepNote": NullableString(description="clients sleepNote"),
            # Раздел “Аппетит”
            "appetiteDisordersActual": fields.String(required=True, description="clients appetiteDisorders", enum=["increased", "decreased"]), 
            "appetiteRegulationActionNote": NullableString(description="clients appetiteRegulationActionNote"),
            # Раздел “Когнитивные функции”
            "cognUnderstandingOfInfoNote": NullableString(description="clients cognUnderstandingOfInfoNote"), 
            "cognMemoizationOfInfoNote": NullableString(description="clients cognMemoizationOfInfoNote"),
            "cognSpeechNote": NullableString(description="clients cognSpeechNote"),
            "cognPraxisNote": NullableString(description="clients cognPraxisNote"),
            "cognSocIntelligenceNote": NullableString(description="clients cognSocIntelligenceNote"),
            # Раздел “В беседе использовалась терапия”
            "useCognBehavTherapy": fields.Boolean(required=True, description="clients useCognBehavTherapy"), 
            "useExistentialTherapy": fields.Boolean(required=True, description="clients useExistentialTherapy"),
            "useWorkImagesTherapy": fields.Boolean(required=True, description="clients useWorkImagesTherapy"),
            "useDecisionTherapy": fields.Boolean(required=True, description="clients useDecisionTherapy"),
            "useAcceptanceTherapy": fields.Boolean(required=True, description="clients useAcceptanceTherapy"),
            "useArtTherapy": fields.Boolean(required=True, description="clients useArtTherapy"),
            "useBodilyOrientedTherapy": fields.Boolean(required=True, description="clients useBodilyOrientedTherapy"),
            "useOtherTherapy": fields.Boolean(required=True, description="clients useOtherTherapy"),
            "useOtherTherapyNote": NullableString(description="clients useOtherTherapyNote"),
            # Раздел “Заключение”
            "conclNotes": NullableString(description="clients conclNotes"), 
            "hasAdaptationDisorder": fields.Boolean(required=True, description="clients hasAdaptationDisorder"),
            "hasAnxietyDisorder": fields.Boolean(required=True, description="clients hasAnxietyDisorder"),
            "hasDepressionClinical": fields.Boolean(required=True, description="clients hasDepressionClinical"),
            "hasAcutePsyReact": fields.Boolean(required=True, description="clients hasAcutePsyReact"),
            "hasPostDisorder": fields.Boolean(required=True, description="clients hasPostDisorder"),
            "hasConclOther": fields.Boolean(required=True, description="clients hasConclOther"),
            "conclOtherNote": NullableString(description="clients conclOtherNote"),
            "conclFirstPlanNote": NullableString(description="clients conclFirstPlanNote"),
            "conclOnBackgroundNote": NullableString(description="clients conclOnBackgroundNote"),
            "hasInnerPicture": fields.Boolean(required=True, description="clients hasInnerPicture"),
            "conclTargetNote": NullableString(description="clients conclTargetNote"),
            # Раздел “Рекомендации”
            "recomNeuroStudy": fields.Boolean(required=True, description="clients recomNeuroStudy"), 
            "recomPathoStudy": fields.Boolean(required=True, description="clients recomPathoStudy"),
            "recomContactSpecialist": fields.Boolean(required=True, description="clients recomContactSpecialist"),
            "recomPassTraining": fields.Boolean(required=True, description="clients recomPassTraining"),
            "recomPassTrainingNote": NullableString(description="clients recomPassTrainingNote"),
            "recomHomework": fields.Boolean(required=True, description="clients recomHomework"),
            "recomHomeworkNote": NullableString(description="clients recomHomeworkNote"),
            "recomPsychocorrection": fields.Boolean(required=True, description="clients recomPsychocorrection"),
            "recomAdditionalPsychometry": fields.Boolean(required=True, description="clients recomAdditionalPsychometry"),
            "recomAdditionalPsychometryNote": NullableString(description="clients recomAdditionalPsychometryNote"),
        },
    )
    consultation_card_create_new = api.model(
        "consultation_card_create_new",
        {
            "publicUserClientId": fields.String(required=True, description="user Identifier referenced to cards client"),
            "statusConsultationActual": fields.String(required=True, description="Status of consultation", enum=['first', 'second']),
        },
    )
    consultation_card_save_blueprint = api.model(
        "consultation_card_save_blueprint",
        {
            # Жалобы пациента
            "comPsychoEmotionNote": NullableString(description="clients comPsychoEmotionNote"), 
            "comSomatic": NullableString(description="clients comSomatic"), 
            "comSocial": NullableString(description="clients comSocial"), 
            # Анамнез заболевания
            "oncologyTime": NullableString(description="clients oncologyTime"), 
            "emotionReactOnco": NullableString(description="clients emotionReactOnco"), 
            "experiencingEmotion": NullableString(description="clients experiencingEmotion"), 
            "usuallyHelpEmotion": NullableString(description="clients usuallyHelpEmotion"), 
            "usuallyNoHelpEmotion": NullableString(description="clients usuallyNoHelpEmotion"), 
            "hasConnectionPsychotrauma": NullableBoolean(description="clients hasConnectionPsychotrauma"), 
            "connectionPsychotraumaNote": NullableString(description="clients connectionPsychotraumaNote"), 
            # Раздел “Объективный статус”
            "featuresConversationsNote": NullableString(description="clients featuresConversationsNote"), 
            "hasAnxiety": NullableBoolean(description="clients hasAnxiety"), 
            # Подраздел “Депрессивные симптомы”
            "hasContinuousDuration": NullableBoolean(description="clients hasContinuousDuration"), 
            "hasPersistentLowMood": NullableBoolean(description="clients hasPersistentLowMood"), 
            "hasLossInterest": NullableBoolean(description="clients hasLossInterest"), 
            "hasEnergyDecline": NullableBoolean(description="clients hasEnergyDecline"), 
            "hasDecliningAttention": NullableBoolean(description="clients hasDecliningAttention"), 
            "hasGuilt": NullableBoolean(description="clients hasGuilt"), 
            "hasLowerSelfesteem": NullableBoolean(description="clients hasLowerSelfesteem"), 
            "hasAppetiteChange": NullableBoolean(description="clients hasAppetiteChange"), 
            "hasSleepDisturbance": NullableBoolean(description="clients hasSleepDisturbance"), 
            "hasPessimisticThoughts": NullableBoolean(description="clients hasPessimisticThoughts"), 
            "hasHopelessness": NullableBoolean(description="clients hasHopelessness"), 
            "hasSuicidalThoughts": NullableBoolean(description="clients hasSuicidalThoughts"), 
            "symptomAtRelationshipNote": NullableString(description="clients symptomAtRelationshipNote"), 
            "suicidalThoughtsNote": NullableString(description="clients suicidalThoughtsNote"), 
            # Раздел “Внутренняя картина болезни”
            "opinionPersonIllnessNote": NullableString(description="clients opinionPersonIllnessNote"), 
            "opinionOnsetOfDiseaseNote": NullableString(description="clients opinionOnsetOfDiseaseNote"),
            "opinionTreatmentNote": NullableString(description="clients opinionTreatmentNote"),
            "opinionFutureNote": NullableString(description="clients opinionFutureNote"),
            # Подраздел “Копинги”
            "copingHostsNote": NullableString(description="clients copingHostsNote"), 
            "hasActiveCopingSpecies": NullableBoolean(description="clients hasActiveCopingSpecies"),
            "hasGoodDevelopedCoping": NullableBoolean(description="clients hasGoodDevelopedCoping"),
            "copingNote": NullableString(description="clients copingNote"),
            # Подраздел “Алекситимия”
            "hasAlexithymiaPresumed": NullableBoolean(description="clients hasAlexithymiaPresumed"), 
            "alexithymiaPresumedNote": NullableString(description="clients alexithymiaPresumedNote"),
            "alexithymiaNoPresumedNote": NullableString(description="clients alexithymiaNoPresumedNote"),
            "alexithymiaNote": NullableString(description="clients alexithymiaNote"),
            # Раздел “Нарушение сна”
            "isHardToFallAsleep": NullableBoolean(description="clients isHardToFallAsleep"), 
            "hasFrequentWaking": NullableBoolean(description="clients hasFrequentWaking"),
            "isAwakeEarly": NullableBoolean(description="clients isAwakeEarly"),
            "earlyAwakeningNote": NullableString(description="clients earlyAwakeningNote"),
            "hasSleepDeprivation": NullableBoolean(description="clients hasSleepDeprivation"),
            "hasIncreasedDrowsiness": NullableBoolean(description="clients hasIncreasedDrowsiness"),
            "isCopeWithSleepDisturbancesActual": NullableString(description="clients isCopeWithSleepDisturbances", enum=[
                "bySelf",
                "withMedicine",
                "cantСope",
                None
            ]),
            "sleepNote": NullableString(description="clients sleepNote"),
            # Раздел “Аппетит”
            "appetiteDisordersActual": NullableString(description="clients appetiteDisorders", enum=["increased", "decreased", None]), 
            "appetiteRegulationActionNote": NullableString(description="clients appetiteRegulationActionNote"),
            # Раздел “Когнитивные функции”
            "cognUnderstandingOfInfoNote": NullableString(description="clients cognUnderstandingOfInfoNote"), 
            "cognMemoizationOfInfoNote": NullableString(description="clients cognMemoizationOfInfoNote"),
            "cognSpeechNote": NullableString(description="clients cognSpeechNote"),
            "cognPraxisNote": NullableString(description="clients cognPraxisNote"),
            "cognSocIntelligenceNote": NullableString(description="clients cognSocIntelligenceNote"),
            # Раздел “В беседе использовалась терапия”
            "useCognBehavTherapy": NullableBoolean(description="clients useCognBehavTherapy"), 
            "useExistentialTherapy": NullableBoolean(description="clients useExistentialTherapy"),
            "useWorkImagesTherapy": NullableBoolean(description="clients useWorkImagesTherapy"),
            "useDecisionTherapy": NullableBoolean(description="clients useDecisionTherapy"),
            "useAcceptanceTherapy": NullableBoolean(description="clients useAcceptanceTherapy"),
            "useArtTherapy": NullableBoolean(description="clients useArtTherapy"),
            "useBodilyOrientedTherapy": NullableBoolean(description="clients useBodilyOrientedTherapy"),
            "useOtherTherapy": NullableBoolean(description="clients useOtherTherapy"),
            "useOtherTherapyNote": NullableString(description="clients useOtherTherapyNote"),
            # Раздел “Заключение”
            "conclNotes": NullableString(description="clients conclNotes"), 
            "hasAdaptationDisorder": NullableBoolean(description="clients hasAdaptationDisorder"),
            "hasAnxietyDisorder": NullableBoolean(description="clients hasAnxietyDisorder"),
            "hasDepressionClinical": NullableBoolean(description="clients hasDepressionClinical"),
            "hasAcutePsyReact": NullableBoolean(description="clients hasAcutePsyReact"),
            "hasPostDisorder": NullableBoolean(description="clients hasPostDisorder"),
            "hasConclOther": NullableBoolean(description="clients hasConclOther"),
            "conclOtherNote": NullableString(description="clients conclOtherNote"),
            "conclFirstPlanNote": NullableString(description="clients conclFirstPlanNote"),
            "conclOnBackgroundNote": NullableString(description="clients conclOnBackgroundNote"),
            "hasInnerPicture": NullableBoolean(description="clients hasInnerPicture"),
            "conclTargetNote": NullableString(description="clients conclTargetNote"),
            # Раздел “Рекомендации”
            "recomNeuroStudy": NullableBoolean(description="clients recomNeuroStudy"), 
            "recomPathoStudy": NullableBoolean(description="clients recomPathoStudy"),
            "recomContactSpecialist": NullableBoolean(description="clients recomContactSpecialist"),
            "recomPassTraining": NullableBoolean(description="clients recomPassTraining"),
            "recomPassTrainingNote": NullableString(description="clients recomPassTrainingNote"),
            "recomHomework": NullableBoolean(description="clients recomHomework"),
            "recomHomeworkNote": NullableString(description="clients recomHomeworkNote"),
            "recomPsychocorrection": NullableBoolean(description="clients recomPsychocorrection"),
            "recomAdditionalPsychometry": NullableBoolean(description="clients recomAdditionalPsychometry"),
            "recomAdditionalPsychometryNote": NullableString(description="clients recomAdditionalPsychometryNote"),
        },
    )
    consultation_card_validate = api.model(
        "consultation_card_validate",
        {
            # Жалобы пациента
            "comPsychoEmotionNote": NullableString(description="clients comPsychoEmotionNote"), 
            "comSomatic": fields.String(required=True, description="clients comSomatic"), 
            "comSocial": fields.String(required=True, description="clients comSocial"), 
            # Анамнез заболевания
            "oncologyTime": fields.String(required=True, description="clients oncologyTime"), 
            "emotionReactOnco": fields.String(required=True, description="clients emotionReactOnco"), 
            "experiencingEmotion": fields.String(required=True, description="clients experiencingEmotion"), 
            "usuallyHelpEmotion": fields.String(required=True, description="clients usuallyHelpEmotion"), 
            "usuallyNoHelpEmotion": fields.String(required=True, description="clients usuallyNoHelpEmotion"), 
            "hasConnectionPsychotrauma": fields.Boolean(required=True, description="clients hasConnectionPsychotrauma"), 
            "connectionPsychotraumaNote": NullableString(description="clients connectionPsychotraumaNote"), 
            # Раздел “Объективный статус”
            "featuresConversationsNote": NullableString(description="clients featuresConversationsNote"), 
            "hasAnxiety": fields.Boolean(required=True, description="clients hasAnxiety"), 
            # Подраздел “Депрессивные симптомы”
            "hasContinuousDuration": fields.Boolean(required=True, description="clients hasContinuousDuration"), 
            "hasPersistentLowMood": fields.Boolean(required=True, description="clients hasPersistentLowMood"), 
            "hasLossInterest": fields.Boolean(required=True, description="clients hasLossInterest"), 
            "hasEnergyDecline": fields.Boolean(required=True, description="clients hasEnergyDecline"), 
            "hasDecliningAttention": fields.Boolean(required=True, description="clients hasDecliningAttention"), 
            "hasGuilt": fields.Boolean(required=True, description="clients hasGuilt"), 
            "hasLowerSelfesteem": fields.Boolean(required=True, description="clients hasLowerSelfesteem"), 
            "hasAppetiteChange": fields.Boolean(required=True, description="clients hasAppetiteChange"), 
            "hasSleepDisturbance": fields.Boolean(required=True, description="clients hasSleepDisturbance"), 
            "hasPessimisticThoughts": fields.Boolean(required=True, description="clients hasPessimisticThoughts"), 
            "hasHopelessness": fields.Boolean(required=True, description="clients hasHopelessness"), 
            "hasSuicidalThoughts": fields.Boolean(required=True, description="clients hasSuicidalThoughts"), 
            "symptomAtRelationshipNote": NullableString(description="clients symptomAtRelationshipNote"), 
            "suicidalThoughtsNote": NullableString(description="clients suicidalThoughtsNote"), 
            # Раздел “Внутренняя картина болезни”
            "opinionPersonIllnessNote": NullableString(description="clients opinionPersonIllnessNote"), 
            "opinionOnsetOfDiseaseNote": NullableString(description="clients opinionOnsetOfDiseaseNote"),
            "opinionTreatmentNote": NullableString(description="clients opinionTreatmentNote"),
            "opinionFutureNote": NullableString(description="clients opinionFutureNote"),
            # Подраздел “Копинги”
            "copingHostsNote": NullableString(description="clients copingHostsNote"), 
            "hasActiveCopingSpecies": fields.Boolean(required=True, description="clients hasActiveCopingSpecies"),
            "hasGoodDevelopedCoping": fields.Boolean(required=True, description="clients hasGoodDevelopedCoping"),
            "copingNote": NullableString(description="clients copingNote"),
            # Подраздел “Алекситимия”
            "hasAlexithymiaPresumed": fields.Boolean(required=True, description="clients hasAlexithymiaPresumed"), 
            "alexithymiaPresumedNote": NullableString(description="clients alexithymiaPresumedNote"),
            "alexithymiaNoPresumedNote": NullableString(description="clients alexithymiaNoPresumedNote"),
            "alexithymiaNote": NullableString(description="clients alexithymiaNote"),
            # Раздел “Нарушение сна”
            "isHardToFallAsleep": fields.Boolean(required=True, description="clients isHardToFallAsleep"), 
            "hasFrequentWaking": fields.Boolean(required=True, description="clients hasFrequentWaking"),
            "isAwakeEarly": fields.Boolean(required=True, description="clients isAwakeEarly"),
            "earlyAwakeningNote": NullableString(description="clients earlyAwakeningNote"),
            "hasSleepDeprivation": fields.Boolean(required=True, description="clients hasSleepDeprivation"),
            "hasIncreasedDrowsiness": fields.Boolean(required=True, description="clients hasIncreasedDrowsiness"),
            "isCopeWithSleepDisturbancesActual": fields.String(required=True, description="clients isCopeWithSleepDisturbances", enum=[
                "bySelf",
                "withMedicine",
                "cantСope"
            ]),
            "sleepNote": NullableString(description="clients sleepNote"),
            # Раздел “Аппетит”
            "appetiteDisordersActual": fields.String(required=True, description="clients appetiteDisorders", enum=["increased", "decreased"]), 
            "appetiteRegulationActionNote": NullableString(description="clients appetiteRegulationActionNote"),
            # Раздел “Когнитивные функции”
            "cognUnderstandingOfInfoNote": NullableString(description="clients cognUnderstandingOfInfoNote"), 
            "cognMemoizationOfInfoNote": NullableString(description="clients cognMemoizationOfInfoNote"),
            "cognSpeechNote": NullableString(description="clients cognSpeechNote"),
            "cognPraxisNote": NullableString(description="clients cognPraxisNote"),
            "cognSocIntelligenceNote": NullableString(description="clients cognSocIntelligenceNote"),
            # Раздел “В беседе использовалась терапия”
            "useCognBehavTherapy": fields.Boolean(required=True, description="clients useCognBehavTherapy"), 
            "useExistentialTherapy": fields.Boolean(required=True, description="clients useExistentialTherapy"),
            "useWorkImagesTherapy": fields.Boolean(required=True, description="clients useWorkImagesTherapy"),
            "useDecisionTherapy": fields.Boolean(required=True, description="clients useDecisionTherapy"),
            "useAcceptanceTherapy": fields.Boolean(required=True, description="clients useAcceptanceTherapy"),
            "useArtTherapy": fields.Boolean(required=True, description="clients useArtTherapy"),
            "useBodilyOrientedTherapy": fields.Boolean(required=True, description="clients useBodilyOrientedTherapy"),
            "useOtherTherapy": fields.Boolean(required=True, description="clients useOtherTherapy"),
            "useOtherTherapyNote": NullableString(description="clients useOtherTherapyNote"),
            # Раздел “Заключение”
            "conclNotes": NullableString(description="clients conclNotes"), 
            "hasAdaptationDisorder": fields.Boolean(required=True, description="clients hasAdaptationDisorder"),
            "hasAnxietyDisorder": fields.Boolean(required=True, description="clients hasAnxietyDisorder"),
            "hasDepressionClinical": fields.Boolean(required=True, description="clients hasDepressionClinical"),
            "hasAcutePsyReact": fields.Boolean(required=True, description="clients hasAcutePsyReact"),
            "hasPostDisorder": fields.Boolean(required=True, description="clients hasPostDisorder"),
            "hasConclOther": fields.Boolean(required=True, description="clients hasConclOther"),
            "conclOtherNote": NullableString(description="clients conclOtherNote"),
            "conclFirstPlanNote": NullableString(description="clients conclFirstPlanNote"),
            "conclOnBackgroundNote": NullableString(description="clients conclOnBackgroundNote"),
            "hasInnerPicture": fields.Boolean(required=True, description="clients hasInnerPicture"),
            "conclTargetNote": NullableString(description="clients conclTargetNote"),
            # Раздел “Рекомендации”
            "recomNeuroStudy": fields.Boolean(required=True, description="clients recomNeuroStudy"), 
            "recomPathoStudy": fields.Boolean(required=True, description="clients recomPathoStudy"),
            "recomContactSpecialist": fields.Boolean(required=True, description="clients recomContactSpecialist"),
            "recomPassTraining": fields.Boolean(required=True, description="clients recomPassTraining"),
            "recomPassTrainingNote": NullableString(description="clients recomPassTrainingNote"),
            "recomHomework": fields.Boolean(required=True, description="clients recomHomework"),
            "recomHomeworkNote": NullableString(description="clients recomHomeworkNote"),
            "recomPsychocorrection": fields.Boolean(required=True, description="clients recomPsychocorrection"),
            "recomAdditionalPsychometry": fields.Boolean(required=True, description="clients recomAdditionalPsychometry"),
            "recomAdditionalPsychometryNote": NullableString(description="clients recomAdditionalPsychometryNote"),
        },
    )

class AuthDto:
    api = Namespace("auth", description="authentication related operations")
    user_auth = api.model(
        "auth_details",
        {
            "email": fields.String(required=True, description="The email address"),
            "password": fields.String(required=True, description="The user password"),
        },
    )


class TestDTOs:
    api = Namespace("test", description="tests related operations")
    test_creds = api.model(
        "test_creds",
        {
            "email": fields.String(required=True, description="The email address"),
            "test_id": fields.String(required=True, description="The test identifier"),
        },
    )
    test_answers_list = api.model(
        "test_answers_list",
        {
            "answerNumber" : fields.Integer(description="The test answer number"),
            "score" : fields.Integer(description="The test answer score"),
            "answerText" : fields.String(description="The test answer text"),
        },
    )
    test_creds_return = api.model(
        "test_creds_return",
        {
            "public_id" : fields.String(required=True, description="The test result identifier"),
            "user_id" : fields.String(required=True, description="User Identifier"),
            "test_id" : fields.String(required=True, description="Test type Identifier"),
            "name" : fields.String(description="The test name"),
            "questionNumber" : fields.Integer(description="Number of current question"),
            "numberOfQuestions" : fields.Integer(description="Number of questions in test"),
            "test_question_id" : fields.String(description="The test question identifier"),
            "title" : fields.String(description="The test title"),
            "questionTypeActual" : fields.String(description="The questions markup type", enum = ["Radio Button", "Checkbox", "Selector", "Text"]),
            "result_id" : fields.String(description="The test results id"),
            "test_answers" : fields.Nested(test_answers_list, description="The questions markup type", as_list = True)
        },
    )

    test_ans = api.model(
        "test_ans",
        {
            "user_id": fields.String(required=True, description="The email address"),
            "test_id": fields.String(required=True, description="The test identifier"),
            "test_question_id" : fields.String(description="The test question identifier"),
            "answerNumber" : fields.List(fields.Integer(description="The test answer number")),
        },
    )

    test_result_ret = api.model(
        "test_result_ret",
        {
            "description" : fields.String(description="The test result description"),
            "recommendation" : fields.String(description="The test result recommendation"),
            "total" : fields.Integer(description="The test total score"),
        },
    )

    test_list_return = api.model(
        "test_list_return",
        {
            "public_id" : fields.String(description="The test public_id"),
            "name" : fields.String(description="The test name"),
            "clientTypeActual" : fields.List(fields.String(description="The test clientTypeActual", enum=["patient", "staff", "relatives"], as_list = True)),
            "stageActual" : fields.String(description="The test stageActual", enum=["justDiagnosed", "cure", "therapy", "remission", "palliativeCare", "staff"]),
            "interval" : fields.Integer(description="The test interval"),
            "numberOfQuestions" : fields.Integer(description="The test numberOfQuestions"),
            "maxScore" : fields.Integer(description="The test max score"),
            "minScore" : fields.Integer(description="The test min score")
        }
    )

    test_set_return = api.model(
        "test_set_return",
        {
            "public_id" : fields.String(description="The test public_id"),
            "test_id" : fields.String(description="The test id in list"),
            "stressLevelActual" : fields.String(description="The test clientTypeActual", enum=["yellow", "red", "green"]),
            "minCount" : fields.Integer(description="The test interval min score"),
            "maxCount" : fields.Integer(description="The test interval max score"),
            "description" : fields.String(description="The test description"),
            "recommendation" : fields.String(description="The test recommendation"),
        }
    )

    test_ans_return = api.model(
        "test_ans_return",
        {
            "public_id" : fields.String(description="The test public_id"),
            "test_question_id" : fields.String(description="The test id in questions"),
            "answerNumber" : fields.Integer(description="The test answer number"),
            "score" : fields.Integer(description="The test score"),
            "answerText" : fields.String(description="The test answer text"),
        }
    )

    test_ques_return = api.model(
        "test_ques_return",
        {
            "public_id" : fields.String(description="The test public_id"),
            "test_id" : fields.String(description="The test id in list"),
            "questionNumber" : fields.Integer(description="The test question number"),
            "title" : fields.String(description="The test title"), 
            "questionTypeActual" : fields.String(description="The test questionTypeActual", enum=["radio", "checkbox", "select", "text"]),
        }
    )

    test_logs_return = api.model(
        "test_logs_return",
        {
            "public_id" : fields.String(description="The test public_id"),
            "user_id" : fields.String(description="The user id for test"),
            "test_id" : fields.String(description="The test id in list"),
            "testAnswersNumbers" : fields.String(description="The test answers numbers"),
            "gettedScore" : fields.Integer(description="The test title"), 
            "dateStart" : fields.String(description="The test date Start"),
            "dateEnd" : fields.String(description="The test date End"),
            "questionNumber" : fields.Integer(description="The test question Number"),
        }
    )

    test_ret_return = api.model(
        "test_ret_return",
        {
            "public_id" : fields.String(description="The test public_id"),
            "user_id" : fields.String(description="The user id for test"),
            "test_id" : fields.String(description="The test id in list"),
            "startDate" : fields.String(description="The test start Date"),
            "spendTime" : fields.String(description="The test spend Time"), 
            "total" : fields.Integer(description="The test total"),
            "clientFullName": fields.String(description="user FCs referenced to client"),
            "email": fields.String(required=True, description="The email address"),
            "name" : fields.String(description="The test name")
        }
    )

    test_ret_return_with_logs = api.model(
        "test_ret_return_with_logs",
        {
            "public_id" : fields.String(description="The test public_id"),
            "user_id" : fields.String(description="The user id for test"),
            "test_id" : fields.String(description="The test id in list"),
            "startDate" : fields.String(description="The test start Date"),
            "spendTime" : fields.String(description="The test spend Time"), 
            "total" : fields.Integer(description="The test total"),
            "linked_logs" : fields.Nested(test_logs_return, description="The logs markup type", as_list = True)
        }
    )