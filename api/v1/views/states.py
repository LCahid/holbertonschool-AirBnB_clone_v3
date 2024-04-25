#!/usr/bin/python3
'''Doc for status'''
from flask import jsonify, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'])
def get_states():
    '''Doc for status'''
    states = storage.all("State")
    return jsonify([state.to_dict() for state in states.values()])


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    '''Doc for status'''
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    '''Doc for status'''
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'])
@app_views.route('/states/', methods=['POST'])
def create_state():
    '''Doc for status'''
    state = request.get_json()
    if state is None:
        return jsonify({"error": "Not a JSON"}), 400
    if "name" not in state:
        return jsonify({"error": "Missing name"}), 400
    new_state = State(**state)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    '''Doc for status'''
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    update = request.get_json()
    if update is None:
        return jsonify({"error": "Not a JSON"}), 400 
    for key, value in update.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
