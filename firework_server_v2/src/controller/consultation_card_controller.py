from flask import request, send_file
from flask_restx import Resource

from src.util.decorator import admin_token_required
from src.util.dto import ConsultationCardDto
from src.service.consultation_card_service import save_card, get_all_cards, get_a_card, delete_a_card, save_new_card_blueprint, validate_card, get_card_as_word
from typing import Dict, Tuple

api = ConsultationCardDto.api
_card_create_new = ConsultationCardDto.consultation_card_create_new
_card_save_blueprint = ConsultationCardDto.consultation_card_save_blueprint
_card_return = ConsultationCardDto.consultation_card_return
_card_validate = ConsultationCardDto.consultation_card_validate


@api.route("/")
class ConsultationCardList(Resource):
    @api.doc("list_of_registered_consultation_cards")
    @admin_token_required
    @api.marshal_list_with(_card_return, envelope="data")
    def get(self):
        """List all registered consultation cards"""
        return get_all_cards()
    

@api.route("/create")
class NewCard(Resource):
    @api.response(400, "Ошибка валидации")
    @api.response(201, "Успешно создан.")
    @api.expect(_card_create_new, validate=True)
    @admin_token_required
    @api.doc("create a new card ")
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Card"""
        data = request.json
        cookie = request.headers.get('Authorization')
        res = save_new_card_blueprint(data=data, cookie = cookie)
        return res
    

@api.route("/save/blueprint/<public_id>", methods = ['PUT'])
@api.param("public_id", "The Card identifier")
class CardSaveBlueprint(Resource):
    @api.expect(_card_save_blueprint, validate=True)
    @api.response(200, "Успешно сохранено.")
    @api.response(404, "Карточки консультации не существует.")
    @admin_token_required
    @api.doc("Save refactoring to a card by given ID")
    def put(self, public_id) -> Tuple[Dict[str, str], int]:
        """Save a cards parameters"""
        data = request.json
        res = save_card(data=data, public_id = public_id)
        return res
    

@api.route("/save/card/<public_id>", methods = ['PUT'])
@api.param("public_id", "The Card identifier")
class CardValidateBlueprint(Resource):
    @api.response(200, "Успешно провалидировано.")
    @api.response(404, "Карточки консультации не существует.")
    @api.expect(_card_validate, validate=True)
    @admin_token_required
    @api.doc("Save refactoring to a card by given ID")
    def put(self, public_id) -> Tuple[Dict[str, str], int]:
        """Validates a card"""
        data = request.json
        res = validate_card(data=data, public_id = public_id)
        return res
        

@api.route("/<public_id>", methods = ['GET', 'DELETE'])
@api.param("public_id", "The card identifier")
class Card(Resource):
    @api.doc("get a card")
    @api.response(404, "Карточки консультации не существует.")
    @api.marshal_with(_card_return)
    @admin_token_required
    def get(self, public_id):
        """get a card given its identifier"""
        card = get_a_card(public_id)
        if not card:
            response_object = {
                "status": "fail",
                "message": "Карточки консультации не существует.",
            }
            return response_object, 404
        else:
            return card
        
    @api.doc("delete a card")
    @api.response(404, "Карточки консультации не существует.")
    @api.response(200, "Успешно удален.")
    @admin_token_required
    def delete(self, public_id):
        """delete a card given its identifier"""
        return delete_a_card(public_id)
        
@api.route("/upload/<public_id>", methods = ['GET'])
@api.param("public_id", "The card identifier")
class CardUpload(Resource):
    @api.doc("upload consultation card as Word document")
    @api.response(404, "Карточки консультации не существует.")
    @admin_token_required
    def get(self, public_id):
        """get a card as a word file given its identifier"""
        card = get_card_as_word(public_id)
        if not card:
            response_object = {
                "status": "fail",
                "message": "Карточки консультации не существует.",
            }
            return response_object, 404
        else:
            return send_file(card, as_attachment=True, download_name='example.docx')
