#include <ESP8266WiFi.h>

//define WiFi connection information
//current not connecting to a network, so commented out
//const char* ssid = "";
//const char* password = "";

bool scanReady = false;
long lastScanMillis;
String command;

void setup() {
    //Setup serial communication
    Serial.begin(115200);
    delay(100);
    Serial.println("Connected to Serial Interface");

    //initialize Wifi, but disconnect so its not doing anything
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();
    delay(100);
}

void loop() {
    while(Serial.available()){
        command = Serial.readString();
        if (command.startsWith("M:")){
            scanReady = true;
            //Serial.println("Scanning networks...");
        }
    }
    
    if (scanReady){
        WiFi.scanNetworks(true); //true variable is to set the scan method as async, meaning we can do other stuff while it is scanning
        scanReady = false;
    }
    int n = WiFi.scanComplete();    //checks if the previous run scannetworks function has completed. (runs asychronous). returns -1 if not done. returns -2 if no scan is active
    //if scan is complete, print information for each network
    if(n >= 0){
        //Serial.printf("%d network(s) found\n", n);
        for (int i = 0; i < n; i++){
            if(WiFi.SSID(i).startsWith("SPS")){
                 //Serial.printf("%d: %s, Ch:%d (%ddBm) %s\n", i+1, WiFi.SSID(i).c_str(), WiFi.channel(i), WiFi.RSSI(i), WiFi.encryptionType(i) == ENC_TYPE_NONE ? "open" : ""); //print network information
                Serial.println(command+":"+WiFi.RSSI(i)+":"+WiFi.channel(i));//+":"+WiFi.SSID(i));
            }
        }
        WiFi.scanDelete(); //clears the scanning result from memory to prevent repeating data
        //Serial.println("Scan Complete");
        command = "";
    }
}
