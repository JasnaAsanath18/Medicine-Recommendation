package com.example.medicinerecommendation;

import static com.example.medicinerecommendation.R.id.password;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Login extends AppCompatActivity implements JsonResponse{
EditText e1,e2;
Button b1;
String username,password,logid,usertype;
SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText) findViewById(R.id.uname);
        e2=(EditText)findViewById(R.id.password);
        b1= (Button) findViewById(R.id.login);



        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                username=e1.getText().toString();
                password=e2.getText().toString();
//                JsonReq jrr = new JsonReq();
//                jrr.json_response = (JsonResponse) Login.this;
//                String qr = "/AndroidBarcodeQrExample?contents=3" ;
//                qr.replace(" ", "%20");
//                jrr.execute(qr);

                JsonReq jr = new JsonReq();
                jr.json_response = (JsonResponse) Login.this;
                String q = "/login?username=" + username + "&password=" + password;
                q.replace(" ", "%20");
                jr.execute(q);




            }
        });

    }


    @Override
    public void response(JSONObject jo) {
        try {

            String status = jo.getString("status");
            String user_id = jo.getString("user_id");
            Log.d("pearl", status);

            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("check");
                logid = ja1.getJSONObject(0).getString("login_id");
                usertype = ja1.getJSONObject(0).getString("usertype");
                SharedPreferences.Editor e = sh.edit();
                Toast.makeText(this, usertype, Toast.LENGTH_SHORT).show();
                e.putString("log_id", logid);
                e.commit();
                e.putString("user_id", user_id);
                e.commit();
                if(usertype.equals("user"))
                {
                    Toast.makeText(getApplicationContext(),"Logged in Successfully", Toast.LENGTH_SHORT).show();//length long is here
                    startActivity(new Intent(getApplicationContext(), userhome.class));
                }

            }
            else {
                Toast.makeText(getApplicationContext(), "Login failed invalid username and password", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), Login.class));
            }
        } catch (Exception e) {
            // TODO: handle exception

            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        startActivity(new Intent(getApplicationContext(),MainActivity
                .class));

    }
}