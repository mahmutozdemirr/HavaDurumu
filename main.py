import requests

api_key = "6c77d822e64df800e49e46f1b30a1c57"
city = input("Lütfen Şehir Adını Giriniz: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = round(data["main"]["temp"] -273)
    desc = data["weather"][0]["description"]
    print(f"Temperature: {temp} C")
    print(f"description: {desc}")
else:
    print("Hava Durumu Verileri Alınırken Hata Oluştu!")
