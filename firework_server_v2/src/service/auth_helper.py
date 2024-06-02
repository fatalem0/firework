from src.model.user import User
from src.service.blacklist_service import save_token
from typing import Dict, Tuple


class Auth:
    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            user = User.query.filter_by(email=data.get("email")).first()
            if user and user.check_password(data.get("password")):
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        "status": "success",
                        "message": "Удачный вход в систему.",
                        "Authorization": auth_token,
                    }
                    return response_object, 200
            else:
                response_object = {
                    "status": "fail",
                    "message": "Почта или пароль не совпадают.",
                }
                return response_object, 401

        except Exception as e:
            response_object = {"status": "fail", "message": "Попробуйте снова."}
            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ""
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                return save_token(token=auth_token)
            else:
                response_object = {"status": "fail", "message": resp}
                return response_object, 401
        else:
            response_object = {
                "status": "fail",
                "message": "Отсутствует фактор аутентификации.",
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get("Authorization")
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                query = User.query.filter_by(id=resp)
                if query.count() != 0:
                    user = query.first()
                    response_object = {
                        "status": "success",
                        "data": {
                            "public_id": user.public_id,
                            "email": user.email,
                            "admin": user.admin,
                            "created": str(user.created),
                        },
                    }
                    return response_object, 200
                else:
                    response_object = {
                        "status": "fail",
                        "message": "Отсутствует фактор аутентификации.",
                    }
                    return response_object, 401
            response_object = {"status": "fail", "message": resp}
            return response_object, 401
        else:
            response_object = {
                "status": "fail",
                "message": "Отсутствует фактор аутентификации.",
            }
            return response_object, 401
