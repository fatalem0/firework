from src.models.user import User
from src.models.tests.tests_list import TestsList
from src.models.tests.test_question import TestQuestion
from src.models.tests.test_answer import TestAnswer
from src.models.tests.test_settings import TestSettings
from src.models.tests.test_type_to_id import TestsType2Id
from datetime import datetime
from src.db import db
import uuid

import time
from src import create_app
import os


def execute_data():
    start = datetime.now()
    print("Started adding data at", start)

    user_count = User.query.count()
    if user_count > 0:
        print('User(test1@test.com) for this database already exists')
    else:
        user = User(
                public_id=str(uuid.uuid4()),
                email="test1@test.com",
                firstName="Иван",
                lastName="Иванов",
                phoneNumber="8(999)999-99-99",
                password="test",
                sexActual="male",
                blocked=False,
                userTypeActual="employer",
                admin = True
            )
        save(user)
        db.session.commit()

    test1 = TestsList.query.filter_by(name = "Дистресс термометр").first()
    if test1:
        print('Test(Дистресс термометр) for this database already exists')
    else:
        test = TestsList(
            public_id=str(uuid.uuid4()),
            name="Дистресс термометр",
            stageActual="justDiagnosed",
            interval=10,
            numberOfQuestions=7
        )
        save(test)

        test_id = TestsList.query.filter_by(name = "Дистресс термометр").first().public_id

        type2id = TestsType2Id(
            public_id=str(uuid.uuid4()),
            clientTypeActual="patient",
            test_id = test_id
        )

        save(type2id)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=1,
            title="Насколько сильно вы чувствовали стресс (напряжение) на протяжении последней недели, включая сегодняшний день",
            questionTypeActual="select"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 1).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="1"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="2"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="3"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="4"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=5,
            score=5,
            answerText="5"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=6,
            score=6,
            answerText="6"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=7,
            score=7,
            answerText="7"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=8,
            score=8,
            answerText="8"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=9,
            score=9,
            answerText="9"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=10,
            score=10,
            answerText="10"
        )
        save(testAnswer)


        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=2,
            title="Общие проблемы",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 2).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=0,
            answerText="Работа по дому"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=0,
            answerText="Финансы/страхование"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=0,
            answerText="Транспорт"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=0,
            answerText="Работа/учеба"
        )
        save(testAnswer)


        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=3,
            title="Физические проблемы",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 3).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=0,
            answerText="Мытье/Одевание"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=0,
            answerText="Дыхание"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=0,
            answerText="Мочеиспускание"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=0,
            answerText="Запор"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=5,
            score=0,
            answerText="Усталость"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=6,
            score=0,
            answerText="Отеки"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=7,
            score=0,
            answerText="Несварение желудка"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=8,
            score=0,
            answerText="Память/концентрация"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=9,
            score=0,
            answerText="Язвы во рту"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=10,
            score=0,
            answerText="Тошнота"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=11,
            score=0,
            answerText="Заложенность/сухость носа"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=12,
            score=0,
            answerText="Секс"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=13,
            score=0,
            answerText="Сон"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=14,
            score=0,
            answerText="Покалывание в руках\ногах"
        )
        save(testAnswer)


        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=4,
            title="Семейные проблемы",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 4).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=0,
            answerText="Взаимодействие с детьми"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=0,
            answerText="Взаимодействие с партнером"
        )
        save(testAnswer)


        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=5,
            title="Эмоциональные проблемы",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 5).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=0,
            answerText="Депрессия"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=0,
            answerText="Страх"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=0,
            answerText="Нервозность"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=0,
            answerText="Тоска"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=5,
            score=0,
            answerText="Беспокойство"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=6,
            score=0,
            answerText="Потеря интереса к обычной активности"
        )
        save(testAnswer)


        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=6,
            title="Духовная/религиозная обеспокоенность",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 6).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=0,
            answerText="Духовная/религиозная обеспокоенность"
        )
        save(testAnswer)


        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=7,
            title="Другие проблемы",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 7).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=0,
            answerText="Опишите проблему"
        )
        save(testAnswer)


        testSettings = TestSettings(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            stressLevelActual="green",
            minCount=0,
            maxCount=1,
            description="Нормальный стресс",
            recommendation="Достаточно чтобы была поддержка семьи и друзей"
        )
        save(testSettings)
        testSettings = TestSettings(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            stressLevelActual="green",
            minCount=2,
            maxCount=3,
            description="Низкий стресс",
            recommendation="Нужна поддержка от лечащего врача и др. медицинских специалистов"
        )
        save(testSettings)
        testSettings = TestSettings(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            stressLevelActual="yellow",
            minCount=4,
            maxCount=5,
            description="Средний стресс",
            recommendation="Требуется дополнительная психологическая поддержка, поведенческая и духовная"
        )
        save(testSettings)
        testSettings = TestSettings(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            stressLevelActual="red",
            minCount=6,
            maxCount=10,
            description="Высокий стресс",
            recommendation="Необходима психотерапия немедикаментозная и медикаментозная (по необходимости)"
        )
        save(testSettings)


    test2 = TestsList.query.filter_by(name = "Тест тревожности Спилбергера Ханина").first()
    if test2:
        print('Test(Тест тревожности Спилбергера Ханина) for this database already exists')
    else:
        test = TestsList(
            public_id=str(uuid.uuid4()),
            name="Тест тревожности Спилбергера Ханина",
            stageActual="justDiagnosed",
            interval=10,
            numberOfQuestions=40
        )
        save(test)

        test_id = TestsList.query.filter_by(name = "Тест тревожности Спилбергера Ханина").first().public_id

        type2id = TestsType2Id(
            public_id=str(uuid.uuid4()),
            clientTypeActual="patient",
            test_id = test_id
        )

        save(type2id)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=1,
            title="Я спокоен",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 1).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=1,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=2,
            answerText="Почти всегда"
        )
        save(testAnswer)

        
        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=2,
            title="Мне ничто не угрожает",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 2).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=1,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=2,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=3,
            title="Я нахожусь в напряжении",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 3).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=4,
            title="Я внутренне скован",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 4).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=5,
            title="Я чувствую себя свободно",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 5).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=1,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=2,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=6,
            title="Я расстроен",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 6).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=7,
            title="Меня волнуют возможные неудачи",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 7).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=8,
            title="Я ощущаю душевный покой",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 8).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=9,
            title="Я встревожен",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 9).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=10,
            title="Я испытываю чувство внутреннего удовлетворения",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 10).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=11,
            title="Я уверен в себе",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 11).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=12,
            title="Я нервничаю",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 12).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=13,
            title="Я не нахожу себе места",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 13).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=14,
            title="Я взвинчен",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 14).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=15,
            title="Я не чувствую скованности, напряжения",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 15).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=1,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=2,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=16,
            title="Я доволен",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 16).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=1,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=2,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=17,
            title="Я озабочен",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 17).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=18,
            title="Я слишком возбужден и мне не по себе",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 18).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=4,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=3,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=19,
            title="Мне радостно",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 19).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=1,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=2,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=20,
            title="Мне приятно",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 20).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=1,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=2,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=21,
            title="У меня бывает приподнятое настроение",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 21).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=3,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=1,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=22,
            title="Я бываю раздражительным",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 22).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=23,
            title="Я легко расстраиваюсь",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 23).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=24,
            title="Я хотел бы быть таким же удачливым, как и другие",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 24).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=25,
            title="Я сильно переживаю неприятности и долго не могу о них забыть",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 25).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=26,
            title="Я чувствую прилив сил и желание работать",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 26).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=3,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=1,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=27,
            title="Я спокоен, хладнокровен и собран",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 27).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=3,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=1,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=28,
            title="Меня тревожат возможные трудности",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 28).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=29,
            title="Я слишком переживаю из-за пустяков",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 29).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=30,
            title="Я бываю вполне счастлив",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 30).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=3,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=1,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=31,
            title="Я все принимаю близко к сердцу",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 31).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=32,
            title="Мне не хватает уверенности в себе",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 32).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=33,
            title="Я чувствую себя беззащитным",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 33).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=34,
            title="Я стараюсь избегать критических ситуаций и трудностей",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 34).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=35,
            title="У меня бывает хандра",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 35).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=36,
            title="Я бываю доволен",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 36).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=3,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=1,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=37,
            title="Всякие пустяки отвлекают и волнуют меня",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 37).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=38,
            title="Бывает, что я чувствую себя неудачником",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 38).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=39,
            title="Я уравновешенный человек",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 39).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=4,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=3,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=2,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=1,
            answerText="Почти всегда"
        )
        save(testAnswer)

        testQuestion = TestQuestion(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            questionNumber=40,
            title="Меня охватывает беспокойство, когда я думаю о своих делах и заботах",
            questionTypeActual="checkbox"
        )
        save(testQuestion)
        test_question_id = TestQuestion.query.filter_by(test_id = test_id, questionNumber = 40).first().public_id
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=1,
            score=1,
            answerText="Никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=2,
            score=2,
            answerText="Почти никогда"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=3,
            score=3,
            answerText="Часто"
        )
        save(testAnswer)
        testAnswer = TestAnswer(
            public_id=str(uuid.uuid4()),
            test_question_id=test_question_id,
            answerNumber=4,
            score=4,
            answerText="Почти всегда"
        )
        save(testAnswer)


        testSettings = TestSettings(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            stressLevelActual="green",
            minCount=0,
            maxCount=30,
            description="Низкая тревожность",
            recommendation=""
        )
        save(testSettings)
        testSettings = TestSettings(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            stressLevelActual="yellow",
            minCount=31,
            maxCount=44,
            description="Умеренная тревожность",
            recommendation=""
        )
        save(testSettings)
        testSettings = TestSettings(
            public_id=str(uuid.uuid4()),
            test_id=test_id,
            stressLevelActual="red",
            minCount=45,
            maxCount=90,
            description="Высокий уровень тревожности",
            recommendation=""
        )
        save(testSettings)


    ended = datetime.now()
    print('Ended adding data at', ended)



def save(data):
    db.session.add(data)
    db.session.commit()
        

def main():
    time.sleep(10)
    app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")

    with app.app_context():
        execute_data()

if __name__ == "__main__":
    main()