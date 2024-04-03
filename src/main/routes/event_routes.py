from flask import Blueprint, jsonify

eventRouteBp = Blueprint("event_route", __name__)

@eventRouteBp.route("/events", methods=["POST"])
def createEvent():
  return jsonify({
    "msg": "received!"
  })