import requests
import datetime as dt
import smtplib
import time

my_lat = 51.507351
my_lng = -0.127758
my_mail= "verze1220@gmail.com"
password ="lzrm izfz qxwd fiqk"

def location_true():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # will give u all the https codes n matter which prblm u went into

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if my_lat -5.0<=latitude<=my_lat+5.0 and my_lng -5.0<=longitude<=my_lng+5.0:
        return True
    else:
        return False

def is_night():
    parameters ={
        "lat":my_lat,
        "lng":my_lat,
        "formatted":0,
    }
    response = requests.get(url =  "https://api.sunrise-sunset.org/json",params = parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    now = dt.datetime.now()
    print(now.hour)

    if now.hour >= sunset or now.hour <= sunrise:
        return True
    else:
       return False

while True:
    time.sleep(5)
    if location_true() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs="verze1220@yahoo.com",
                                msg=f"Subject:STARGAZIING!!\n\nHey! see what ISS is above you")
        print("Success")
























