from flask import *
from database import *
from web3 import Web3,HTTPProvider
import json

user=Blueprint('user',__name__)


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


@user.route('/addproduct_tocart',methods=['get'])
def addproduct():
    data={}
    med_id=request.args['medicine_id']
    qty=request.args['qty']
    user_id=request.args['userid']

    qry="select * from order_master where user_id='%s' and status='cart'"%(user_id)
    res=select(qry)
    if res:
        qry1="insert into `order` values(null,'%s','%s','%s')"%(res[0]['order_master_id'],med_id,qty)
        gg=insert(qry1)
        if gg:
             data['status']="success"
        else:   
            data['status']="failed"
        
    else:
        qry2="insert into order_master values(null,'%s','%s','cart',curdate())"%(user_id,0)
        lid=insert(qry2)
        qry3="insert into order values(null,'%s','%s','%s')"%(lid,med_id,qty)
        aa=insert(qry3)
        if aa:
             data['status']="success"
        else:   
            data['status']="failed"
    return str(data)


@user.route('/view_cart',methods=['get'])
def view_cart():
    data={}
    user_id=request.args['user_id']
    # qry="SELECT medicine.med_name,medicine.a,order.quantity,SUM(medicine.a*order.quantity) AS total FROM order_master JOIN `order` ON order_master.order_master_id=order.order_master_id JOIN medicine ON medicine.medicine_id=order.med_id WHERE order_master.status='cart' AND order_master.user_id='%s' GROUP BY medicine.medicine_id"%(id)
    qry="SELECT medicine.med_name,medicine.a,order.quantity,order_master.order_master_id FROM order_master JOIN `order` ON order_master.order_master_id=order.order_master_id JOIN medicine ON medicine.medicine_id=order.med_id WHERE order_master.status='cart' AND order_master.user_id='%s' "%(user_id)
    dt=select(qry)
    amt=0
    if dt:
        for i in dt:
            amt+=int(i['a'])*int(i['quantity'])
        data['status']="success"
        data['check']=dt
        data['total']=amt
    else:
         data['status']="failed"
    return str(data)

    
    # quan=data[0]['quantity']
    # price=data[0]['a']
    # total=int(quan)*int(price)
@user.route('/book_medicine')
def book_medicine():
    data={}
    om_id=request.args['om_id']
    u_id=request.args['user_id']
    total=request.args['total']
    qry="update order_master set status='booked',total='%s' where order_master_id='%s'"%(total,om_id)
    update(qry)
    q="insert into payment_cart values(null,'%s','%s',curdate())"%(u_id,total)
    r=insert(q)
    t="select total,date from order_master where order_master_id='%s'"%(om_id)
    val=select(t)
    total=val[0]['total']
    date=val[0]['date']

    # ----------------------------------------------

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()

    # contract function name
    message2 = contract.functions.add_purchase_info(blocknumber,int(om_id),int(u_id),total,date).transact()
    res1 = []
    
    for i in range(blocknumber + 1, 42, -1):

        print(i)
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        print(decoded_input)

    if r:
         data['status']="success"
    else:
         data['status']="failed"
    return(data)


###################################################################################################
@user.route('/user_feedback')
def feedback():
    data={}
    feedback=request.args['feedback']
    user_id=request.args['uid']
    qry="insert into feedback values(null,'%s','%s',curdate())"%(user_id,feedback)
    re=insert(qry)
    if re:
        data['status']="success"
    else:   
        data['status']="failed"
    return str(data)


# @user.route('/Feedbacks',methods=['get','post'])
# def Feedbacks():
# 	data={}
# 	feed=request.args['feed']
# 	users=request.args['users']
	

# 	q="INSERT INTO `feedback` VALUES(null,'%s','%s',curdate())"%(users,feed)
# 	id=insert(q)
# 	data['status']="success"
# 	data['method']="Feedbacks"
# 	return str(data)

@user.route('/register')
def register():
    data={}
    uname=request.args['uname']
    pwd=request.args['pwd']
    fname=request.args['fname']
    lname=request.args['lname']
    dob=request.args['dob']
    phone=request.args['phone']
    email=request.args['email']
    place=request.args['place']
    dist=request.args['dist']
    q1="insert into login values(null,'%s','%s','user')"%(uname,pwd)
    res=insert(q1)
    q2="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,dob,phone,email,place,dist)
    re=insert(q2)
    if re:
        data['status']="success"
    else:   
        data['status']="failed"
    return str(data)

@user.route('/login',methods=['get','post'])
def login():
    data={}
    uname=request.args['username']
    paswd=request.args['password']
    qry="select * from login where `username` ='%s' and `password`='%s'"%(uname,paswd)
    login=select(qry)
    if login:
        login_id=login[0]['login_id']
        if login[0]['usertype']=="user":
            qry="select * from user where login_id='%s'"%(login_id)
            deta=select(qry)
            if deta:
                data['user_id']=deta[0]['user_id']
                data['status']="success"
                data['check']=login
            else:
                data['status']="failed"
    return str(data)

