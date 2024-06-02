from flask import request
from flask_restx import Resource

from src.util.decorator import admin_token_required
from src.util.dto import ClientDto
from src.service.client_service import save_new_client, get_all_clients, get_a_client, update_client, delete_a_client
from typing import Dict, Tuple

api = ClientDto.api
_client_create = ClientDto.client_create
_client_return = ClientDto.client_return
_client_return_all = ClientDto.client_return_all
_client_update = ClientDto.client_update

@api.route("/")
class ClientList(Resource):
    @api.doc("list_of_registered_clients")
    @admin_token_required
    @api.marshal_list_with(_client_return_all, envelope="data")
    def get(self):
        """List all registered clients"""
        return get_all_clients()

    @api.expect(_client_create, validate=True)
    @api.response(201, "Успешно зарегестрирован.")
    @admin_token_required
    @api.doc("create a new client")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Client"""
        data = request.json
        print(data)
        res = save_new_client(data=data)
        print(res)
        return res


@api.route("/<public_id>", methods = ['GET', 'DELETE', 'PUT'])
@api.param("public_id", "The Client identifier")
@api.response(404, "Клиент не существует.")
class Client(Resource):
    @api.doc("get a client")
    @api.marshal_with(_client_return)
    @admin_token_required
    def get(self, public_id):
        """get a client given its identifier"""
        client = get_a_client(public_id)
        if not client:
            api.abort(404)
        else:
            return client

    @api.doc("delete a client")
    @admin_token_required
    def delete(self, public_id):
        """delete a client given its identifier"""
        return delete_a_client(public_id)
    
    @api.doc("update a client")
    @api.expect(_client_update, validate=True)
    @admin_token_required
    def put(self, public_id) ->Tuple[Dict[str, str], int]:
        """update a client by its identifier"""
        data = request.json
        res = update_client(data=data, public_id=public_id)
        return res
        