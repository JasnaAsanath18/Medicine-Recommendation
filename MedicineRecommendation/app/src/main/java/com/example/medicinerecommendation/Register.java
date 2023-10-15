package com.example.medicinerecommendation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import org.json.JSONArray;
import org.json.JSONObject;


public class Register extends AppCompatActivity implements JsonResponse{

    EditText e1,e2,e3,e4,e5,e6,e7,e8,e9;
    Button b1;
    String uname,pwd,fname,lname,dob,phone,email,place,dist;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        e1=(EditText) findViewById(R.id.uname);
        e2=(EditText) findViewById(R.id.pswd);
        e3=(EditText) findViewById(R.id.fname);
        e4=(EditText) findViewById(R.id.lname);
        e5=(EditText) findViewById(R.id.dob);
        e6=(EditText) findViewById(R.id.phone);
        e7=(EditText) findViewById(R.id.email);
        e8=(EditText) findViewById(R.id.place);
        e9=(EditText) findViewById(R.id.district);
        b1=(Button) findViewById(R.id.button);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                uname=e1.getText().toString();
                pwd=e2.getText().toString();
                fname=e3.getText().toString();
                lname=e4.getText().toString();
                dob=e5.getText().toString();
                phone=e6.getText().toString();
                email=e7.getText().toString();
                place=e8.getText().toString();
                dist=e9.getText().toString();


                JsonReq jr = new JsonReq();
                jr.json_response = (JsonResponse) Register.this;
                String q = "/register?uname=" + uname + "&pwd=" + pwd +"&fname=" + fname + "&lname=" + lname + "&dob=" + dob +"&phone=" + phone + "&email=" + email + "&place=" + place +"&dist=" + dist;
                q.replace(" ", "%20");
                jr.execute(q);
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        // TODO Auto-generated method stub

        try
        {
            String status=jo.getString("status");
            Toast.makeText(getApplicationContext(), status, Toast.LENGTH_LONG).show();
            if(status.equalsIgnoreCase("success"))
            {
                Toast.makeText(getApplicationContext(), "Registered Successfully", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(),MainActivity.class));
            }

            else
            {
                Toast.makeText(getApplicationContext(), "Not Successfull", Toast.LENGTH_LONG).show();
            }

        }
        catch(Exception e)
        {
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), "Hai"+e, Toast.LENGTH_LONG).show();
        }

    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        startActivity(new Intent(getApplicationContext(),MainActivity.class));

    }
}


