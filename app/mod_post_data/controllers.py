from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from werkzeug import check_password_hash, generate_password_hash

from app import db
from flask import json 
from flask.ext.restful import fields, marshal
from app.mod_auth.models import CLIENT
from app.mod_auth.models import DAATE
from app.mod_auth.models import CONCERNE
from flask.ext.restful import marshal_with

#from app.mod_post_data import data

mod_post_data = Blueprint('post', __name__, url_prefix='/post')

accel={
    'x' :fields.Integer,
    'y' :fields.Integer,
    'z' :fields.Integer,
    'timestamp' : fields.Integer,
}
    #location={
    #'latitude': fields.Integer,
    #'longitude': fields.Integer,
#'timestamp': fields.Integer,
#}

#data = {
#        'location': location,
#        'accel': accel,
#}

@mod_post_data.route('/data', methods=['POST'])
def insertdata():
    #mfields={'latitude': fields.Raw}
    i=1
    for h in request.json['data']['location']:
        #print h
        lati =h['latitude']
        lon=h['longitude']
        t= CONCERNE(email='hbalafrej@enseirb.fr', date=str('2014-02-'+i)  , long=lon, lat= lati, mod='3', alt='1')
        i=i+1
        db.session.add(t)
        db.session.commit()
    # print marshal(h, mfields)
    return 'laloli'

