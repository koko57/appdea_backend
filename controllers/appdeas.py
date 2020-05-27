from flask import Blueprint, request, abort, jsonify
from models import db, Appdea

appdeas = Blueprint('appdeas', __name__)


@appdeas.route('/appdeas')
def get_appdeas():
    results = Appdea.query.all()

    formatted = [result.format() for result in results]

    return jsonify(
        success=True,
        appdeas=formatted,
        results_count=len(formatted)
    )


@appdeas.route('/appdeas', methods=['POST'])
def create_appdea():
    body = request.get_json()
    name = body['name']
    description = body.get('description', None)

    new_appdea = Appdea(name=name, description=description)

    try:
        Appdea.insert(new_appdea)
    except:
        abort(500)

    return jsonify(success=True, appdea=new_appdea.format())
