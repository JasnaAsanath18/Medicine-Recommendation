
from flask import *
from database import *
import json
from  web3 import Web3,HTTPProvider
import uuid
import qrcode

manufacturer=Blueprint('manufacturer',__name__)


# -----------------------------------------------------------------------------------

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = 'C:/Users/jessi/Desktop/medicine delivery/build/contracts/medicine.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x7590261Ffd9660DAf797b39208EAD7E9d978F22C'



# --------------------------------------------------------------------------------------



@manufacturer.route('/manufacturer_home')
def manufacturerhome():
    return render_template("manufacturer_home.html")

@manufacturer.route('/add_medicine',methods=['get','post'])
def add_medicine():
    data={}
    qry="select * from manufacture inner join medicine using (manufacture_id) where manufacture_id='%s'"%(session['manufacture_id'])
    data['res']=select(qry)
    if 'id' in request.args:
        medic_id=request.args['id']
    if 'submit' in request.form:
        mname=request.form['name']
        type=request.form['type']
        amount=request.form['amount']
        cn=request.form['cn']
        n=request.form['nature']
        ul=request.form['label']
        se=request.form['se']
        storage=request.form['storage']
        ed=request.form['ed']
        path="static/qr_code/"+str(uuid.uuid4())+".png"

       
        qry="insert into medicine values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(session['manufacture_id'],mname,type,amount,cn,n,ul,se,storage,ed,path)
        res=insert(qry)
        s=qrcode.make(str(res))
        s.save(path)
        return redirect(url_for('manufacturer.add_medicine'))
    return render_template("manufacturer_add_medicine.html",data=data)

# @manufacturer.route('/addstock_man',methods=['get','post'])
# def addstock():
#     data={}
#     rid=request.args['reqid']
#     phar_id=request.args['pharid']
#     medid=request.args['medid']
#     distid=request.args['distid']
#     qry="select * from request where request_id='%s'"%(rid)
#     data['res']=select(qry)
#     print(data['res'])
#     if 'submit' in request.form:
        
#         a=request.form['stock']
#         b=request.form['mfg']
#         # c=request.form['distributor1']
#         # d=request.form['pharmacy1']
#         qey="insert into stock values(null,'%s','%s','%s','%s','%s','%s',curdate(),'null')"%(medid,session['manufacture_id'],distid,phar_id,a,b)
#         insert(qey)
#         return redirect(url_for('manufacturer.manu_view_request'))
#     return render_template("manufacturer_add_stock.html",data=data)




@manufacturer.route('/addstock_man',methods=['get','post'])
def addstock():
    data={}
    qry="select * from distributor"
    data['res']=select(qry)
    qr1="select * from pharmacy"
    data['res1']=select(qr1)
    
    medid=request.args['medid']
    if 'submit' in request.form:
        
        a=request.form['stock']
        b=request.form['mfg']
        c=request.form['distributor1']
        d=request.form['pharmacy1']
        qey="insert into stock values(null,'%s','%s','%s','%s','%s','%s',curdate(),'null')"%(medid,session['manufacture_id'],c,d,a,b)
        insert(qey)
        return redirect(url_for('manufacturer.add_medicine'))
    return render_template("manufacturer_add_stock1.html",data=data)

@manufacturer.route('/manu_view_request')
def manu_view_request():
    data={}
    qry="SELECT * FROM request INNER JOIN medicine USING(medicine_id) INNER JOIN distributor USING(distributor_id) WHERE request.`manufacture_id`='%s'"%(session['manufacture_id'])
    data['res']=select(qry)
    if 'action' in request.args:
        action=request.args['action']
        reqid=request.args['reqid']
    else:
        action=None
    if action=='accept':
        # qry="update request set status='approved' where request_id='%s'"%(reqid)
        qry2="select * from request where request_id='"+reqid+"'"
        print(qry2)
        data=select(qry2)
        phar_id=data[0]['pharmacy_id']
        dist_id=data[0]['distributor_id']
        manu_id=data[0]['manufacture_id']
        quantity=data[0]['quantity']
        med_id=data[0]['medicine_id']
        # ----------------------------------------------
        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()

        # contract function name
        message2 = contract.functions.add_info(blocknumber,int(phar_id),int(dist_id),int(manu_id),int(quantity),int(med_id)).transact()
        res1 = []
        # for i in range(blocknumber + 1, 14, -1):

        #     print(i)
        #     a = web3.eth.get_transaction_by_block(i, 0)
        #     decoded_input = contract.decode_function_input(a['input'])
        #     print(decoded_input)

        return '''<script>alert("Inserted..");window.location="/manu_view_request"</script>'''





        # --------------------------------------------------


        # update(qry)
    if action=='reject':
        qry="update request set status='rejected' where request_id='%s'"%(reqid)
        update(qry)
    return render_template("manufacturer_view_request.html",data=data)


@manufacturer.route('/manu_view_accepted_req')
def manu_accepted_req():
    data1 = []
    with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    print(blocknumber)
    res1 = []
    for i in range(blocknumber, 42, -1):
        data={}
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        print(decoded_input)
        try:
            if str(decoded_input[1]['_manuid'])==str(session['manufacture_id']):


                data['pharmacy']=decoded_input[1]['_phrid']
                data['distributor']=decoded_input[1]['_distid']
                data['manufacturer']=decoded_input[1]['_manuid']
                data['quantity']=decoded_input[1]['_quantity']
                data['medicine']=decoded_input[1]['_medid']

                data1.append(data)
        except:
             return '''<script>alert("no data..");window.location="/manu_view_request"</script>'''



    print(data1)
    l1=[]
    for row in data1:
        data2={}
        q="select * from distributor where distributor_id='"+str(row['distributor'])+"'"
        q1="select * from manufacture where manufacture_id='"+str(row['manufacturer'])+"'"
        q2="select * from pharmacy where pharmacy_id='"+str(row['pharmacy'])+"'"
        q3="select * from medicine where medicine_id='"+str(row['medicine'])+"'"
        res=select(q)
        res1=select(q1)
        res2=select(q2)
        res3=select(q3)
        data2['dname']=res[0]['fname'] + res[0]['lname']
        data2['mname']=res1[0]['name']
        data2['pname']=res2[0]['pharmacy_name']
        data2['medname']=res3[0]['med_name']
        data2['quantity']=row['quantity']
        l1.append(data2)

    print(l1,"aaaaaaaaaaaaaaaaaaaaaaa")
    return render_template("manufacturer_view_accepted_req.html",data=l1)