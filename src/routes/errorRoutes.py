from flask import jsonify, abort
from . import router

@router.errorhandler(403)
    def error403(e):
        message = {
            "status-code": 403,
            "message": "you belom login kayanya, atau belom apapun"
        }
        return jsonify(message)

@router.errorhandler(404)
def error404(e):
    message = {
        "status-code":404,
        "message": "resource ga ketemu"
    }
    return jsonify(message)

@router.errorhandler(500)
def error500(e):
    message = {
        "status-code":404,
        "message": "resource ga ketemu"
    }
    return jsonify(message)
