// morse-sender.ino

int sensorPin = A0;    // Wähle den Eingangspin für den Sensor
int outPin = 7;        // Wähle den Pin für die Ausgabe
int ledPin = 13;       // Pin für die Status-LED

void setup() {
  Serial.begin(115200);  // Initialisiere die serielle Kommunikation mit 115200 Baud, um mit dem Python-Skript übereinzustimmen
  pinMode(outPin, OUTPUT);
  digitalWrite(outPin, LOW);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop() {
  // Lese den Eingangspin A0, wenn "s" von Python gesendet wird
  if (Serial.available()) {
    char data = Serial.read();
    if (data == 's') {
      digitalWrite(ledPin, !digitalRead(ledPin));  // Status-LED umschalten
      int sensorValue = analogRead(sensorPin);
      Serial.println(sensorValue);
      Serial.flush();
      delay(1);  // Wartezeit zwischen den Lesevorgängen für Stabilität
    } else if (data == 'h') {
      digitalWrite(outPin, HIGH);
      digitalWrite(ledPin, HIGH);
      Serial.println("on");
      Serial.flush();
      delay(1);  // Wartezeit zwischen den Lesevorgängen für Stabilität
    } else if (data == 'l') {
      Serial.println("off");
      Serial.flush();
      digitalWrite(ledPin, HIGH);
      digitalWrite(outPin, LOW);
      delay(100);
      digitalWrite(ledPin, HIGH);
      delay(130);
      digitalWrite(ledPin, LOW);
      delay(100);
      digitalWrite(ledPin, HIGH);
      delay(130);
      digitalWrite(ledPin, LOW);
      delay(100);
      digitalWrite(ledPin, HIGH);
      delay(130);
      digitalWrite(ledPin, LOW);
      delay(100);
      digitalWrite(ledPin, HIGH);
      delay(130);
      digitalWrite(ledPin, LOW);
    }
  }
}
