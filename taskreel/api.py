from flask import jsonify, Blueprint
from .models import User, db

api = Blueprint('api', __name__)

@api.route('/')

def home():
  first_user = User.query.first()
  print(f':) {first_user}')
  return jsonify(message="welcome home!")

@api.route('/reelemxs', 
methods=['GET', 'POST'])
def reelemx_index_create():
    if request.method == 'GET':
        self.title = title
        self.body = body
        
        # return get_all_reelemx()
        # if request.method == 'POST':
        #     return create_reelemx(**request.form)


def reelemxs():
  pass

@api.route('/reelemxs')
def reelemx_show_put_delete(id):
  if request.method == 'GET':
      return get_reelemx(id)
      if request.method == 'PUT':
          return update_reelemx(
              id,
              title=request.form['title'],
              body=request.form['body'])
              