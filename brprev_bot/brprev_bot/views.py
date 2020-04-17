from flask import Blueprint, jsonify, request


api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')


def init_app(app):
    app.register_blueprint(api_v1)


@api_v1.route('/')
def index():
    return 'It Works!'


@api_v1.route('/search_result/broadcast', methods=['POST'])
def search_result_broadcast():
    from brprev_bot.tasks import broadcast_search_result
    broadcast_search_result.delay(request.json)
    return jsonify('{"message": "search result sended to chats"}'), 200
