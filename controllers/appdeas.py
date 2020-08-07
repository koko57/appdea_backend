from flask import Blueprint, request, abort, jsonify
from models import db, Appdea

appdeas = Blueprint('appdeas', __name__)


@appdeas.route('/appdeas')
def get_appdeas():
    results = Appdea.query.all()

    formatted = [result.format_short() for result in results]

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

    return jsonify(success=True, appdea=new_appdea.format_short())


@appdeas.route('/appdeas/<int:id>')
def get_appdea(id):
    result = Appdea.query.filter_by(id=id).first()

    return jsonify(
        success=True,
        appdea=result.format_long(),
    )

@appdeas.route('/appdeas/<int:id>', methods=['DELETE'])
def delete_coffee(id):
    appdea_to_delete = Appdea.query.filter_by(id=id).first()
    deleted_id = appdea_to_delete.id

    try:
        Appdea.delete(appdea_to_delete)
    except:
        abort(500)

    return jsonify(success=True, appdea=deleted_id)
