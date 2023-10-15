from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template("admin_home.html")

@admin.route('/verify_manufacturer')
def verify_manufacturer():
    data={}
    qry="select * from manufacture"
    data['res']=select(qry)
    if 'action' in request.args:
        action=request.args['action']
        
        lid=request.args['lid']
    else:
        action=None

    if action=='accept':
        qry="update login set usertype='%s' where login_id='%s'"%('manufacturer',lid)
        update(qry)
        return redirect(url_for('admin.verify_manufacturer'))

    if action=='reject':
        qry="delete from manufacture where login_id='%s'"%(lid)
        qry1="delete from login where login_id='%s'"%(lid)
        delete(qry)
        delete(qry1)
        return redirect(url_for('admin.verify_manufacturer'))
    return render_template("admin_verify_manufacturer.html",data=data)

@admin.route('/verify_distributor')
def verify_distributor():
    data={}
    qry="select * from distributor"
    data['res']=select(qry)
    if 'action' in request.args:
        action=request.args['action']
        
        lid=request.args['lid']
    else:
        action=None

    if action=='accept':
        qry="update login set usertype='%s' where login_id='%s'"%('distributor',lid)
        update(qry)
        return redirect(url_for('admin.verify_distributor'))

    if action=='reject':
        qry="delete from distributor where login_id='%s'"%(lid)
        qry1="delete from login where login_id='%s'"%(lid)
        delete(qry)
        delete(qry1)
        return redirect(url_for('admin.verify_distributor'))
    return render_template("admin_verify_distributor.html",data=data)

@admin.route('/verify_pharmacy')
def verify_pharmacy():
    data={}
    qry="select * from pharmacy"
    data['res']=select(qry)
    if 'action' in request.args:
        action=request.args['action']
        
        lid=request.args['lid']
    else:
        action=None

    if action=='accept':
        qry="update login set usertype='%s' where login_id='%s'"%('pharmacy',lid)
        update(qry)
        return redirect(url_for('admin.verify_pharmacy'))

    if action=='reject':
        qry="delete from pharmacy where login_id='%s'"%(lid)
        qry1="delete from login where login_id='%s'"%(lid)
        delete(qry)
        delete(qry1)
        return redirect(url_for('admin.verify_pharmacy'))

    return render_template("admin_verify_pharmacy.html",data=data)

@admin.route('/admin_feedback')
def admin_feedback():
    data={}
    s="select * from feedback"
    data['res']=select(s)
    return render_template("admin_feedback.html",data=data)