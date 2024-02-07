int sensorPin = A0;    // select the input pin 
int outPin = 7;      // select the pin for the output
int ledPin = 13; // visual command indicator

void setup() {
  Serial.begin(115200);   // initialize serial communication at 115200 bits per second to match that of the python script
  pinMode(outPin, OUTPUT);
  digitalWrite(outPin, LOW);
  
#if 0
  pinMode(inputPin, INPUT_PULLUP);
  pinMode(inputPin, INPUT);
  int val = digitalRead(inputPin);
#endif

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readString();  // read the entire string from the serial buffer

    for (int i = 0; i < data.length(); i++) {
      char c = data.charAt(i);

      switch (c) {
        case '.':
          blink(1);  // Kurz
          break;
        case '-':
          blink(3);  // Lang
          break;
        case ' ':
          delay(3 * 250);  // Wortabstand (3 Mal den Kurzzeitraum)
          break;
        case 's':
          digitalWrite(ledPin, !digitalRead(ledPin));
          Serial.println(analogRead(sensorPin));
          Serial.flush();
          delay(1);        // delay in between reads for stability
          break;
        case 'h':
          digitalWrite(outPin, HIGH);
          digitalWrite(ledPin, HIGH);
          Serial.println("on");
          Serial.flush();
          delay(1);        // delay in between reads for stability
          break;
        case 'l':
          Serial.println("off");
          Serial.flush();
          digitalWrite(ledPin, HIGH);
          digitalWrite(outPin, LOW);
          delay(100);
          digitalWrite(ledPin, LOW);
          delay(100);
          break;
        default:
          break;
      }
      delay(250);  // Kurzzeitraum zwischen Morsezeichen
    }
  }
}

void blink(int units) {
  digitalWrite(ledPin, HIGH);  // LED einschalten
  delay(units * 250);  // Länge basierend auf Morse-Code-Einheiten (250 Millisekunden pro Einheit)
  digitalWrite(ledPin, LOW);   // LED ausschalten
  delay(100);  // Verzögerung nach dem Blinken
}