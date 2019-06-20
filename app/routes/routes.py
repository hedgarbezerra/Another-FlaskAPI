from app import app
from ..views import users, index, helper


"""Neste arquivo iremos criar todas rotas para aplicação para manter o código limpo usando
 as views(controllers)  e as relacionando por meio de funções"""

@app.route('/v1', methods=['GET'])
@helper.token_required
def index():
    return index.index()


@app.route('/', methods=['GET'])
def redirect():
    return index.index_redirect()


@app.route('/v1/users', methods=['GET'])
def get_users():
    return users.get_users()


@app.route('/v1/users/<id>', methods=['GET'])
def get_user(id):
    return users.get_user(id)


@app.route('/v1/users', methods=['POST'])
def post_users():
    return users.post_user()


@app.route('/v1/users/<id>', methods=['DELETE'])
def delete_users(id):
    return users.delete_user(id)


@app.route('/v1/users/<id>', methods=['PUT'])
def update_users(id):
    return users.update_user(id)

@app.route('/v1/auth', methods=['POST'])
def auth():
    pass
