"""empty message

Revision ID: 83d902250d30
Revises: 
Create Date: 2024-05-17 17:35:50.617740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83d902250d30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('testsList',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('stageActual', sa.Enum('justDiagnosed', 'cure', 'therapy', 'remission', 'palliativeCare', name='stagesenum'), nullable=False),
    sa.Column('interval', sa.Integer(), nullable=True),
    sa.Column('numberOfQuestions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('firstName', sa.String(length=255), nullable=False),
    sa.Column('lastName', sa.String(length=255), nullable=False),
    sa.Column('middleName', sa.String(length=255), nullable=True),
    sa.Column('userTypeActual', sa.Enum('client', 'employer', name='usertypeenum'), nullable=True),
    sa.Column('statusActual', sa.Enum('new', 'failed_val', 'success_val', 'active', 'blocked', 'archive', name='statusenum'), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phoneNumber', sa.String(length=255), nullable=False),
    sa.Column('sexActual', sa.Enum('male', 'female', name='sexenum'), nullable=False),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('blocked', sa.Boolean(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('created'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phoneNumber'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('aggrement',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('hasTGAggrement', sa.Boolean(), nullable=False),
    sa.Column('hasMailAggrement', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('public_user_id', sa.String(length=100), nullable=False),
    sa.Column('clientEmail', sa.String(length=100), nullable=False),
    sa.Column('clientFullName', sa.String(length=100), nullable=False),
    sa.Column('clientCreated', sa.DateTime(), nullable=False),
    sa.Column('clientTypeActual', sa.Enum('patient', 'staff', 'relatives', name='clienttypeenum'), nullable=False),
    sa.Column('diseaseLocation', sa.String(length=255), nullable=True),
    sa.Column('stageActual', sa.Enum('justDiagnosed', 'cure', 'therapy', 'remission', 'palliativeCare', name='stagesenum'), nullable=True),
    sa.Column('monthsAfterTreatment', sa.String(length=255), nullable=True),
    sa.Column('workWithPsychologist', sa.Boolean(), nullable=True),
    sa.Column('experienceTypeActual', sa.Enum('positive', 'neutral', 'negative', name='experiencetypeenum'), nullable=True),
    sa.Column('experienceDescription', sa.String(length=255), nullable=True),
    sa.Column('duration', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['clientCreated'], ['user.created'], ),
    sa.ForeignKeyConstraint(['clientEmail'], ['user.email'], ),
    sa.ForeignKeyConstraint(['public_user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('clientCreated'),
    sa.UniqueConstraint('clientEmail'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('public_user_id')
    )
    op.create_table('consultationcard',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('validationStatusActual', sa.Enum('blueprint', 'validated', name='validationstatusenum'), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('publicUserClientId', sa.String(length=100), nullable=False),
    sa.Column('clientFullName', sa.String(length=100), nullable=False),
    sa.Column('clientEmail', sa.String(length=100), nullable=False),
    sa.Column('publicSpecialistId', sa.String(length=100), nullable=False),
    sa.Column('specialistFullName', sa.String(length=100), nullable=False),
    sa.Column('statusConsultationActual', sa.Enum('first', 'second', name='statusconsultationenum'), nullable=True),
    sa.Column('comPsychoEmotionNote', sa.String(length=100), nullable=True),
    sa.Column('comSomatic', sa.String(length=100), nullable=True),
    sa.Column('comSocial', sa.String(length=100), nullable=True),
    sa.Column('oncologyTime', sa.String(length=100), nullable=True),
    sa.Column('emotionReactOnco', sa.String(length=100), nullable=True),
    sa.Column('experiencingEmotion', sa.String(length=100), nullable=True),
    sa.Column('usuallyHelpEmotion', sa.String(length=100), nullable=True),
    sa.Column('usuallyNoHelpEmotion', sa.String(length=100), nullable=True),
    sa.Column('hasConnectionPsychotrauma', sa.Boolean(), nullable=True),
    sa.Column('connectionPsychotraumaNote', sa.String(length=100), nullable=True),
    sa.Column('featuresConversationsNote', sa.String(length=100), nullable=True),
    sa.Column('hasAnxiety', sa.Boolean(), nullable=True),
    sa.Column('hasContinuousDuration', sa.Boolean(), nullable=True),
    sa.Column('hasPersistentLowMood', sa.Boolean(), nullable=True),
    sa.Column('hasLossInterest', sa.Boolean(), nullable=True),
    sa.Column('hasEnergyDecline', sa.Boolean(), nullable=True),
    sa.Column('hasDecliningAttention', sa.Boolean(), nullable=True),
    sa.Column('hasGuilt', sa.Boolean(), nullable=True),
    sa.Column('hasLowerSelfesteem', sa.Boolean(), nullable=True),
    sa.Column('hasAppetiteChange', sa.Boolean(), nullable=True),
    sa.Column('hasSleepDisturbance', sa.Boolean(), nullable=True),
    sa.Column('hasPessimisticThoughts', sa.Boolean(), nullable=True),
    sa.Column('hasHopelessness', sa.Boolean(), nullable=True),
    sa.Column('hasSuicidalThoughts', sa.Boolean(), nullable=True),
    sa.Column('symptomAtRelationshipNote', sa.String(length=100), nullable=True),
    sa.Column('suicidalThoughtsNote', sa.String(length=100), nullable=True),
    sa.Column('opinionPersonIllnessNote', sa.String(length=100), nullable=True),
    sa.Column('opinionOnsetOfDiseaseNote', sa.String(length=100), nullable=True),
    sa.Column('opinionTreatmentNote', sa.String(length=100), nullable=True),
    sa.Column('opinionFutureNote', sa.String(length=100), nullable=True),
    sa.Column('copingHostsNote', sa.String(length=100), nullable=True),
    sa.Column('hasActiveCopingSpecies', sa.Boolean(), nullable=True),
    sa.Column('hasGoodDevelopedCoping', sa.Boolean(), nullable=True),
    sa.Column('copingNote', sa.String(length=100), nullable=True),
    sa.Column('hasAlexithymiaPresumed', sa.Boolean(), nullable=True),
    sa.Column('alexithymiaPresumedNote', sa.String(length=100), nullable=True),
    sa.Column('alexithymiaNoPresumedNote', sa.String(length=100), nullable=True),
    sa.Column('alexithymiaNote', sa.String(length=100), nullable=True),
    sa.Column('isHardToFallAsleep', sa.Boolean(), nullable=True),
    sa.Column('hasFrequentWaking', sa.Boolean(), nullable=True),
    sa.Column('isAwakeEarly', sa.Boolean(), nullable=True),
    sa.Column('earlyAwakeningNote', sa.String(length=100), nullable=True),
    sa.Column('hasSleepDeprivation', sa.Boolean(), nullable=True),
    sa.Column('hasIncreasedDrowsiness', sa.Boolean(), nullable=True),
    sa.Column('isCopeWithSleepDisturbancesActual', sa.Enum('bySelf', 'withMedicine', 'cantСope', name='copewithsleepdisturbancesenum'), nullable=True),
    sa.Column('sleepNote', sa.String(length=100), nullable=True),
    sa.Column('appetiteDisordersActual', sa.Enum('increased', 'decreased', name='appetitedisordersenum'), nullable=True),
    sa.Column('appetiteRegulationActionNote', sa.String(length=100), nullable=True),
    sa.Column('cognUnderstandingOfInfoNote', sa.String(length=100), nullable=True),
    sa.Column('cognMemoizationOfInfoNote', sa.String(length=100), nullable=True),
    sa.Column('cognSpeechNote', sa.String(length=100), nullable=True),
    sa.Column('cognPraxisNote', sa.String(length=100), nullable=True),
    sa.Column('cognSocIntelligenceNote', sa.String(length=100), nullable=True),
    sa.Column('useCognBehavTherapy', sa.Boolean(), nullable=True),
    sa.Column('useExistentialTherapy', sa.Boolean(), nullable=True),
    sa.Column('useWorkImagesTherapy', sa.Boolean(), nullable=True),
    sa.Column('useDecisionTherapy', sa.Boolean(), nullable=True),
    sa.Column('useAcceptanceTherapy', sa.Boolean(), nullable=True),
    sa.Column('useArtTherapy', sa.Boolean(), nullable=True),
    sa.Column('useBodilyOrientedTherapy', sa.Boolean(), nullable=True),
    sa.Column('useOtherTherapy', sa.Boolean(), nullable=True),
    sa.Column('useOtherTherapyNote', sa.String(length=100), nullable=True),
    sa.Column('conclNotes', sa.String(length=100), nullable=True),
    sa.Column('hasAdaptationDisorder', sa.Boolean(), nullable=True),
    sa.Column('hasAnxietyDisorder', sa.Boolean(), nullable=True),
    sa.Column('hasDepressionClinical', sa.Boolean(), nullable=True),
    sa.Column('hasAcutePsyReact', sa.Boolean(), nullable=True),
    sa.Column('hasPostDisorder', sa.Boolean(), nullable=True),
    sa.Column('hasConclOther', sa.Boolean(), nullable=True),
    sa.Column('conclOtherNote', sa.String(length=100), nullable=True),
    sa.Column('conclFirstPlanNote', sa.String(length=100), nullable=True),
    sa.Column('conclOnBackgroundNote', sa.String(length=100), nullable=True),
    sa.Column('hasInnerPicture', sa.Boolean(), nullable=True),
    sa.Column('conclTargetNote', sa.String(length=100), nullable=True),
    sa.Column('recomNeuroStudy', sa.Boolean(), nullable=True),
    sa.Column('recomPathoStudy', sa.Boolean(), nullable=True),
    sa.Column('recomContactSpecialist', sa.Boolean(), nullable=True),
    sa.Column('recomPassTraining', sa.Boolean(), nullable=True),
    sa.Column('recomPassTrainingNote', sa.String(length=100), nullable=True),
    sa.Column('recomHomework', sa.Boolean(), nullable=True),
    sa.Column('recomHomeworkNote', sa.String(length=100), nullable=True),
    sa.Column('recomPsychocorrection', sa.Boolean(), nullable=True),
    sa.Column('recomAdditionalPsychometry', sa.Boolean(), nullable=True),
    sa.Column('recomAdditionalPsychometryNote', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['clientEmail'], ['user.email'], ),
    sa.ForeignKeyConstraint(['publicSpecialistId'], ['user.public_id'], ),
    sa.ForeignKeyConstraint(['publicUserClientId'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('notificationJournal',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('test_id', sa.String(length=100), nullable=False),
    sa.Column('sendNextTime', sa.DateTime(), nullable=False),
    sa.Column('testIsFinished', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['test_id'], ['testsList.public_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('notificationLog',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('chanel', sa.Enum('telegramm', 'mail', name='chaneltypeenum'), nullable=False),
    sa.Column('tgChatId', sa.String(length=100), nullable=True),
    sa.Column('status', sa.Enum('send', 'not_send', name='sendingstatusenum'), nullable=False),
    sa.Column('sendTime', sa.DateTime(), nullable=False),
    sa.Column('errorDescription', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('test2id',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('test_id', sa.String(length=100), nullable=False),
    sa.Column('clientTypeActual', sa.Enum('patient', 'staff', 'relatives', name='clienttypeenum'), nullable=False),
    sa.ForeignKeyConstraint(['test_id'], ['testsList.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('testLog',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('test_id', sa.String(length=100), nullable=False),
    sa.Column('testAnswersNumbers', sa.String(length=100), nullable=True),
    sa.Column('gettedScore', sa.Integer(), nullable=True),
    sa.Column('dateStart', sa.DateTime(), nullable=False),
    sa.Column('dateEnd', sa.DateTime(), nullable=True),
    sa.Column('questionNumber', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['test_id'], ['testsList.public_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('testQuestion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('test_id', sa.String(length=100), nullable=False),
    sa.Column('questionNumber', sa.BigInteger(), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('questionTypeActual', sa.Enum('radio', 'checkbox', 'select', 'text', name='questiontypeenum'), nullable=False),
    sa.ForeignKeyConstraint(['test_id'], ['testsList.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('testResult',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('test_id', sa.String(length=100), nullable=False),
    sa.Column('startDate', sa.DateTime(), nullable=False),
    sa.Column('spendTime', sa.Interval(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['test_id'], ['testsList.public_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('testSettings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('test_id', sa.String(length=100), nullable=False),
    sa.Column('stressLevelActual', sa.Enum('green', 'yellow', 'red', name='stresslevelenum'), nullable=False),
    sa.Column('minCount', sa.Integer(), nullable=True),
    sa.Column('maxCount', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('recommendation', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['test_id'], ['testsList.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('clients_cure',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('public_client_id', sa.String(length=100), nullable=False),
    sa.Column('cureType', sa.Enum('chem', 'ray', 'surgery', 'target', 'hormon', 'palliative', name='curetypeenum'), nullable=False),
    sa.ForeignKeyConstraint(['public_client_id'], ['client.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('clients_recomendation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('public_client_id', sa.String(length=100), nullable=False),
    sa.Column('recomendationType', sa.Enum('info', 'exercises', 'support', 'work', 'other', name='recomendationtypeenum'), nullable=False),
    sa.Column('recomendationDescription', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['public_client_id'], ['client.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('testAnswer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('test_question_id', sa.String(length=100), nullable=False),
    sa.Column('answerNumber', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('answerText', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['test_question_id'], ['testQuestion.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testAnswer')
    op.drop_table('clients_recomendation')
    op.drop_table('clients_cure')
    op.drop_table('testSettings')
    op.drop_table('testResult')
    op.drop_table('testQuestion')
    op.drop_table('testLog')
    op.drop_table('test2id')
    op.drop_table('notificationLog')
    op.drop_table('notificationJournal')
    op.drop_table('consultationcard')
    op.drop_table('client')
    op.drop_table('aggrement')
    op.drop_table('user')
    op.drop_table('testsList')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###