import requests

def get_weather_data(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'
city = 'London'  # Replace with the city you want to get weather data for

weather_data = get_weather_data(api_key, city)
if weather_data:
    temperature = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']
    
    print(f"Current weather in {city}: {temperature}°C, {condition}")
