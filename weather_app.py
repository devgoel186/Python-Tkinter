from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import config

root = Tk()
root.title("Weather App")
root.geometry("200x400")


city = Entry(root, width=20)
city.pack()


def getData():
    global city
    api_request = requests.get(
        "http://api.airvisual.com/v2/city?city=" + city.get() + "&state=Uttar%20Pradesh&country=India&key=" + config.api_key)
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    Label(root, text="City : " + api["data"]["city"] + "\nState : " + api["data"]["state"] +
          "\nCountry : " + api["data"]["country"] + "\nCurrent Weather : " + str(api["data"]["current"])).pack()


Button(root, text="Get Data", command=getData).pack()


# Label(root, text="City : " + api["data"]["city"] + "\nState : " +
#       api["data"]["state"] + "\nCountry : " + api["data"]["country"] + "\nCurrent Weather : " + str(api["data"]["current"])).pack()

mainloop()
