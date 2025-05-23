from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "1ccebaa7983a82f95adffebc39fb8f19"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                weather = {'error': 'City not found!'}
    return render_template('index.html', weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
