from flask import *
from database import *
from web3 import Web3,HTTPProvider
import json

pharmacy=Blueprint('pharmacy',__name__)



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

@pharmacy.route('/pharmacyhome')
def pharmacyhome():
    return render_template("pharmacy_home.html")


@pharmacy.route('/viewmedicine')
def viewmedicine():
    data={}
    qry="SELECT * FROM `medicine` inner join manufacture using(manufacture_id)"
    data['res']=select(qry)
    # if 'action' in request.args:
    #     action=request.args['action']
        
    # else:
    #     action=None

    # if action=='accept':
    #     qry="update login set usertype='%s' where login_id='%s'"%('manufacturer',session['lid'])
    #     update(qry)
    return render_template("pharmacy_view_medicines.html",data=data)

@pharmacy.route('/sendrequest',methods=['get','post'])
def sendrequest():
    data={}
    mf_id=request.args['manuid']

    md_id=request.args['medid']
    s="select * from distributor"
    data['res']=select(s)

    if 'submit' in request.form:
        qty=request.form['qty'] 
        dist=request.form['distri']
        qry="insert into request values(null,'%s','%s','%s','%s','%s','pending')"%(session['phar_id'],dist,mf_id,qty,md_id)
        print(qry)
        insert(qry)
        return redirect(url_for('pharmacy.viewmedicine'))
    return render_template("pharmacy_send_request.html",data=data)


@pharmacy.route('/viewrequestpharmacy')
def viewrequestpharmacy():
    data={}
    s="select * from request inner join medicine using(medicine_id) where pharmacy_id='%s'"%(session['phar_id'])
    data['res']=select(s)
    return render_template("pharmacy_view_request.html",data=data)


@pharmacy.route('/phr_accepted_req')
def phr_accepted_req():
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
        if str(decoded_input[1]['_phrid'])==str(session['phar_id']):


            data['pharmacy']=decoded_input[1]['_phrid']
            data['distributor']=decoded_input[1]['_distid']
            data['manufacturer']=decoded_input[1]['_manuid']
            data['quantity']=decoded_input[1]['_quantity']
            data['medicine']=decoded_input[1]['_medid']

            data1.append(data)
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

    return render_template("pharmacy_accepted_req.html",data=l1)