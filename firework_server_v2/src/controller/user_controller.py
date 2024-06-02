from flask import request
from flask_restx import Resource

from src.util.decorator import admin_token_required
from src.util.dto import UserDto
from src.service.user_service import save_new_user, get_all_users, get_a_user, update_user, delete_a_user
from typing import Dict, Tuple

api = UserDto.api
_user_create_with_client = UserDto.user_create_with_client
_user_return = UserDto.user_return
_user_update = UserDto.user_update


@api.route("/")
class UserList(Resource):
    @api.doc("list_of_registered_users")
    @admin_token_required
    @api.marshal_list_with(_user_return, envelope="data")
    def get(self):
        """List all registered users"""
        return get_all_users()
    
    @api.expect(_user_create_with_client, validate=True)
    @api.response(201, "Пользователь успешно создан.")
    @api.doc("create a new user")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new User"""
        data = request.json
        res = save_new_user(data=data)
        return res
    

@api.route("/<public_id>", methods = ['GET', 'PUT', 'DELETE'])
@api.param("public_id", "The User identifier")
@api.response(404, "Пользователь не найден.")
class User(Resource):
    @api.doc("get a user")
    @api.marshal_with(_user_return)
    @admin_token_required
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
        
    @api.doc("delete a user")
    @admin_token_required
    def delete(self, public_id):
        """delete a user given its identifier"""
        return delete_a_user(public_id)


    @api.doc("update a user")
    @api.expect(_user_update, validate=True)
    @admin_token_required
    def put(self, public_id) ->Tuple[Dict[str, str], int]:
        """update a user by its identifier"""
        user = get_a_user(public_id)
        data = request.json
        print(data)
        res = update_user(data=data, user=user)
        return res
        