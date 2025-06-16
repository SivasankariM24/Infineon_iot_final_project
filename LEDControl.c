#define LED1 23   // Connect 1st LED to GPIO23
#define LED2 22   // Connect 2nd LED to GPIO22

void setup() {
  Serial.begin(115200);         // Starts serial communication at 115200 baud rate
  pinMode(LED1, OUTPUT);        // Set GPIO23 as output for LED1
  pinMode(LED2, OUTPUT);        // Set GPIO22 as output for LED2
}

void loop() {
  if (Serial.available()) {     // Checks if data is available on the serial port
    char data = Serial.read();  // Reads the incoming character

    if (data == '1') {          // If character '1' is received
      digitalWrite(LED1, HIGH); // Turn ON LED1
      digitalWrite(LED2, LOW);  // Turn OFF LED2
    }
    else if (data == '2') {     // If character '2' is received
      digitalWrite(LED1, LOW);  // Turn OFF LED1
      digitalWrite(LED2, HIGH); // Turn ON LED2
    }
    else if (data == '0') {     // If character '0' is received
      digitalWrite(LED1, LOW);  // Turn OFF both LEDs
      digitalWrite(LED2, LOW);
    }
  }
}
