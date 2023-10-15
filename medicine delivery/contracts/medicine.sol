pragma solidity >=0.4.22 <0.9.0;

contract medicine{
uint public vcount = 0;
mapping(uint => medicinedetails) public med;
struct medicinedetails{
	uint bid;
	uint phrid; 
	uint distid;
	uint manuid;
	uint quantity;
	uint medid;
	

}
uint public vcount1 = 0;
mapping(uint => purchasedetails) public pdetails;
struct purchasedetails{
	uint bid;
	uint omid; 
	uint userid;
	string total;
	string date;
	
	

}

function add_info(uint _bid,uint _phrid,uint _distid,uint _manuid,uint _quantity,uint _medid)public{
        vcount++;
     med[vcount]=medicinedetails(_bid,_phrid,_distid,_manuid,_quantity,_medid);
    }

function add_purchase_info(uint _bid,uint _omid,uint _userid,string memory _total,string memory _date)public{
        vcount1++;
     pdetails[vcount1]=purchasedetails(_bid,_omid,_userid,_total,_date);
    }

}