@user.route('/user_view_medicines')
def user_viewmedicine():
    data={}
    qry="select * from medicine"
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)
    

@user.route('/user_view_qr')
def user_viewqr():
    mid=request.args['medicine_id']
    data={}
    qry="select qr_code from medicine where medicine_id='%s'"%(mid)
    res=select(qry)
    if res:
        data['status']="success"
        data['check']=res
    else:
        data['status']="failed"
    return str(data)    



# @user.route('/user_medicinedetails')
# def user_medicinedetails():
#     mid=request.args['medicine_id']
#     # print(mid,"medicine id")
#     data1 = []
#     with open(compiled_contract_path) as file:
#             contract_json = json.load(file)  # load contract info as JSON
#             contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
#     contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
#     blocknumber = web3.eth.get_block_number()
#     # print(blocknumber)
#     res1 = []
#     for i in range(blocknumber, 42, -1):
#         data={}
#         a = web3.eth.get_transaction_by_block(i, 0)
#         decoded_input = contract.decode_function_input(a['input'])
#         print(decoded_input)
#         try:
#             if str(decoded_input[1 ]['_medid'])==str(mid):


#                 data['pharmacy']=decoded_input[1]['_phrid']
#                 data['distributor']=decoded_input[1]['_distid']
#                 data['manufacturer']=decoded_input[1]['_manuid']
#                 data['quantity']=decoded_input[1]['_quantity']
#                 data['medicine']=decoded_input[1]['_medid']

#                 data1.append(data)
#         except:
#              return '''<script>alert("no data..");window.location="/user_medicinedetails"</script>'''



#     # print(data1)
#     l1=[]
#     for row in data1:
#         data2={}
#         q="select * from distributor where distributor_id='"+str(row['distributor'])+"'"
#         q1="select * from manufacture where manufacture_id='"+str(row['manufacturer'])+"'"
#         q2="select * from pharmacy where pharmacy_id='"+str(row['pharmacy'])+"'"
#         q3="select * from medicine where medicine_id='"+str(row['medicine'])+"'"
#         res=select(q)
#         res1=select(q1)
#         res2=select(q2)
#         res3=select(q3)
#         data2['dname']=res[0]['fname'] + res[0]['lname']
#         data2['mname']=res1[0]['name']
#         data2['pname']=res2[0]['pharmacy_name']
#         data2['medname']=res3[0]['med_name']
#         data2['quantity']=row['quantity']
#         l1.append(data2)

#     print(l1,"aaaaaaaaaaaaaaaaaaaaaaa")
#     return str(l1)

@user.route('/AndroidBarcodeQrExample')
def AndroidBarcodeQr():
    data={}
    lid=request.args['contents']
    print(lid,"MEdicine ID")
    # from datetime import datetime 
    # now = datetime.now()

    # date_time = now.strftime("%Y-%m-%d")
    # print("date and time:",date_time)



    # dt=date_time
    # print("DT : ",dt)

    # q="SELECT *,CONCAT(`user`.`fname`,' ',`user`.`lname`) AS user_name,`appointments`.`status` AS `statuss` FROM `appointments` INNER JOIN `schedule` USING(`schedule_id`) INNER JOIN `staff` USING(`staff_id`) INNER JOIN `designation` USING(`designation_id`) inner join user using(user_id) WHERE `appointment_id`='%s'"%(lid)
    # print(q)
    # res=select(q)
    # if res:
    #     if res[0]['date']==date_time:
    #         data['status']="success"
    #     else:
    #         data['status']='failed'


    data1 = []
    with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    # print(blocknumber)
    res1 = []
    for i in range(blocknumber, 42, -1):
        data={}
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        print(decoded_input,"decoded input")
        try:
            if str(decoded_input[1]['_medid'])==str(lid):


                data['pharmacy']=decoded_input[1]['_phrid']
                data['distributor']=decoded_input[1]['_distid']
                data['manufacturer']=decoded_input[1]['_manuid']
                data['quantity']=decoded_input[1]['_quantity']
                data['medicine']=decoded_input[1]['_medid']

                data1.append(data)
        except:
             return '''<script>alert("no data..");window.location="/user_medicinedetails"</script>'''



    # print(data1)
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
        data2['d_id']=res[0]['distributor_id']
        data2['mname']=res1[0]['name']
        data2['m_id']=res1[0]['manufacture_id']
        data2['pname']=res2[0]['pharmacy_name']
        data2['p_id']=res2[0]['pharmacy_id']
        data2['medname']=res3[0]['med_name']
        data2['med_id']=res3[0]['medicine_id']

        data2['quantity']=row['quantity']
        l1.append(data2)

    print(l1,"aaaaaaaaaaaaaaaaaaaaaaa")

    data2['status']="success"


    return str(data2)