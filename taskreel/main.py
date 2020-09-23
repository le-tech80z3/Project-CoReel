from flask_login import login_required, current_user
from flask import Blueprint, render_template
from taskreel.viz_crud import get_all_reelemxs
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
   

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name )

@main.route('/allreelemxs')
@login_required
def allreelemxs():
    reelemxs = get_all_reelemxs(current_user.id)
    # reelemxs = db.Reelemx.query.all()
    return render_template('allreelemxs.html', name=current_user.name, reelemxs = reelemxs, id=current_user.id)

