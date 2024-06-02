from src.db import db
import datetime
from src.model.enums import statusConsultationEnum, copeWithSleepDisturbancesEnum, appetiteDisordersEnum, validationStatusEnum
from sqlalchemy import Enum

class ConsultationCard(db.Model):
    """Consultation Card Model for storing card related details"""

    __tablename__ = "consultationcard"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    validationStatusActual = db.Column(Enum(validationStatusEnum), nullable = False, default = validationStatusEnum.blueprint)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    publicUserClientId = db.Column(
        db.String(100),
        db.ForeignKey('user.public_id'), 
        nullable=False)
    clientFullName = db.Column(db.String(100), nullable=False)
    clientEmail = db.Column(
        db.String(100),
        db.ForeignKey('user.email'), 
        nullable=False)
    publicSpecialistId = db.Column(
        db.String(100),
        db.ForeignKey('user.public_id'), 
        nullable=False)
    specialistFullName = db.Column(db.String(100), nullable=False)
    statusConsultationActual = db.Column(Enum(statusConsultationEnum))
    comPsychoEmotionNote = db.Column(db.String(100))
    comSomatic = db.Column(db.String(100))
    comSocial = db.Column(db.String(100))
    oncologyTime = db.Column(db.String(100))
    emotionReactOnco = db.Column(db.String(100))
    experiencingEmotion = db.Column(db.String(100))
    usuallyHelpEmotion = db.Column(db.String(100))
    usuallyNoHelpEmotion = db.Column(db.String(100))
    hasConnectionPsychotrauma = db.Column(db.Boolean)
    connectionPsychotraumaNote = db.Column(db.String(100))
    featuresConversationsNote = db.Column(db.String(100))
    hasAnxiety = db.Column(db.Boolean)
    hasContinuousDuration = db.Column(db.Boolean)
    hasPersistentLowMood = db.Column(db.Boolean)
    hasLossInterest = db.Column(db.Boolean)
    hasEnergyDecline = db.Column(db.Boolean)
    hasDecliningAttention = db.Column(db.Boolean)
    hasGuilt = db.Column(db.Boolean)
    hasLowerSelfesteem = db.Column(db.Boolean)
    hasAppetiteChange = db.Column(db.Boolean)
    hasSleepDisturbance = db.Column(db.Boolean)
    hasPessimisticThoughts = db.Column(db.Boolean)
    hasHopelessness = db.Column(db.Boolean)
    hasSuicidalThoughts = db.Column(db.Boolean)
    symptomAtRelationshipNote = db.Column(db.String(100))
    suicidalThoughtsNote = db.Column(db.String(100))
    opinionPersonIllnessNote = db.Column(db.String(100))
    opinionOnsetOfDiseaseNote = db.Column(db.String(100))
    opinionTreatmentNote = db.Column(db.String(100))
    opinionFutureNote = db.Column(db.String(100))
    copingHostsNote = db.Column(db.String(100))
    hasActiveCopingSpecies = db.Column(db.Boolean)
    hasGoodDevelopedCoping = db.Column(db.Boolean)
    copingNote = db.Column(db.String(100))
    hasAlexithymiaPresumed = db.Column(db.Boolean)
    alexithymiaPresumedNote = db.Column(db.String(100))
    alexithymiaNoPresumedNote = db.Column(db.String(100))
    alexithymiaNote = db.Column(db.String(100))
    isHardToFallAsleep = db.Column(db.Boolean)
    hasFrequentWaking = db.Column(db.Boolean)
    isAwakeEarly = db.Column(db.Boolean)
    earlyAwakeningNote = db.Column(db.String(100))
    hasSleepDeprivation = db.Column(db.Boolean)
    hasIncreasedDrowsiness = db.Column(db.Boolean)
    isCopeWithSleepDisturbancesActual = db.Column(Enum(copeWithSleepDisturbancesEnum))
    sleepNote = db.Column(db.String(100))
    appetiteDisordersActual = db.Column(Enum(appetiteDisordersEnum))
    appetiteRegulationActionNote = db.Column(db.String(100))
    cognUnderstandingOfInfoNote = db.Column(db.String(100))
    cognMemoizationOfInfoNote = db.Column(db.String(100))
    cognSpeechNote = db.Column(db.String(100))
    cognPraxisNote = db.Column(db.String(100))
    cognSocIntelligenceNote = db.Column(db.String(100))
    useCognBehavTherapy = db.Column(db.Boolean)
    useExistentialTherapy = db.Column(db.Boolean)
    useWorkImagesTherapy = db.Column(db.Boolean)
    useDecisionTherapy = db.Column(db.Boolean)
    useAcceptanceTherapy = db.Column(db.Boolean)
    useArtTherapy = db.Column(db.Boolean)
    useBodilyOrientedTherapy = db.Column(db.Boolean)
    useOtherTherapy = db.Column(db.Boolean)
    useOtherTherapyNote = db.Column(db.String(100))
    conclNotes = db.Column(db.String(100))
    hasAdaptationDisorder = db.Column(db.Boolean)
    hasAnxietyDisorder = db.Column(db.Boolean)
    hasDepressionClinical = db.Column(db.Boolean)
    hasAcutePsyReact = db.Column(db.Boolean)
    hasPostDisorder = db.Column(db.Boolean)
    hasConclOther = db.Column(db.Boolean)
    conclOtherNote = db.Column(db.String(100))
    conclFirstPlanNote = db.Column(db.String(100))
    conclOnBackgroundNote = db.Column(db.String(100))
    hasInnerPicture = db.Column(db.Boolean)
    conclTargetNote = db.Column(db.String(100))
    recomNeuroStudy = db.Column(db.Boolean)
    recomPathoStudy = db.Column(db.Boolean)
    recomContactSpecialist = db.Column(db.Boolean)
    recomPassTraining = db.Column(db.Boolean)
    recomPassTrainingNote = db.Column(db.String(100))
    recomHomework = db.Column(db.Boolean)
    recomHomeworkNote = db.Column(db.String(100))
    recomPsychocorrection = db.Column(db.Boolean)
    recomAdditionalPsychometry = db.Column(db.Boolean)
    recomAdditionalPsychometryNote = db.Column(db.String(100))

    def __repr__(self):
        return "<Consultation Card '{}'>".format(self.public_id)
    
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
