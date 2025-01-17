from src import db

from src.model.blacklist import BlacklistToken
from typing import Dict, Tuple


def save_token(token: str) -> Tuple[Dict[str, str], int]:
    blacklist_token = BlacklistToken(token=token)
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {"status": "success", "message": "Выход из системы произведен успешно."}
        return response_object, 200
    except Exception as e:
        response_object = {"status": "fail", "message": e}
        return response_object, 200
