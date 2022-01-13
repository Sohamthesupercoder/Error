from tkinter import *
root=Tk()
root.title("My Weather App")
root.geometry("350x300")
root.overrideredirect(True)



import requests
import json

#Setting labels
city_name_label=Label(root, text="City Name",font=("Helvetica", 18,'bold'),bg="white")
city_name_label.place(relx=0.6,rely=0.15,anchor=CENTER)

city_entry = Entry(root , fg = "Black")
city_entry.place(relx=0.6,rely=0.35,anchor=CENTER)

weather_info_label = Label(root,text="Weather: ", bg="white", font=("bold", 18))
weather_info_label.place(relx=0.3,rely=0.6,anchor=CENTER) 

humidity_info_label = Label(root,text="Humidity: ", bg="white", font=( "bold",18)) 
humidity_info_label.place(relx=0.3,rely=0.7,anchor=CENTER) 

def cityname():
    city_name = "    "
    api_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=21cab08deb7b27f4c2b55f3e2df28ea4")
    json_data = json.loads(api_data.content)
    
    
    weather_info = json_data["weather"][0]["main"]
    print(weather_info)
    weather_info_label["text"] ="Weather : " +  str(weather_info)
    
    humidity_info = json_data["main"]["humidity"]
    print(humidity_info)
    humidity_info_label["text"] = "Humidity : " + str(humidity_info) + "%"
    
    city_entry.destroy()
    button.destroy()


root.configure(background="white")

  
button = Button(root , command = cityname , text = "Get Weather" , font = ("bold",18))
button.place(relx = 0.5 , rely = 0.85) 
root.mainloop()
