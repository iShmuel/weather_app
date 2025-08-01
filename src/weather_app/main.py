import os
import streamlit as st
import requests
from dotenv import load_dotenv
from datetime import datetime
import folium
from streamlit_folium import st_folium

load_dotenv()  # load ver from  .env


def get_weather_data(city, weather_api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
    response = requests.get(url)
    return response.json()


def get_weekly_forecast(weather_api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    return response.json()


def display_weekly_forecast(data):
    try:
        st.write("========================================================================================")
        st.write("### Weekly Weather Forecast")
        display_dates = set()  # To keep track of dates for which forecast has been displayed

        # c1, c2, c3, c4 = st.columns(4)
        c1, c2, c3, c4 = st.columns([4, 4, 2, 2])

        with c1:
            st.metric("", "Day")
        with c2:
            st.metric("", "Description")
        with c3:
            st.metric("", "Min_temp")
        with c4:
            st.metric("", "Max_temp")

        for day in data['list']:

            date = datetime.fromtimestamp(day['dt']).strftime('%A, %B, %d')
            # Check if the date has already been displayed
            if date not in display_dates:
                display_dates.add(date)

                min_temp = day['main']['temp_min']
                max_temp = day['main']['temp_max']
                description = day['weather'][0]['description'].capitalize()

                with c1:
                    st.metric(label="Date", value=date)
                with c2:
                    st.metric(label="Description", value=description.capitalize())
                with c3:
                    st.metric(label="Min Temp", value=f"{min_temp:.1f}°C")
                with c4:
                    st.metric(label="Max Temp", value=f"{max_temp:.1f}°C")

    except Exception as e:
        st.error("Error in Displaying weekly forecast: " + str(e))


def main():
    # sidebar configuration
    st.sidebar.title("Weather Forecasting")
    city = st.sidebar.text_input("Enter city name")

    # API key
    # weather_api_key = os.getenv("WEATHER_API")
    weather_api_key = st.secrets["weather"]["api_key"]

    # Button to fetch and display weather data
    submit = st.sidebar.button("Get Weather")

    if submit:
        st.title("Weather Updates for " + city + "is:")
        with st.spinner("Fetching weather data..."):
            weather_data = get_weather_data(city, weather_api_key)
            print(weather_data)

            # Check if the city is found and display weather data
            if weather_data.get("cod") != 404:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Temperature ", f"{weather_data['main']['temp']:.2f} *C")
                with col2:
                    st.metric("Pressure ", f"{weather_data['main']['pressure']} hPa")
                with col3:
                    st.metric("Humidity ", f"{weather_data['main']['humidity']}%")
                with col4:
                    st.metric("Wind Speed ", f"{weather_data['wind']['speed']}m/s")

                lat = weather_data['coord']['lat']
                lon = weather_data['coord']['lon']
                icon_code = weather_data['weather'][0]['icon']
                # Call function to get weekly forecast
                forecast_data = get_weekly_forecast(weather_api_key, lat, lon)

                print(forecast_data)
                if forecast_data.get("cod") != "404":
                    display_weekly_forecast(forecast_data)

                else:
                    st.error("Error fetching weekly forecast data")

            else:
                # Display an error message if the city is not found
                st.error("City not found or an error occurred!")


if __name__ == "__main__":
    main()
