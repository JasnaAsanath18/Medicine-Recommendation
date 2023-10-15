package com.example.medicinerecommendation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONObject;

public class feedback extends AppCompatActivity implements JsonResponse{
    String feedback;
    EditText e1;
    Button b1;
    SharedPreferences sh;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_feedback);

        e1=(EditText) findViewById(R.id.feedback);
        b1=(Button) findViewById(R.id.feedbackbtn);



        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                feedback = e1.getText().toString();


                JsonReq jr = new JsonReq();
                jr.json_response = (JsonResponse) feedback.this;
                String uid = sh.getString("user_id", "");
                String q = "/user_feedback?feedback=" + feedback + "&uid=" + uid;
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
                Toast.makeText(getApplicationContext(), "Successfully sent", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(),userhome.class));
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
        startActivity(new Intent(getApplicationContext(),userhome.class));

    }
}