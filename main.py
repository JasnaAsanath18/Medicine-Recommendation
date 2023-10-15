from flask import *
from public import public
from admin import admin
from distributor import distributor
from manufacturer import manufacturer
from user import user

from pharmacy import pharmacy

# from user import user

app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(distributor)
app.register_blueprint(manufacturer)
app.register_blueprint(pharmacy)
app.register_blueprint(user,url_prefix='/user')



app.secret_key='key'
app.run(debug=True,port=5017,host="0.0.0.0")