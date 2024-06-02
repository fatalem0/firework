import uuid
import datetime

from sqlalchemy import and_

from src.db import db
from src.model.tests.test_result import TestResult
from src.model.tests.test_log import TestLog
from src.model.tests.tests_list import TestsList
from src.model.tests.test_question import TestQuestion
from src.model.tests.test_answer import TestAnswer
from src.model.tests.test_settings import TestSettings
from src.model.tests.test_type_to_id import TestsType2Id
from src.model.user import User
from src.model.client import Client
from typing import Dict, Tuple
from src.model.notifications.notificationJournal import NotificationJournal
from src.model.notifications.notificationLogs import NotificationLog

def find_test(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(email = data["email"]).first()
    client = Client.query.filter_by(public_user_id = user.public_id).first()
    testsList = TestsList.query.filter_by(public_id = data["test_id"]).first()
    type2idEntities = TestsType2Id.query.filter_by(test_id = data["test_id"]).all()
    testTypes = []
    for type2idEntity in type2idEntities:
        testTypes.append(type2idEntity.clientTypeActual)

    if testsList and client and client.clientTypeActual in testTypes:
        if user:
            Test = TestResult.query.filter_by(test_id = data["test_id"], user_id = user.public_id, spendTime = datetime.timedelta()).order_by(TestResult.startDate.desc()).first()
            if not Test:
                Test = TestResult(
                    public_id = str(uuid.uuid4()),
                    user_id = user.public_id,
                    test_id = data["test_id"],
                    startDate = datetime.datetime.utcnow(),
                    spendTime = datetime.timedelta(),
                    total = 0
                )
                save_changes(Test)
                testLog = TestLog(
                    public_id = str(uuid.uuid4()),
                    user_id = user.public_id,
                    test_id = data["test_id"],
                    dateStart = datetime.datetime.utcnow(),
                    gettedScore = 0,
                    questionNumber = 1
                )
                save_changes(testLog)

                notification = NotificationJournal.query.filter_by(user_id = user.public_id, test_id = data["test_id"]).first()
                if not notification:
                    notification = NotificationJournal(
                        public_id = str(uuid.uuid4()),
                        user_id = user.public_id,
                        test_id = data["test_id"],
                        sendNextTime = testLog.dateStart + datetime.timedelta(days=7),
                        testIsFinished = False
                    )
                else:
                    notification.testIsFinished = False
                    notification.sendNextTime = testLog.dateStart + datetime.timedelta(day=7)
                save_changes(notification)
            else:
                testLogPrev = TestLog.query.filter_by(test_id = data["test_id"], user_id = user.public_id).order_by(TestLog.dateStart.desc()).first()
                if testLogPrev.dateEnd and testLogPrev.questionNumber != testsList.numberOfQuestions:
                    testLog = TestLog(
                        public_id = str(uuid.uuid4()),
                        user_id = user.public_id,
                        test_id = data["test_id"],
                        dateStart = datetime.datetime.utcnow(),
                        gettedScore = testLogPrev.gettedScore,
                        questionNumber = testLogPrev.questionNumber + 1
                        )
                    save_changes(testLog)
                else:
                    testLog = testLogPrev
            questionNum = 0
            if testLog.questionNumber == testsList.numberOfQuestions and testLog.dateEnd:
                questionNum = -1  
            elif testLog.dateEnd:
                questionNum = testLog.questionNumber + 1  
            else:
                questionNum = testLog.questionNumber
            testQuestion = TestQuestion.query.filter_by(test_id = data["test_id"], questionNumber = questionNum).first() if questionNum != -1 else None
            if testQuestion:
                test_answers = TestAnswer.query.filter_by(test_question_id = testQuestion.public_id).all()
                response_object = {
                            "public_id" : Test.public_id,
                            "user_id" : Test.user_id, 
                            "test_id" : Test.test_id, 
                            "name" : testsList.name,
                            "questionNumber" : questionNum,
                            "numberOfQuestions" : testsList.numberOfQuestions,
                            "test_question_id" : testQuestion.public_id,
                            "title" : testQuestion.title,
                            "questionTypeActual" : testQuestion.questionTypeActual.value,
                            "result_id" : Test.public_id,
                            "test_answers" : test_answers
                    }
            else:
                response_object = {
                            "id" : Test.public_id,
                            "user_id" : Test.user_id, 
                            "test_id" : Test.test_id, 
                            "name" : testsList.name,
                            "questionNumber" : questionNum,
                            "numberOfQuestions" : testsList.numberOfQuestions,
                            "result_id" : Test.public_id,
                    }
            return response_object, 200
        else:
            response_object = {
                "status": "fail",
                "message": "Пользователь не найден.",
            }
            return response_object, 400
    else:
        response_object = {
            "status": "fail",
            "message": "Тест не найден.",
        }
        return response_object, 401

def answer(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    answerNumberList = data["answerNumber"]
    answerList = []
    testQuestion = TestQuestion.query.filter_by(public_id = data["test_question_id"]).first()
    testLog = TestLog.query.filter_by(test_id = data["test_id"], user_id = data["user_id"]).order_by(TestLog.dateStart.desc()).first()
    for answerNumber in answerNumberList:
        answerEntity = TestAnswer.query.filter_by(test_question_id = data["test_question_id"], answerNumber = answerNumber).first()
        if answerEntity:
            answerList.append(answerEntity)
        else:
            response_object = {
                "status": "fail",
                "message": "Ответ не найден.",
            }
            return response_object, 400
        
    if testLog:
        if testQuestion:
            answerNumberList = []
            for answerEntity in answerList:
                testLog.gettedScore = testLog.gettedScore + answerEntity.score
                answerNumberList.append(answerEntity.answerNumber)
            testLog.testAnswersNumbers = ', '.join(map(str, answerNumberList))
            testLog.questionNumber = testQuestion.questionNumber
            testLog.dateEnd = datetime.datetime.utcnow()
            save_changes(testLog)

            response_object = {
                    "status": "success",
                    "message": "Ответ принят.",
                }
            return response_object, 200
        else:
            response_object = {
                "status": "fail",
                "message": "Вопрос не найден.",
            }
            return response_object, 400
    else:
        response_object = {
                "status": "fail",
                "message": "Лог теста не найден.",
            }
        return response_object, 400


def get_a_result(public_id : str) -> Tuple[Dict[str, str], int]:
    Test = TestResult.query.filter_by(public_id = public_id).first()
    if Test:
        testLog = TestLog.query.filter_by(test_id = Test.test_id, user_id = Test.user_id).order_by(TestLog.dateStart.desc()).first()
        if testLog:
            Test.spendTime = datetime.datetime.utcnow() - Test.startDate
            Test.total = testLog.gettedScore
            save_changes(Test)

            test_type = TestsList.query.filter_by(public_id = Test.test_id).first()
            notification = NotificationJournal.query.filter_by(user_id = Test.user_id, test_id = Test.test_id).first()
            notification.sendNextTime = Test.startDate + Test.spendTime + datetime.timedelta(days=test_type.interval)
            notification.testIsFinished = True
            save_changes(notification)

            testSettings = TestSettings.query.filter(and_(TestSettings.test_id == Test.test_id, TestSettings.minCount <= Test.total, TestSettings.maxCount >= Test.total)).first()
            if testSettings:
                response_object = response_object = {
                        "description" : testSettings.description,
                        "recommendation" : testSettings.recommendation,
                        "total" : Test.total,
                }
                return response_object, 200
            else:
                response_object = {
                        "status": "fail",
                        "message": "Настроек теста не найдено.",
                    }
                return response_object, 402
        else:
            response_object = {
                    "status": "fail",
                    "message": "Лог теста не найден.",
                }
            return response_object, 401
    else:
        response_object = {
                "status": "fail",
                "message": "Результат теста не найден.",
            }
        return response_object, 400

def save_changes(data) -> None:
    db.session.add(data)
    db.session.commit()

def get_a_result_with_logs(public_id : str) -> Tuple[Dict[str, str], int]:
    Test = TestResult.query.filter_by(public_id = public_id).first()
    if Test:
        logs = TestLog.query.filter(and_(TestLog.test_id == Test.test_id, TestLog.user_id == Test.user_id, TestLog.dateStart >= Test.startDate)).all()
        response_object = {
            "public_id" : Test.public_id,
            "user_id" : Test.user_id,
            "test_id" : Test.test_id,
            "startDate" : Test.startDate,
            "spendTime" : Test.spendTime, 
            "total" : Test.total,
            "linked_logs" : logs
        }
        return response_object, 200
    else: 
        response_object = {
            "status": "fail",
            "message": "Результат теста не найден.",
        }
        return response_object, 404



def ques_get() -> Tuple[Dict[str, str], int]:
    return TestQuestion.query.all()

def ques_post(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    testQuestion = TestQuestion(
        public_id = str(uuid.uuid4()),
        test_id = data.get("test_id"),
        questionNumber = data.get("questionNumber"),
        title = data.get("title"),
        questionTypeActual = data.get("questionTypeActual")
    )
    save_changes(testQuestion)
    return {
        "status": "success",
        "message" : "Успешно создан."
    }

def update_ques(data: Dict[str, str], public_id : str) -> Tuple[Dict[str, str], int]:
    testQuestion = TestQuestion.query.filter_by(public_id = public_id).first()
    if testQuestion:
        testQuestion.test_id=data.get("test_id") if data.get("test_id") else testQuestion.test_id
        testQuestion.questionNumber=data.get("questionNumber") if data.get("questionNumber") else testQuestion.questionNumber
        testQuestion.title=data.get("title") if data.get("title") else testQuestion.title
        testQuestion.questionTypeActual=data.get("questionTypeActual") if data.get("questionTypeActual") else testQuestion.questionTypeActual

        save_changes(testQuestion)
        response_object = {
            "status": "success",
            "message": "Успешно обновлен.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Вопрос не найден.",
        }
        return response_object, 404

def delete_ques(public_id):
    testQuestion = TestQuestion.query.filter_by(public_id=public_id).first()
    if testQuestion:
        TestQuestion.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Вопрос не найден.",
        }
        return response_object, 404
    


def ans_get() -> Tuple[Dict[str, str], int]:
    return TestAnswer.query.all()

def ans_post(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    testQuestion = TestAnswer(
        public_id = str(uuid.uuid4()),
        test_question_id = data.get("test_question_id"),
        answerNumber = data.get("answerNumber"),
        score = data.get("score"),
        answerText = data.get("answerText")
    )
    save_changes(testQuestion)
    return {
        "status": "success",
        "message" : "Успешно создан."
    }

def update_ans(data: Dict[str, str], public_id : str) -> Tuple[Dict[str, str], int]:
    testAnswer = TestAnswer.query.filter_by(public_id = public_id).first()
    if testAnswer:
        testAnswer.test_question_id=data.get("test_question_id") if data.get("test_question_id") else testAnswer.test_question_id
        testAnswer.answerNumber=data.get("answerNumber") if data.get("answerNumber") else testAnswer.answerNumber
        testAnswer.score=data.get("score") if data.get("score") is not None else testAnswer.score
        testAnswer.answerText=data.get("answerText") if data.get("answerText") else testAnswer.answerText

        save_changes(testAnswer)
        response_object = {
            "status": "success",
            "message": "Успешно обновлен.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Ответ не найден.",
        }
        return response_object, 404

def delete_ans(public_id):
    testAnswer = TestAnswer.query.filter_by(public_id=public_id).first()
    if testAnswer:
        TestAnswer.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Ответ не найден.",
        }
        return response_object, 404



def set_get() -> Tuple[Dict[str, str], int]:
    return TestSettings.query.all()

def set_post(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    testQuestion = TestSettings(
        public_id = str(uuid.uuid4()),
        test_id = data.get("test_id"),
        stressLevelActual = data.get("stressLevelActual"),
        minCount = data.get("minCount"),
        maxCount = data.get("maxCount"),
        description = data.get("description"),
        recommendation = data.get("recommendation")
    )
    save_changes(testQuestion)
    return {
        "status": "success",
        "message" : "Успешно создан."
    }

def update_set(data: Dict[str, str], public_id : str) -> Tuple[Dict[str, str], int]:
    testSettings = TestSettings.query.filter_by(public_id = public_id).first()
    if testSettings:
        testSettings.test_id=data.get("test_id") if data.get("test_id") else testSettings.test_id
        testSettings.stressLevelActual=data.get("stressLevelActual") if data.get("stressLevelActual") else testSettings.stressLevelActual
        testSettings.minCount=data.get("minCount") if data.get("minCount") is not None else testSettings.minCount
        testSettings.maxCount=data.get("maxCount") if data.get("maxCount") is not None else testSettings.maxCount
        testSettings.description=data.get("description") if data.get("description") else testSettings.description
        testSettings.recommendation=data.get("recommendation") if data.get("recommendation") else testSettings.recommendation

        save_changes(testSettings)
        response_object = {
            "status": "success",
            "message": "Успешно обновлен.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Настроек теста не найдено.",
        }
        return response_object, 404

def delete_set(public_id):
    testSettings = TestSettings.query.filter_by(public_id=public_id).first()
    if testSettings:
        TestSettings.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Настроек теста не найдено.",
        }
        return response_object, 404



def list_get() -> Tuple[Dict[str, str], int]:
    tests = TestsList.query.all()
    response_object = []
    for test in tests:
        test_object = vars(test)
        types2id = TestsType2Id.query.filter_by(test_id = test.public_id).all()
        test_object["clientTypeActual"] = []
        for type2id in types2id:
            test_object["clientTypeActual"].append(type2id.clientTypeActual)

        questionsInTest = TestQuestion.query.filter_by(test_id = test.public_id).all()
        test_object["maxScore"] = 0
        test_object["minScore"] = 0
        for question in questionsInTest:
            answersInQuestion = TestAnswer.query.filter_by(test_question_id = question.public_id).all()
            scores = []
            for answer in answersInQuestion:
                scores.append(answer.score)
            test_object["minScore"] += min(scores)
            test_object["maxScore"] += max(scores)
        response_object.append(test_object)
    return response_object

def list_post(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    testQuestion = TestsList(
        public_id = str(uuid.uuid4()),
        name = data.get("name"),
        clientTypeActual = data.get("clientTypeActual"),
        stageActual = data.get("stageActual"),
        interval = data.get("interval"),
        numberOfQuestions = data.get("numberOfQuestions")
    )
    save_changes(testQuestion)
    return {
        "status": "success",
        "message" : "Успешно создан."
    }

def update_list(data: Dict[str, str], public_id : str) -> Tuple[Dict[str, str], int]:
    testsList = TestsList.query.filter_by(public_id = public_id).first()
    if testsList:
        testsList.name=data.get("name") if data.get("name") else testsList.name
        testsList.clientTypeActual=data.get("clientTypeActual") if data.get("clientTypeActual") else testsList.clientTypeActual
        testsList.stageActual=data.get("stageActual") if data.get("stageActual") else testsList.stageActual
        testsList.interval=data.get("interval") if data.get("interval") else testsList.interval
        testsList.numberOfQuestions=data.get("numberOfQuestions") if data.get("numberOfQuestions") else testsList.numberOfQuestions

        save_changes(testsList)
        response_object = {
            "status": "success",
            "message": "Успешно обновлен.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Тест не найден",
        }
        return response_object, 404

def delete_list(public_id):
    testsList = TestsList.query.filter_by(public_id=public_id).first()
    if testsList:
        TestsList.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Тест не найден",
        }
        return response_object, 404
    

def logs_get() -> Tuple[Dict[str, str], int]:
    return TestLog.query.all()

def delete_logs(public_id):
    testsLog = TestLog.query.filter_by(public_id=public_id).first()
    if testsLog:
        TestLog.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Лог теста не найден.",
        }
        return response_object, 404
    


def ret_get() -> Tuple[Dict[str, str], int]:
    testResults = TestResult.query.all()
    response_object = []
    for testResult in testResults:
        user = User.query.filter_by(public_id = testResult.user_id).first()
        midNameUser = f" {user.middleName}" if user.middleName else ""
        test = TestsList.query.filter_by(public_id = testResult.test_id).first()
        response_object.append({
            "public_id" : testResult.public_id,
            "user_id" : testResult.user_id,
            "test_id" : testResult.test_id,
            "startDate" : testResult.startDate,
            "spendTime" : testResult.spendTime,
            "total" : testResult.total,
            "clientFullName" : f"{user.firstName} {user.lastName}{midNameUser}",
            "email" : user.email,
            "name" : test.name
        })
    return response_object


def delete_ret(public_id):
    testsRet = TestResult.query.filter_by(public_id=public_id).first()
    if testsRet:
        TestResult.query.filter_by(public_id=public_id).delete()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Успешно удален.",
        }
        return response_object, 200
    else:
        response_object = {
            "status": "fail",
            "message": "Результат теста не найден.",
        }
        return response_object, 404
    
def easter_egg_notification() -> None:
    NotificationLog.query.all()
