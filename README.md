# 🌤️ Weather Forecast Web App

A simple and responsive web application built with **Python** and **Flask** that displays real-time weather information using the [OpenWeatherMap API](https://openweathermap.org/api).  
Users can enter any city to get the current temperature, weather description, and a representative icon.

---

## 🚀 Features

- 🌍 Search weather by city name
- 📡 Real-time data fetched from OpenWeatherMap API
- 🧠 Error handling for invalid city names
- 🌐 Deployed live on Render.com
- 💻 Clean and minimal UI

---

## 🔧 Technologies Used

- Python
- Flask
- HTML & CSS
- OpenWeatherMap API
- Render (for deployment)
- Git & GitHub

---

## 🎥 Demo

[Live App](https://your-render-app-url.onrender.com)

*Replace the link above with your real Render URL*

---

## 📷 Screenshots

*(Optional — you can take a screenshot of your app and include it here)*

---

## 🛠️ Setup Instructions

To run the app locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/Scribbzz/weather-forecast-app.git
    cd weather-forecast-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Add your OpenWeatherMap API key:
    - Open `app.py` and replace `"your_openweathermap_api_key_here"` with your actual API key.

5. Run the app:
    ```bash
    python app.py
    ```

6. Visit `http://localhost:5000` in your browser.

---

## 📂 Project Structure
weather-forecast-app/ ├── app.py ├── requirements.txt ├── Procfile ├── templates/ │ └── index.html └── README.md

## 📄 License

This project is open-source and free to use under the MIT License.
