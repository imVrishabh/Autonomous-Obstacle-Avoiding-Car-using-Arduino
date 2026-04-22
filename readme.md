# 🚗 Arduino Autonomous Obstacle Avoiding Car (4 Motor Control)

This project is a fully autonomous robot car built using Arduino that detects obstacles and navigates its path using real-time sensor data and decision logic.

Unlike basic setups, this version uses **direct 4-channel motor control (no AFMotor library)** for better understanding of motor driver logic.

---

## 🔧 Features

* Real-time obstacle detection using ultrasonic sensor
* Servo-based scanning (left & right)
* Autonomous navigation (no manual control)
* Direct 4-channel motor control (IN1–IN4)
* Fully battery-powered system

---

## ⚙️ Components Used

* Arduino Uno
* Ultrasonic Sensor (HC-SR04)
* Servo Motor (SG90)
* Motor Driver (L298N / L293D module with exposed pins)
* 4 DC Motors
* Lithium-ion Battery

---

## 🧠 Working Principle

1. Car moves forward continuously
2. Ultrasonic sensor detects distance in front
3. If obstacle is detected:

   * Car stops
   * Moves backward
   * Servo scans left and right
   * Compares distances
4. Car turns towards the direction with more space
5. Continues moving autonomously

---

## 🔌 Connections

### Motor Driver (4 Channel Control)

* IN1 → Pin 2
* IN2 → Pin 3
* IN3 → Pin 4
* IN4 → Pin 5

### Ultrasonic Sensor

* TRIG → A1
* ECHO → A0

### Servo Motor

* Signal → Pin 10

---

## 💻 Code Structure

* Distance measurement using ultrasonic sensor
* Servo scanning for decision making
* Manual motor control using digital pins
* Direction logic based on sensor input

---

## ⚠️ Challenges Faced

* Power distribution issues with 4 motors
* Current limitations of motor drivers
* Debugging wiring and connections
* Sensor noise and unstable readings

---

## 🚀 Future Improvements

* Speed control using PWM
* Bluetooth / mobile control
* Camera-based obstacle detection
* Smarter navigation algorithms

---

## 📸 Demo



---

## 📂 Code

The complete Arduino code is available in this repository.

---

## 📬 Connect

Feel free to fork, modify, or suggest improvements.

#Arduino #Robotics #EmbeddedSystems #IoT #Automation
