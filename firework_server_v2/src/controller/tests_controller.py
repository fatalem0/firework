from flask import request
from flask_restx import Resource

from src.util.decorator import admin_token_required
from src.util.dto import TestDTOs
from typing import Dict, Tuple
from src.service.test_service import find_test, answer, get_a_result

from src.service.test_service import *

api = TestDTOs.api
_test_open = TestDTOs.test_creds
_test_open_ret = TestDTOs.test_creds_return
_test_ans = TestDTOs.test_ans
_test_list_return = TestDTOs.test_list_return
_test_set_return = TestDTOs.test_set_return
_test_ans_return = TestDTOs.test_ans_return
_test_ques_return = TestDTOs.test_ques_return
_test_logs_return = TestDTOs.test_logs_return
_test_ret_return = TestDTOs.test_ret_return
_test_result_ret = TestDTOs.test_result_ret
_test_result_ret_with_logs = TestDTOs.test_ret_return_with_logs


@api.route("/open")
class OpenTest(Resource):
    """
    Start or open test Resource
    """
    @admin_token_required
    @api.doc("open test")
    @api.expect(_test_open, validate=True)
    @api.marshal_list_with(_test_open_ret, envelope="data")
    def post(self) -> Tuple[Dict[str, str], int]:
        # get the post data
        post_data = request.json
        res = find_test(data=post_data)
        if res[1] == 400:
            return api.abort(400, "Пользователь не найден.")
        elif res[1] == 401:
            return api.abort(400, "Тест не найден.")
        else:
            return res

@api.route("/answer")
class AnswerQuestion(Resource):
    """
    Answer on tests question Resource
    """
    @admin_token_required
    @api.doc("answer on tests question")
    @api.expect(_test_ans, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        post_data = request.json
        return answer(data=post_data)


@api.route("/end/<public_id>")
@api.param("public_id", "The Test identifier")
@api.response(404, "Тест не найден.")
class TestsResults(Resource):
    @api.doc("get a tests result")
    @admin_token_required
    @api.marshal_with(_test_result_ret, envelope="data")
    def post(self, public_id):
        """get a tests results given its identifier"""
        result = get_a_result(public_id)
        if result[1] == 400:
            return api.abort(404, "Результат теста не найден.")
        elif result[1] == 401:
            return api.abort(404, "Лог теста не найден.")
        elif result[1] == 402:
            return api.abort(404, "Настроек теста не найдено.")
        else:
            return result
        

@api.route("/result/<public_id>")
@api.param("public_id", "The Test identifier")
@api.response(404, "Тест не найден.")
class TestsResultsWithLogs(Resource):
    @api.doc("get a tests result with linked logs")
    @admin_token_required
    @api.marshal_list_with(_test_result_ret_with_logs, envelope="data")
    def get(self, public_id):
        """get a tests results with linked logs given its identifier"""
        result = get_a_result_with_logs(public_id)
        if result[1] == 404:
            return api.abort(404, "Результат теста не найден.")
        else:
            return result







@api.route("/question", methods = ['GET', 'POST', 'DELETE', 'PUT'])
class TestsQue(Resource):
    @api.marshal_list_with(_test_ques_return, envelope="data")
    @admin_token_required
    def get(self):
        return ques_get()

    @admin_token_required    
    def post(self):
        post_data = request.json
        return ques_post(data=post_data)
    
    @admin_token_required
    def put(self):
        data = request.json
        public_id = data["public_id"]
        return update_ques(data = data, public_id = public_id)
    
    @admin_token_required
    def delete(self):
        public_id = request.json["public_id"]
        return delete_ques(public_id)

    
@api.route("/answeradd", methods = ['GET', 'POST', 'DELETE', 'PUT'])
class TestsAns(Resource):
    @api.marshal_list_with(_test_ans_return, envelope="data")
    @admin_token_required
    def get(self):
        return ans_get()

    @admin_token_required    
    def post(self):
        post_data = request.json
        return ans_post(data=post_data)
    
    @admin_token_required
    def put(self):
        data = request.json
        public_id = data["public_id"]
        return update_ans(data = data, public_id = public_id)
    
    @admin_token_required
    def delete(self):
        public_id = request.json["public_id"]
        return delete_ans(public_id)
    
@api.route("/settings", methods = ['GET', 'POST', 'DELETE', 'PUT'])
class TestsSet(Resource):
    @api.marshal_list_with(_test_set_return, envelope="data")
    @admin_token_required
    def get(self):
        return set_get()

    @admin_token_required 
    def post(self):
        post_data = request.json
        return set_post(data=post_data)
    
    @admin_token_required
    def put(self):
        data = request.json
        public_id = data["public_id"]
        return update_set(data = data, public_id = public_id)
    
    @admin_token_required
    def delete(self):
        public_id = request.json["public_id"]
        return delete_set(public_id)
    
@api.route("/list", methods = ['GET', 'POST', 'DELETE', 'PUT'])
class TestsList(Resource):
    @api.marshal_list_with(_test_list_return, envelope="data")
    @admin_token_required
    def get(self):
        return list_get(), 200

    @admin_token_required    
    def post(self):
        post_data = request.json
        return list_post(data=post_data)
    
    @admin_token_required
    def put(self):
        data = request.json
        public_id = data["public_id"]
        return update_list(data = data,public_id = public_id)
    
    @admin_token_required
    def delete(self):
        public_id = request.json["public_id"]
        return delete_list(public_id)
    

@api.route("/logs", methods = ['GET', 'DELETE'])
class TestsLogs(Resource):
    @api.marshal_list_with(_test_logs_return, envelope="data")
    @admin_token_required
    def get(self):
        return logs_get()
    
    @admin_token_required
    def delete(self):
        public_id = request.json["public_id"]
        return delete_logs(public_id)
    


@api.route("/result", methods = ['GET', 'DELETE'])
class TestsLogs(Resource):
    @api.marshal_list_with(_test_ret_return, envelope="data")
    @admin_token_required
    def get(self):
        return ret_get()
    
    @admin_token_required
    def delete(self):
        public_id = request.json["public_id"]
        return delete_ret(public_id)