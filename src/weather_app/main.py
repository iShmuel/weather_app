import  streamlit as st
import  requests



def main():
    #sidebar configuration
    st.sidebar.title("Weather Forecasting")
    city = st.sidebar.text_input("Enter city name")

    #API key
    weather_api_key = "" #put the actual one

    #Button to fetch and display weather data
    submit = st.sidebar.button("Get Weather")


if __name__ == "__main__":
    main()
