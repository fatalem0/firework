from flask_mail import Mail, Message
from src.config import Config
mail = Mail()

def send_message(email : str, finished : bool, test_name : str) -> str:
    msg = Message( 
                'Напоминания в тестах',
                recipients = [email],
                sender = Config.MAIL_USERNAME 
            )
    if finished:
        msg.body = fr"""Уважаемый клиент, 

Вам необходимо пройти тест {test_name}!
Прохождение тестов позволяет нам вместе двигаться вперед более осознанно, улучшая состояния!"""
    else:
        msg.body = fr"""Уважаемый клиент, 

Вы не закончили прохождение теста {test_name}! Вы можете продолжить его на том же сайте. Прогресс сохраняется.
Прохождение тестов позволяет нам вместе двигаться вперед более осознанно, улучшая состояние!
"""
    try:
        mail.send(msg)
        return 'Sent'
    except Exception as e:
        return e