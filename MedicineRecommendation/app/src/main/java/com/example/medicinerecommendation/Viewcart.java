package com.example.medicinerecommendation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Viewcart extends AppCompatActivity implements JsonResponse{
    ListView l1;
    String[] medicine,amount,quantity,total,details,ordermasterid;
   public static int amnt=0;
    Button b1;
    SharedPreferences sh;
    TextView t1;
    public static int omid;
    public static String tot;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewcart);
        t1=(TextView)findViewById(R.id.total);

        l1 = (ListView) findViewById(R.id.cartlist);
        b1 = (Button) findViewById(R.id.payment);
        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)Viewcart.this;
        String uid = sh.getString("user_id", "");
        String q="/view_cart?user_id="+ uid;
        q = q.replace(" ", "%20");
        JR.execute(q);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),payment.class));
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
                tot=jo.getString("total");
                t1.setText("Grand Total : "+tot);
                medicine = new String[ja1.length()];
                amount = new String[ja1.length()];
                quantity = new String[ja1.length()];
                total = new String[ja1.length()];
                ordermasterid = new String[ja1.length()];
                details = new String[ja1.length()];
                for (int i = 0; i < ja1.length(); i++) {


                    medicine[i] = ja1.getJSONObject(i).getString("med_name");
                    amount[i] = ja1.getJSONObject(i).getString("a");
                    ordermasterid[i] = ja1.getJSONObject(i).getString("order_master_id");
                    quantity[i] = ja1.getJSONObject(i).getString("quantity");
//                    total[i] = ja1.getJSONObject(i).getString("total");
//                    amnt=amnt+Integer.parseInt(total[i]);
                    omid=Integer.parseInt(ordermasterid[i]);
                    details[i] = "Medicine : " + medicine[i] + "\nAmount : " + amount[i] + "\nQuantity : "+ quantity[i] ;



//                    Toast.makeText(getApplicationContext(), details[i], Toast.LENGTH_LONG).show();

                }

//                ArrayAdapter<String> itemsAdapter =
//                        new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, details);
//                ListView listView = (ListView) findViewById(R.id.order);
//                listView.setAdapter(itemsAdapter);

//
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, details);

                l1.setAdapter(ar);
            }
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
        startActivity(new Intent(getApplicationContext(),userhome.class));

    }
}