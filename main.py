import ssl

# Specify the TLS version explicitly
ssl_context = ssl.create_default_context()
ssl_context.options |= ssl.OP_NO_TLSv1
ssl_context.options |= ssl.OP_NO_TLSv1_1

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
import requests

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data.")
        return None


def get_weather_for_date(weather_data, date):
    for entry in weather_data["list"]:
        if date in entry["dt_txt"]:
            return entry["main"]["temp"]
    return None


def get_wind_speed_for_date(weather_data, date):
    for entry in weather_data["list"]:
        if date in entry["dt_txt"]:
            return entry["wind"]["speed"]
    return None


def get_pressure_for_date(weather_data, date):
    for entry in weather_data["list"]:
        if date in entry["dt_txt"]:
            return entry["main"]["pressure"]
    return None


def main():
    weather_data = get_weather_data()
    if not weather_data:
        return

    while True:
        print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program.")
            break

        date = input("Enter the date in format 'YYYY-MM-DD HH:MM:SS': ")

        if choice == "1":
            temperature = get_weather_for_date(weather_data, date)
            if temperature is not None:
                print(f"The temperature on {date} is {temperature:.2f}°C")
            else:
                print("Data not available for the specified date.")

        elif choice == "2":
            wind_speed = get_wind_speed_for_date(weather_data, date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed:.2f} m/s")
            else:
                print("Data not available for the specified date.")

        elif choice == "3":
            pressure = get_pressure_for_date(weather_data, date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure:.2f} hPa")
            else:
                print("Data not available for the specified date.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
