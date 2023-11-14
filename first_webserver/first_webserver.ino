#include <WiFi.h>
#include <WebServer.h>

//定义
const char* ssid = "some";
const char* password = "123456780";

WebServer server(80);
String header;
String output26State = "off";

const int output26 = 26;

//登录界面
void handelRoot(){
  String HTML = "<!DOCTYPE html>\
  <html>\
  <body>\
  哈喽，世界QAQ\
  </body>\
  </html>"; 
  server.send(200,"text/html",HTML);
}




void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  

 while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
   }
  Serial.print("\nIP地址： ");
  Serial.println(WiFi.localIP());

  server.on("/",handelRoot);//监听 xx 地址（路由）

  server.begin();
  pinMode(output26, OUTPUT);
  digitalWrite(output26,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  server.handleClient();
  digitalWrite(output26,HIGH);
  delay(500);
  digitalWrite(output26,LOW);
  delay(500);
  Serial.println("aa");
}
