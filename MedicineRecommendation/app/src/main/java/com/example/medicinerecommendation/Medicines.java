package com.example.medicinerecommendation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import android.view.View;


import org.json.JSONArray;
import org.json.JSONObject;

public class Medicines extends AppCompatActivity implements JsonResponse{
    ListView medicines;
    public static String med_id;
    String[] medicine,type,amount,val,medicine_id;
    Button b1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_medicines);
        medicines=(ListView)findViewById(R.id.medicine);
        b1=(Button)findViewById(R.id.viewcart);

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)Medicines.this;
        String q="/user_view_medicines";
        q = q.replace(" ", "%20");
        JR.execute(q);

        medicines.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int i, long id) {
                med_id=medicine_id[i];
                startActivity(new Intent(getApplicationContext(),ScanQR.class));
            }
        });
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),Viewcart.class));
            }
        });

    }
    @Override
    public void response(JSONObject jo) {
        try{
            String status=jo.getString("status");
            Log.d("pearl", status);


            if(status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("check");
                medicine = new String[ja1.length()];
                medicine_id = new String[ja1.length()];
                type= new String[ja1.length()];
                amount = new String[ja1.length()];
                val = new String[ja1.length()];
                for (int i = 0; i < ja1.length(); i++) {


                    medicine[i] = ja1.getJSONObject(i).getString("med_name");
                    medicine_id[i] = ja1.getJSONObject(i).getString("medicine_id");
                    type[i]=ja1.getJSONObject(i).getString("ty");
                    amount[i]=ja1.getJSONObject(i).getString("a");
                    val[i] = "Medicine : " + medicine[i]+"\nType   :"+type[i]+"\nAmount  :"+amount[i];

//                    Toast.makeText(getApplicationContext(), details[i], Toast.LENGTH_LONG).show();

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, val);

                medicines.setAdapter(ar);
            }
        }
        catch(Exception e){
                    e.printStackTrace();
                    Toast.makeText(getApplicationContext(), "Something happened"+e, Toast.LENGTH_LONG).show();
                }
            }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        startActivity(new Intent(getApplicationContext(),userhome.class));

    }
}