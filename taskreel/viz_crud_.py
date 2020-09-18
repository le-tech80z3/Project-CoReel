# create a reelemx
def create_reelemx(**form_kwargs):
    new_reelemx = Reelemx(**form_kwargs)
    db.session.add(new_reelemx)
    db.session.commit()
    return jsonify(new_reelemx.as_dict())

# update a reelemx

def update_reelemx(id, title, body, ):
    reelemx = Reelemx.query.get(id)
    if reelemx:
        reelemx.title = title or reelemx.title
        reelemx.body = body or reelemx.body
        db.session