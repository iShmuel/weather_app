import os
import streamlit as st
import requests
import openai
from dotenv import load_dotenv

load_dotenv()  # טוען את כל המשתנים מקובץ .env


def get_weather_data(city, weather_api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
    response = requests.get(url)
    return response.json()


def generate_weather_description(data, openai_api_key):
    openai.api_key = openai_api_key

    try:
        # Convert temperature from Kelvin to Celsius
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        prompt = f"The current weather in your city is {description} with temperature of {temperature:.1f}*c. Explain this in a simple way for a general audience. "

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=60
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)


def main():
    # sidebar configuration
    st.sidebar.title("Weather Forecasting")
    city = st.sidebar.text_input("Enter city name")

    # API key
    weather_api_key = os.getenv("WEATHER_API")
    openai_api_key = os.getenv("OPENAI_API")

    # url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
    # response= requests.get(url)

    # Button to fetch and display weather data
    submit = st.sidebar.button("Get Weather")

    if submit:
        st.title("Weather Updates for " + city + "is:")
        with st.spinner("Fetching weather data..."):
            weather_data = get_weather_data(city, weather_api_key)
            print(weather_data)


if __name__ == "__main__":
    main()
