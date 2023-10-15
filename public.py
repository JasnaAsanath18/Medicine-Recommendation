from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)

# @public.route('/')
# def home():
#     return render_template('public_home.html')

@public.route('/',methods=['get','post'])
def login():
    if 'login' in request.form:
        a=request.form['uname']
        b=request.form['pwd']
        print(a,b)
        q="select * from login where username='%s' and password='%s'"%(a,b)
        print(q)
        res=select(q)
        if res:
            session['lid']=res[0]['login_id']
            u_type=res[0]['usertype']

            if u_type=="admin":
                return redirect(url_for('admin.adminhome'))
            elif u_type=="manufacturer":
                q="select * from manufacture where login_id='%s'"%(session['lid'])
                print(q)
                re=select(q)
                session['manufacture_id']=re[0]['manufacture_id']
                print(session['manufacture_id'])
                return redirect(url_for('manufacturer.manufacturerhome'))
            elif u_type=="distributor":
                q="select * from distributor where login_id='%s'"%(session['lid'])
                print(q)
                
                re=select(q)
                session['dist_id']=re[0]['distributor_id']
                return redirect(url_for('distributor.distributorhome'))
            elif u_type=="pharmacy":
                q="select * from pharmacy where login_id='%s'"%(session['lid'])
                print(q)
                
                re=select(q)
                session['phar_id']=re[0]['pharmacy_id']
                return redirect(url_for('pharmacy.pharmacyhome'))


    return render_template('login.html')


@public.route('/manufacturer_register',methods=['get','post'])
def manufacturer_register():
    if 'submit' in request.form:
        name=request.form['name']
        phone=request.form['phone']
        email=request.form['email']
        pwd=request.form['pwd']
        place=request.form['place']
        disc=request.form['disc']
        img=request.files['image']
        path='static/'+str(uuid.uuid4())+img.filename
        img.save(path)
        q="insert into login values (null,'%s','%s','%s')"%(email,pwd,'pending')
        lin=insert(q)
        qry="insert into manufacture values(null,'%s','%s','%s','%s','%s','%s','%s')"%(lin,name,phone,email,place,disc,path)
        insert(qry)
        flash("Successfully Registered!!")
        return redirect(url_for('public.manufacturer_register'))
    return render_template("manufacturer_registration.html")



@public.route('/distributor_register',methods=['get','post'])
def distributor_register():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        pwd=request.form['pwd']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        q="insert into login values (null,'%s','%s','%s')"%(email,pwd,'pending')
        lin=insert(q)
        qry="insert into distributor values(null,'%s','%s','%s','%s','%s','%s')"%(lin,fname,lname,place,phone,email)
        insert(qry)
        flash("Successfully Registered!!")
        return redirect(url_for('public.distributor_register'))
    return render_template("distributor_registration.html")


@public.route('/pharmacy_register',methods=['get','post'])
def pharmacy_register():
    if 'submit' in request.form:
        name=request.form['name']
        pwd=request.form['pwd']
        place=request.form['place']
        city=request.form['city']

        phone=request.form['phone']
        email=request.form['email']
        licence=request.form['licence']
        print(name,place,city,email,phone,licence,pwd)
        q="insert into login values (null,'%s','%s','%s')"%(email,pwd,'pending')
        lin=insert(q)
        qry="insert into pharmacy values(null,'%s','%s','%s','%s','%s','%s','%s')"%(lin,name,place,city,email,phone,licence)
        insert(qry)
        flash("Successfully Registered!!")
        return redirect(url_for('public.pharmacy_register'))
    return render_template("pharmacy_registration.html")