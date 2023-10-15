package com.example.medicinerecommendation;



import java.util.Locale;

import org.json.JSONObject;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.speech.tts.TextToSpeech;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

public class ScanQR extends Activity implements JsonResponse
{
    public static String vals,manufacturer,distributor,pharmacy,medicine,medicine_id,quantity;
    SharedPreferences sh;
    /** Called when the activity is first created. */
    String method="getslotidandlocid";
    String soapaction="http://tempuri.org/getslotidandlocid";
    static final String ACTION_SCAN = "com.google.zxing.client.android.SCAN";
    public static TextToSpeech t1;
    public static String amount,merchant,mid;
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scan_qr);

    }

//    public void scanBar(View v) {
//        try {
//            Intent intent = new Intent(ACTION_SCAN);
//            intent.putExtra("SCAN_MODE", "PRODUCT_MODE");
//            startActivityForResult(intent, 0);
//        } catch (ActivityNotFoundException anfe) {
//            showDialog(ScanQR.this, "No Scanner Found", "Download a scanner code activity?", "Yes", "No").show();
//        }
//    }

    public void scanQR(View v) {
        try {
            Intent intent = new Intent(ACTION_SCAN);
            intent.putExtra("SCAN_MODE", "QR_CODE_MODE");
            startActivityForResult(intent, 0);
        } catch (ActivityNotFoundException anfe) {
            showDialog(ScanQR.this, "No Scanner Found", "Download a scanner code activity?", "Yes", "No").show();
        }
    }
//	public void GenerateQR(View v) {
//		startActivity(new Intent(getApplicationContext(),qrcode.class));
//	}

    private static AlertDialog showDialog(final Activity act, CharSequence title, CharSequence message, CharSequence buttonYes, CharSequence buttonNo) {
        AlertDialog.Builder downloadDialog = new AlertDialog.Builder(act);
        downloadDialog.setTitle(title);
        downloadDialog.setMessage(message);
        downloadDialog.setPositiveButton(buttonYes, new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialogInterface, int i) {
                Uri uri = Uri.parse("market://search?q=pname:" + "com.google.zxing.client.android");
                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                try {
                    act.startActivity(intent);
                } catch (ActivityNotFoundException anfe) {

                }
            }
        });
        downloadDialog.setNegativeButton(buttonNo, new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialogInterface, int i)
            {
            }
        });
        return downloadDialog.show();
    }

    public void onActivityResult(int requestCode, int resultCode, Intent intent) {
        if (requestCode == 0) {
            if (resultCode == RESULT_OK) {
                String contents = intent.getStringExtra("SCAN_RESULT");
                sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                SharedPreferences.Editor e = sh.edit();
                e.putString("contents", contents);
                e.putString("profile", "qr_result");
                e.commit();
                String format = intent.getStringExtra("SCAN_RESULT_FORMAT");

                JsonReq JR=new JsonReq();
                JR.json_response=(JsonResponse)ScanQR.this;
                String uid = sh.getString("user_id", "");
                String q="/AndroidBarcodeQrExample?contents="+contents;
                q=q.replace(" ","%20");
                JR.execute(q);
            }
        }
    }

    @Override
    public void response(JSONObject jo) {
        try {


            String status = jo.getString("status");


            Log.d("pearl", status);



            if (status.equalsIgnoreCase("success")) {
//				Toast.makeText(getApplicationContext(), "Attendance Marked", Toast.LENGTH_LONG).show();
                manufacturer=jo.getString("mname");
                distributor=jo.getString("dname");
                pharmacy=jo.getString("pname");
                medicine=jo.getString("medname");
                medicine_id=jo.getString("med_id");
                quantity=jo.getString("quantity");
                startActivity(new Intent(getApplicationContext(), Medicinedetails.class));
            }
            else{
                Toast.makeText(getApplicationContext(), "Date Not Matched", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), ScanQR.class));
            }



        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        startActivity(new Intent(getApplicationContext(),userhome.class));

    }
}