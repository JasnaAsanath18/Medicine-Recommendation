

package com.example.medicinerecommendation;

        import androidx.appcompat.app.AppCompatActivity;

        import android.content.Intent;
        import android.content.SharedPreferences;
        import android.os.Bundle;
        import android.preference.PreferenceManager;
        import android.util.Log;
        import android.widget.ArrayAdapter;
        import android.widget.ImageView;
        import android.widget.Toast;

        import com.squareup.picasso.Picasso;

        import org.json.JSONArray;
        import org.json.JSONObject;

public class qr extends AppCompatActivity implements JsonResponse{
    ImageView img1;
    SharedPreferences sh;
    String qrcode,val;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_qr);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        img1=(ImageView) findViewById(R.id.img1);


//	       Toast.makeText(context, pth, Toast.LENGTH_LONG).show();

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)qr.this;
        String q="/user_view_qr?medicine_id="+Medicines.med_id;
        q = q.replace(" ", "%20");
        JR.execute(q);



    }
    @Override
    public void response(JSONObject jo) {
        try{
            String status=jo.getString("status");
            Log.d("pearl", status);


            if(status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("check");
//                qrcode = new String[ja1.length()];


//                val = new String[ja1.length()];
//                for (int i = 0; i < ja1.length(); i++) {


                qrcode = ja1.getJSONObject(0).getString("qr_code");
                String pth = "http://" + sh.getString("ip", "") + "/" + qrcode;
                pth = pth.replace("~", "");

                Log.d("-------------", pth);
                Picasso.with(getApplicationContext())
                        .load(pth)
                        .placeholder(R.drawable.ic_launcher_background)
                        .error(R.drawable.ic_launcher_background).into(img1);

//                    Toast.makeText(getApplicationContext(), details[i], Toast.LENGTH_LONG).show();

//                }

            }
        }
        catch(Exception e){
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), "Something happened"+e, Toast.LENGTH_LONG).show();
        }
    }

    public void onBackPressed()
    {
        // TODO Auto-generated method stub2
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(), Medicines.class);
        startActivity(b);
    }
}