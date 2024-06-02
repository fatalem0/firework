from flask_apscheduler import APScheduler
from src.models.notifications.aggrements import Aggrements
from src.models.notifications.notificationJournal import NotificationJournal
from src.models.notifications.notificationLogs import NotificationLog
from src.models.user import User 
from src.models.tests.test_log import TestLog
from src.models.tests.tests_list import TestsList
from src.mail import send_message
import time
import datetime
import uuid

from src.db import db
 

scheduler = APScheduler()

@scheduler.task("cron", id="do_job_1", minute='0', hour='8,20')
def job1():
    with scheduler.app.app_context():

        userEntities = User.query.all()
        for userEntity in userEntities:

            aggrement = Aggrements.query.filter_by(user_id=userEntity.public_id).first()
            if aggrement and aggrement.hasMailAggrement:
                usersNotifications = NotificationJournal.query.filter_by(user_id = userEntity.public_id).all()
                for usersNotification in usersNotifications:
                    lastLog = TestLog.query.filter_by(test_id = usersNotification.test_id, user_id = usersNotification.user_id).order_by(TestLog.dateStart.desc()).first()
                    test = TestsList.query.filter_by(public_id = usersNotification.test_id).first()
                    if usersNotification.sendNextTime < datetime.datetime.utcnow() and datetime.datetime.utcnow() - lastLog.dateStart < datetime.timedelta(days=70):
                        responce = send_message(email = userEntity.email, finished = usersNotification.testIsFinished, test_name = test.name)

                        usersNotification.sendNextTime += datetime.timedelta(days=7)
                        save_changes(usersNotification)

                        log = NotificationLog(
                            public_id=str(uuid.uuid4()),
                            email = userEntity.email,
                            chanel = 'mail',
                            status = 'send' if responce == 'Sent' else 'not_send',
                            sendTime = datetime.datetime.utcnow(),
                            errorDescription = None if responce == 'Sent' else responce
                        )
                        save_changes(log)
                        time.sleep(40)


def save_changes(data) -> None:
    db.session.add(data)
    db.session.commit()