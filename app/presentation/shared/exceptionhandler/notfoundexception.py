from http.client import NOT_FOUND
from typing import ClassVar
from flask import jsonify

class NotFoundException(Exception):
    __FLASK_DEFAULT_MSG: ClassVar[str] = "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    __CUSTOM_DEFAULT_MSG: ClassVar[str] = "指定したリソースが見つかりません。"
    
    @classmethod
    def response(cls, e):
        if str(e.description) == cls.__FLASK_DEFAULT_MSG:
            e.description = cls.__CUSTOM_DEFAULT_MSG
            
        return jsonify({
            'code' : NOT_FOUND,
            'message': e.description
        }), NOT_FOUND