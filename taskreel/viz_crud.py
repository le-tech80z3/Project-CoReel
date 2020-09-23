from flask import jsonify, redirect, url_for, render_template
from taskreel.models import db, Reelemx

# create a reelemx
def create_reelemx(title, body, user_id):
    new_reelemx = Reelemx(title = title, body = body, user_id = user_id)
    db.session.add(new_reelemx)
    db.session.commit()
    return redirect(url_for('main.allreelemxs'))

def get_all_reelemxs(user_id):
    reelemxs = Reelemx.query.filter_by(user_id = user_id).all()
    reelemxs = [reelemx.as_dict() for reelemx in reelemxs]
    return reelemxs

def get_reelemx(id):
    reelemx = Reelemx.query.get(id)
    return render_template('showreelemx.html', reelemx = reelemx)
# update a reelemx

def update_reelemx(id, title, body):
    reelemx = Reelemx.query.get(id)
    if reelemx:
        reelemx.title = title or reelemx.title
        reelemx.body = body or reelemx.body
        db.session.commit()
    return redirect(url_for('main.allreelemxs'))