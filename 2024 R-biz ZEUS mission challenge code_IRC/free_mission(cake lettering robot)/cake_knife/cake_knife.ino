#include <Dynamixel2Arduino.h>

// Please modify it to suit your hardware.
#if defined(ARDUINO_AVR_UNO) || defined(ARDUINO_AVR_MEGA2560) // When using DynamixelShield
  #include <SoftwareSerial.h>
  SoftwareSerial soft_serial(7, 8); // DYNAMIXELShield UART RX/TX
  #define DXL_SERIAL   Serial
  #define DEBUG_SERIAL soft_serial
  const int DXL_DIR_PIN = 2; // DYNAMIXEL Shield DIR PIN
#elif defined(ARDUINO_SAM_DUE) // When using DynamixelShield
  #define DXL_SERIAL   Serial
  #define DEBUG_SERIAL SerialUSB
  const int DXL_DIR_PIN = 2; // DYNAMIXEL Shield DIR PIN
#elif defined(ARDUINO_SAM_ZERO) // When using DynamixelShield
  #define DXL_SERIAL   Serial1
  #define DEBUG_SERIAL SerialUSB
  const int DXL_DIR_PIN = 2; // DYNAMIXEL Shield DIR PIN
#elif defined(ARDUINO_OpenCM904) // When using official ROBOTIS board with DXL circuit.
  #define DXL_SERIAL   Serial3 //OpenCM9.04 EXP Board's DXL port Serial. (Serial1 for the DXL port on the OpenCM 9.04 board)
  #define DEBUG_SERIAL Serial
  const int DXL_DIR_PIN = 22; //OpenCM9.04 EXP Board's DIR PIN. (28 for the DXL port on the OpenCM 9.04 board)
#elif defined(ARDUINO_OpenCR) // When using official ROBOTIS board with DXL circuit.
  #define DXL_SERIAL   Serial3
  #define DEBUG_SERIAL Serial
  const int DXL_DIR_PIN = 84; // OpenCR Board's DIR PIN.
#elif defined(ARDUINO_OpenRB)  // When using OpenRB-150
  #define DXL_SERIAL Serial1
  #define DEBUG_SERIAL Serial
  const int DXL_DIR_PIN = -1;
#else // Other boards when using DynamixelShield
  #define DXL_SERIAL   Serial1
  #define DEBUG_SERIAL Serial
  const int DXL_DIR_PIN = 2; // DYNAMIXEL Shield DIR PIN
#endif
 

const uint8_t DXL_ID = 2; //노터치
const float DXL_PROTOCOL_VERSION = 2.0; //노터치
const uint8_t signal = 7;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

//This namespace is required to use Control table item names
using namespace ControlTableItem;

void setup() {
  // put your setup code here, to run once:
  pinMode(7, INPUT);
  // Use UART port of DYNAMIXEL Shield to debug.
  DEBUG_SERIAL.begin(115200);
  while(!DEBUG_SERIAL);

  // Set Port baudrate to 1000000bps. This has to match with DYNAMIXEL baudrate.
  dxl.begin(1000000); //노터치
  // Set Port Protocol Version. This has to match with DYNAMIXEL protocol version.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  // Get DYNAMIXEL information
  dxl.ping(DXL_ID); //노터치

  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(DXL_ID); //노터치
  dxl.setOperatingMode(DXL_ID, OP_POSITION); //노터치
  dxl.torqueOn(DXL_ID); //노터치 

  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 70); // 속도조절 여기서해~
}

void loop() {
  // dxl.setGoalPosition(DXL_ID, 0.0, UNIT_DEGREE);
  // delayUntilGoalPosition(0.0);

  if (digitalRead(signal) == 1) {
    dxl.setGoalPosition(DXL_ID, 180.0, UNIT_DEGREE); // 원하는 각도 "180"부분 수정
    delayUntilGoalPosition(180.0); // 각도 도달할때까지 기다리는 함수
    Serial.println("1");
  }
  else {
    dxl.setGoalPosition(DXL_ID, 0.0, UNIT_DEGREE); // 원하는 각도 "0"부분 수정
    delayUntilGoalPosition(0.0); // 각도 도달할때까지 기다리는 함수
    Serial.println("0");
  }
  
}

// Function to wait until the servo reaches the target position
void delayUntilGoalPosition(float target_position) {
  float current_position = dxl.getPresentPosition(DXL_ID, UNIT_DEGREE);
  
  while (abs(target_position - current_position) > 1.0) {
    current_position = dxl.getPresentPosition(DXL_ID, UNIT_DEGREE);
    DEBUG_SERIAL.print("Present_Position(degree) : ");
    DEBUG_SERIAL.println(current_position);
    DEBUG_SERIAL.println(digitalRead(signal));
    delay(10); // Check position every 10ms
  }
}
