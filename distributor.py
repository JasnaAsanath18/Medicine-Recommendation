from flask import *
from database import *
import json
from web3 import HTTPProvider,Web3
distributor=Blueprint('distributor',__name__)

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

@distributor.route('/distributorhome')
def distributorhome():
    return render_template("distributor_home.html")

@distributor.route('/view_medicine')
def view_medicine():
    data={}
    qry="select * from medicine inner join manufacture using (manufacture_id)"
    data['res']=select(qry)
    return render_template("distributor_viewmedicine.html",data=data)
@distributor.route('/view_medicine_request')
def view_medicine_request():
    data={}
    qry="SELECT * FROM request INNER JOIN manufacture USING(manufacture_id) INNER JOIN medicine ON request.`medicine_id`=medicine.`medicine_id` where distributor_id='%s'"%(session['dist_id'])
    data['res']=select(qry)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['rid']

        if action == 'add':


            # qry="update request set status='%s' where request_id='%s'"%('send',id)
            # update(qry)

            qry2="select * from request where request_id='"+id+"'"
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
            for i in range(blocknumber + 1, 14, -1):

                print(i)
                a = web3.eth.get_transaction_by_block(i, 0)
                decoded_input = contract.decode_function_input(a['input'])
                print(decoded_input)

            return '''<script>alert("Inserted..");window.location="/view_medicine_request"</script>'''





            # --------------------------------------------------





            # return redirect(url_for('distributor.view_medicine_request'))
    return render_template("distributor_view_medicine_request.html",data=data)

@distributor.route('/view_accepted_req')
def accepted_req():
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
            if str(decoded_input[1]['_distid'])==str(session['dist_id']):


                data['pharmacy']=decoded_input[1]['_phrid']
                data['distributor']=decoded_input[1]['_distid']
                data['manufacturer']=decoded_input[1]['_manuid']
                data['quantity']=decoded_input[1]['_quantity']
                data['medicine']=decoded_input[1]['_medid']

                data1.append(data)
        except:
            return '''<script>alert("zz");window.location="/view_medicine_request"</script>'''
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

    return render_template("distributor_accepted_req.html",data=l1)

@distributor.route('/send_to_manufactre')
def send_to_manufactre():
    rid=request.args.get('rid')
    q="update request set status='%s' where request_id='%s'"%('send',rid)
    update(q)
    return '''<script>alert("Inserted..");window.location="/view_medicine_request"</script>'''