🌦️ Weather Checker Application
A simple and user-friendly Streamlit web app that allows users to retrieve and view current weather conditions and a weekly forecast for any city, using real-time data from the OpenWeatherMap API.

🚀 Features
🔎 Enter any city name to fetch weather details

🌡️ Displays temperature, pressure, humidity, and wind speed

📆 Weekly forecast with daily min/max temperature and description

📍 Uses geographic coordinates (lat/lon) for forecast retrieval

📊 Responsive layout using st.columns() for clean UI

🧠 Environment variables loaded securely via .env

🔐 API keys are not hardcoded

📦 Packaged with Poetry for dependency management

🖥️ Streamlit UI Demo
bash
Copy
Edit
streamlit run app.py
Feature	Example
🌡️ Temperature	22.5 °C
💨 Wind Speed	5.5 m/s
📅 Forecast Day	Monday, July 29
🧾 Description	Scattered Clouds

🛠️ Tech Stack
Python 3.10+

Streamlit — for interactive UI

OpenWeatherMap API

requests — for API handling

python-dotenv — to manage secrets securely

datetime — for date parsing and formatting

📁 Project Structure
bash
Copy
Edit
weather-checker/
│
├── app.py                 # Main Streamlit app
├── .env                  # Holds your WEATHER_API key
├── .gitignore            # Standard Python ignore rules
├── README.md             # Project overview and usage
├── pyproject.toml        # Poetry dependencies
└── requirements.txt      # Exported for deployment if needed
🧪 Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/weather-checker.git
cd weather-checker
2. Set up virtual environment (with Poetry)
bash
Copy
Edit
poetry install
poetry shell
3. Add your .env file
Create a .env file with your OpenWeatherMap API key:

env
Copy
Edit
WEATHER_API=your_api_key_here
4. Run the app
bash
Copy
Edit
streamlit run app.py
🔑 How to Get an OpenWeatherMap API Key
Visit https://openweathermap.org/api

Sign up and log in

Create a new API key

Paste it into your .env file like shown above

📚 Stretch Goals (Optional Enhancements)
✅ Stretch A: Show Current Local Time
Display local time in both the user's timezone and the target city using pytz.

✅ Stretch B: Persistent Settings with JSON
Save user preferences (default city, temperature units, etc.) in a local settings.json file.

✅ Stretch C: Add Maps or Icons
Display an interactive map (using folium) or weather icons (using OpenWeatherMap's icon URLs).

🧾 Example Weather API Response (Trimmed)
json
Copy
Edit
{
  "coord": { "lon": -0.13, "lat": 51.51 },
  "weather": [{ "description": "light rain", "icon": "10d" }],
  "main": { "temp": 20.5, "humidity": 60, "pressure": 1012 },
  "wind": { "speed": 4.6 },
  "dt": 1628167200,
  "name": "London"
}
💡 Contribution Guidelines
Pull requests are welcome! If you have suggestions for improvements—UI enhancements, better forecast layout, caching, or other APIs—feel free to open a PR.
