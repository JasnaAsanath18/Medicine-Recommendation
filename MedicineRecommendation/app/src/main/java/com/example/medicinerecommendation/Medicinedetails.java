package com.example.medicinerecommendation;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Medicinedetails extends AppCompatActivity implements JsonResponse{
    TextView t1,t2,t3;
    String manufacturer,distributor,pharmacy,medicine_id,qty;
    Button b1,b2;
    SharedPreferences sh;
    EditText e1;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_medicinedetails);
        e1 = (EditText) findViewById(R.id.qnty);
        t1=(TextView) findViewById(R.id.textView8);
        t1.setText(ScanQR.manufacturer);
        t2=(TextView) findViewById(R.id.textView10);
        t2.setText(ScanQR.distributor);
        t3=(TextView) findViewById(R.id.textView12);
        t3.setText(ScanQR.pharmacy);
        b1=(Button) findViewById(R.id.cart);
        b2=(Button) findViewById(R.id.btnre);
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                qty=e1.getText().toString();
                JsonReq JR=new JsonReq();
                JR.json_response=(JsonResponse)Medicinedetails.this;
                String uid = sh.getString("user_id", "");
                String q="/report_medicine?medicine_id="+ScanQR.medicine_id+  "&userid=" + uid;
                q=q.replace(" ","%20");
                JR.execute(q);


            }
        });
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                qty=e1.getText().toString();
                JsonReq JR=new JsonReq();
                JR.json_response=(JsonResponse)Medicinedetails.this;
                String uid = sh.getString("user_id", "");
                String q="/addproduct_tocart?medicine_id="+ScanQR.medicine_id+ "&qty=" +qty+ "&userid=" + uid;
                q=q.replace(" ","%20");
                JR.execute(q);

            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try{
            String status=jo.getString("status");
            Log.d("pearl", status);


            if(status.equalsIgnoreCase("success")) {
//                JSONArray ja1 = (JSONArray) jo.getJSONArray("check");
//                medicine = new String[ja1.length()];
//                amount = new String[ja1.length()];
//                quantity = new String[ja1.length()];
//                total = new String[ja1.length()];
//                for (int i = 0; i < ja1.length(); i++) {
//
//
//                    medicine[i] = ja1.getJSONObject(i).getString("med_name");
//                    amount[i] = ja1.getJSONObject(i).getString("a");
//                    quantity[i] = ja1.getJSONObject(i).getString("quantity");
//                    total[i] = ja1.getJSONObject(i).getString("total");
//                    details[i] = "Hotel Name : " + medicine[i] + "\nAmount : " + amount[i] + "\nQuantity : "+ quantity[i] + "\nTotal : " + total[i];


                Toast.makeText(this, "product added", Toast.LENGTH_SHORT).show();
                startActivity(new Intent(getApplicationContext(),Medicines.class));
                }

//                ArrayAdapter<String> itemsAdapter =
//                        new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, details);
//                ListView listView = (ListView) findViewById(R.id.order);
//                listView.setAdapter(itemsAdapter);

//
//                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, details);
//
//                l1.setAdapter(ar);
//            }
//            else if (status.equalsIgnoreCase("delivered"))
//            {
//                Toast.makeText(this, "Delivered", Toast.LENGTH_LONG).show();
//                startActivity(new Intent(getApplicationContext(),Db_view_order.class));
//            }
//            else if (status.equalsIgnoreCase("undelivered"))
//            {
//                Toast.makeText(this, "Undelivered", Toast.LENGTH_LONG).show();
//                startActivity(new Intent(getApplicationContext(),Db_view_order.class));
//            }
//            else
//            {
//                Toast.makeText(getApplicationContext(), "Something happened", Toast.LENGTH_LONG).show();
//            }
        }
        catch(Exception e){
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), "Something happened"+e, Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        startActivity(new Intent(getApplicationContext(),ScanQR.class));

    }
}