import customtkinter as ctk
from api import fetch_weather
from utils import convert_temp
import geocoder

from PIL import Image, ImageTk
import requests
import io

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class WeatherApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("600x750")

        self.unit = ctk.StringVar(value="C")

        self.build_ui()

  

    def build_ui(self):
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=20)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(self.main_frame, text="🌦 Weather Dashboard", font=("Arial", 24)).pack(pady=10)

        self.entry = ctk.CTkEntry(self.main_frame, placeholder_text="Enter City")
        self.entry.pack(pady=10)

        btn_frame = ctk.CTkFrame(self.main_frame)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Search", command=self.search).grid(row=0, column=0, padx=5)
        ctk.CTkButton(btn_frame, text="Auto GPS", command=self.gps).grid(row=0, column=1, padx=5)

        ctk.CTkOptionMenu(self.main_frame, values=["C", "F"], variable=self.unit).pack(pady=5)

        # Weather Card
        weather_card = ctk.CTkFrame(self.main_frame, corner_radius=20)
        weather_card.pack(pady=15, fill="x", padx=10)

        self.temp_label = ctk.CTkLabel(weather_card, text="--°", font=("Arial", 42))
        self.temp_label.pack(pady=5)

        self.icon_label = ctk.CTkLabel(weather_card, text="")
        self.icon_label.pack()

        self.desc_label = ctk.CTkLabel(weather_card, text="")
        self.desc_label.pack()

        self.wind_label = ctk.CTkLabel(weather_card, text="")
        self.wind_label.pack()

        # Chart Frame
        self.chart_frame = ctk.CTkFrame(self.main_frame)
        self.chart_frame.pack(pady=20, fill="both", expand=True)

   

    def search(self):
        city = self.entry.get()
        if not city:
            self.temp_label.configure(text="Enter city")
            return
        self.update_weather(city)

    def gps(self):
        try:
            g = geocoder.ip('me')
            if not g.city:
                self.temp_label.configure(text="GPS Failed")
                return
            self.update_weather(g.city)
        except:
            self.temp_label.configure(text="GPS Error")

    def update_weather(self, city):
        data = fetch_weather(city)

        if not data:
            self.temp_label.configure(text="API Error / City not found")
            return

        current = data["current"]

        temp = convert_temp(current["temp_c"], self.unit.get())

        self.temp_label.configure(text=f"{temp:.1f}°{self.unit.get()}")
        self.desc_label.configure(text=current["condition"]["text"])
        self.wind_label.configure(text=f"Wind: {current['wind_kph']} km/h")

        # ICON
        icon_url = current["condition"]["icon"]
        icon_img = self.load_icon(icon_url)
        if icon_img:
            self.icon_label.configure(image=icon_img)
            self.icon_label.image = icon_img

        self.plot_hourly(data)
        self.plot_weekly(data)

 

    def load_icon(self, icon_url):
        try:
            icon_url = "https:" + icon_url
            response = requests.get(icon_url)
            img_data = response.content

            img = Image.open(io.BytesIO(img_data))
            img = img.resize((80, 80))

            return ImageTk.PhotoImage(img)
        except:
            return None


    def plot_hourly(self, data):
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        hours = data["forecast"]["forecastday"][0]["hour"]

        temps = []
        labels = []

        for i in range(8):
            t = convert_temp(hours[i]["temp_c"], self.unit.get())
            temps.append(t)
            labels.append(hours[i]["time"][11:16])

        fig = plt.Figure(figsize=(5,2), facecolor="#1a1a1a")
        ax = fig.add_subplot(111)

        ax.plot(labels, temps, marker='o')
        ax.set_title("Hourly Forecast", color="white")

        ax.set_facecolor("#1a1a1a")
        ax.tick_params(colors="white")

        for spine in ax.spines.values():
            spine.set_color("white")

        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=5)

    def plot_weekly(self, data):
        days = data["forecast"]["forecastday"]

        temps = []
        labels = []

        for d in days:
            t = convert_temp(d["day"]["avgtemp_c"], self.unit.get())
            temps.append(t)
            labels.append(d["date"][5:])

        fig = plt.Figure(figsize=(5,2), facecolor="#1a1a1a")
        ax = fig.add_subplot(111)

        ax.plot(labels, temps, marker='o')
        ax.set_title("7-Day Forecast", color="white")

        ax.set_facecolor("#1a1a1a")
        ax.tick_params(colors="white")

        for spine in ax.spines.values():
            spine.set_color("white")

        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=5)
