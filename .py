#include <Servo.h>

// Motor pins (adjust if needed)
#define IN1 2
#define IN2 3
#define IN3 4
#define IN4 5

// Ultrasonic
#define trigPin A1
#define echoPin A0

Servo myServo;

long duration;
int distance;

void setup() {
  Serial.begin(9600);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  myServo.attach(10);
  myServo.write(90);
}

void loop() {

  distance = getDistance();

  if (distance > 20) {
    moveForward();
  } else {
    stopCar();
    delay(300);

    moveBackward();
    delay(400);

    stopCar();
    delay(300);

    int left = scanLeft();
    int right = scanRight();

    if (left > right) {
      turnLeft();
    } else {
      turnRight();
    }
  }
}

// ===== DISTANCE =====
int getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH, 30000);

  if (duration == 0) return 300;

  return duration * 0.034 / 2;
}

// ===== SERVO =====
int scanLeft() {
  myServo.write(150);
  delay(400);
  int d = getDistance();
  myServo.write(90);
  return d;
}

int scanRight() {
  myServo.write(30);
  delay(400);
  int d = getDistance();
  myServo.write(90);
  return d;
}

// ===== MOTOR CONTROL =====

void moveForward() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void moveBackward() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void turnLeft() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(400);
}

void turnRight() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  delay(400);
}

void stopCar() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}