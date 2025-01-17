from flask import request
from flask_restx import Resource

from src.service.auth_helper import Auth
from src.util.dto import AuthDto
from typing import Dict, Tuple

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route("/login")
class UserLogin(Resource):
    """
    User Login Resource
    """

    @api.doc("user login")
    @api.expect(user_auth, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route("/logout")
class LogoutAPI(Resource):
    """
    Logout Resource
    """

    @api.doc("logout a user")
    def post(self) -> Tuple[Dict[str, str], int]:
        auth_header = request.headers.get("Authorization")
        return Auth.logout_user(data=auth_header)
