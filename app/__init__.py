from flask import  Flask, render_template

from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config')

db= SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_register.controllers import mod_register as register_module
app.register_blueprint(register_module)

from app.mod_auth.controllers import mod_auth as auth_module
app.register_blueprint(auth_module)


from app.mod_post_data.controllers import mod_post_data as post_module

app.register_blueprint(post_module)




db.create_all()