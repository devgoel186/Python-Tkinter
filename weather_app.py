from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO
import json
import config

root = Tk()
root.title("Weather App")

Label(root, text="Enter City Name : ").grid(row=0, column=0)
city = Entry(root, width=20, bg="#e3d3c2", borderwidth=4,
             cursor="dot", font="family=Helvetica")
city.grid(row=0, column=1)

Label(root, text="Enter State Name : ").grid(row=1, column=0)
state = Entry(root, width=20, bg="#e3d3c2", borderwidth=4,
              cursor="dot", font="family=Helvetica")
state.grid(row=1, column=1)

Label(root, text="Enter Country Name : ").grid(row=2, column=0)
country = Entry(root, width=20, bg="#e3d3c2", borderwidth=4,
                cursor="dot", font="family=Helvetica")
country.grid(row=2, column=1)
data_frame = LabelFrame(root, text="Current Weather",
                        borderwidth=4, font="family=Helvetica")
img_frame = LabelFrame(root, text="Weather Icon",
                       borderwidth=4, font="family=Helvetica")

data_frame.grid(row=3, column=0, columnspan=2)
img_frame.grid(row=4, column=0, columnspan=2)


def getImage(api):
    # Get image based on weather code
    response = requests.get("http://openweathermap.org/img/wn/" +
                            str(api["data"]["current"]["weather"]["ic"]) + "@2x.png")
    img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
    return img


def getData():
    global img, img_frame, data_frame
    img_frame.destroy()
    data_frame.destroy()

    # Build and pack frames
    data_frame = LabelFrame(root, text="Current Weather",
                            borderwidth=4, font="family=Helvetica")
    img_frame = LabelFrame(root, text="Weather Icon",
                           borderwidth=4, font="family=Helvetica")
    data_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
    img_frame.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

    api_request = requests.get(
        "http://api.airvisual.com/v2/city?city=" + city.get() + "&state=" + state.get() + "&country=" + country.get() + "&key=" + config.api_key)
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    # Get Image from Weather Codes API
    img = getImage(api)

    Label(data_frame, text="CITY : " + api["data"]["city"] +
          "\nSTATE : " + api["data"]["state"] +
          "\nCOUNTRY : " + api["data"]["country"] +
          "\nTEMPERATURE (in " + u"\N{DEGREE SIGN}" + "C) : " +
          str(api["data"]["current"]["weather"]["tp"]) +
          "\nATMOSPHERIC PRESSURE (in hPa) : " +
          str(api["data"]["current"]["weather"]["pr"]) +
          "\nHUMIDITY : " +
          str(api["data"]["current"]["weather"]["hu"]) +
          "\nWIND SPEED (in m/s) : " +
          str(api["data"]["current"]["weather"]["ws"]) +
          "\nWIND DIRECTION : " +
          str(api["data"]["current"]["weather"]["wd"]) + u"\N{DEGREE SIGN}", anchor=W).pack()
    Label(img_frame, text="WEATHER ICON CODE : " +
          str(api["data"]["current"]["weather"]["ic"])).pack()
    Label(img_frame, image=img).pack()


Button(root, text="Get Data", width=20,
       relief="groove", command=getData).grid(row=3, column=0, columnspan=2, pady=20)

mainloop()
