# 🌦 Weather Dashboard Application

## 📌 Project Overview

The Weather Dashboard Application is a Python-based graphical user interface (GUI) application that provides real-time weather information using API integration. The app allows users to check current weather conditions, hourly forecasts, and weekly forecasts with an attractive and user-friendly interface.

---

## 🎯 Objectives

* To build a modern GUI using Python
* To integrate real-time weather data using API
* To display weather data in an interactive and visual manner
* To implement features like GPS detection and unit conversion

---

## 🚀 Features

### 🌦 Weather Information

* Current temperature and condition
* Wind speed
* Weather description
* Weather icons

### ⏰ Forecast

* Hourly forecast (next few hours)
* Weekly forecast (7 days)

### 📊 Data Visualization

* Embedded charts (Hourly & Weekly)
* Dark-themed graphs

### 📍 Location Detection

* Manual city input
* Automatic GPS-based location detection

### 🔄 Unit Conversion

* Celsius to Fahrenheit toggle

### 🎨 GUI Design

* Modern UI using CustomTkinter
* Card-based layout
* Clean and responsive interface

---

## 🛠 Technologies Used

* Python
* CustomTkinter (GUI)
* Matplotlib (charts)
* WeatherAPI (API integration)
* Requests (API calls)
* PIL (image handling)
* Geocoder (GPS detection)

---

## ⚙️ Installation

### Step 1: Install dependencies

pip install customtkinter requests pillow matplotlib geocoder

### Step 2: Add your API key

Open api.py and replace:
API_KEY = "37b99d24a18e4e249db204546262803"

### Step 3: Run the project

python main.py

---

## 📂 Project Structure

weather_app/
│
├── main.py
├── api.py
├── ui.py
├── utils.py

---

## ⚠️ Error Handling

* Invalid city input handled
* API errors handled
* GPS failures handled
* No crash system implemented

---

## 📈 Future Improvements

* Add database for search history
* Add weather alerts
* Add map integration
* Improve animations and UI effects

---

## 🏁 Conclusion

This project demonstrates the use of Python for building real-world applications using APIs, GUI design, and data visualization. It provides a complete solution for accessing and displaying weather data in an interactive way.

---

## 👨‍💻 Author

Sarthak Jindal

---

## License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, feel free to star the repository!

