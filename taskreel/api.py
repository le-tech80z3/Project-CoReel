from flask import jsonify, Blueprint, request
from taskreel.models import User, db
from taskreel.viz_crud import create_reelemx, get_reelemx, update_reelemx
from flask_login import current_user, login_required

api = Blueprint('api', __name__)

@api.route('/')
def home():
  first_user = User.query.first()
  print(f'🥶 {first_user}')
  return render_template('index.html')

@api.route('/reelemxs', 
methods=['GET', 'POST'])
@login_required
def reelemx_index_create():
    if request.method == 'GET':
      self.title = title
      self.body = body
    if request.method == 'POST':
      # first_user = User.query.first()
      # print(f'🥶 {first_user}')
      # print(User)
      # print('😢')
      #request.form['user_id'] = current_user.id
      print(request.form)
      title = request.form['title']
      body = request.form['body']
      user_id = request.form['user_id']
      return create_reelemx(title, body, user_id)
      
    
        # return get_all_reelemx()
        # if request.method == 'POST':
        #     


#def @api.route()
@api.route('/reelemxs/<int:id>', methods = ['GET', 'PUT'])
def reelemx_show_put_delete(id):
  if request.method == 'GET':
    
      return get_reelemx(id)
  if request.method == 'PUT':
      return update_reelemx(
          id,
          title=request.form['title'],
          body=request.form['body'])
              