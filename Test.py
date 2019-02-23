try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    from Tkinter import *

from PIL import Image, ImageTk
from webcolors import hex_to_rgb, rgb_to_hex
from requests import get
from pyowm import OWM
from io import BytesIO
from functools import partial
from datetime import datetime
import time
from math import cos, sin, tan, pi, atan
from calendar import monthrange
import json
from functools import partial




root = Tk()
root.wm_geometry("800x435")


settings_font = "Times"
header_size = 35
global country_live
text_imput = StringVar()
text_imput.set("Royal Oak")

def set_city(info):
    print(info)

def callback():
    city_name = text_imput.get()
    isfound = False
    with open('/Users/ethanburt/Desktop/Coding/Weather_Python/city.list.json', 'rt') as city_list:
        previous_line = ''
        for line in city_list: #For each line of text store in a string variable named "line"
            if str(city_name) in str(line):
                isfound = True
            else:
                if isfound:
                    country_line = line
                    break
                previous_line = str(line)

        id = ' '
        country = ' '
        num = 0
        for letter in previous_line:
            num += 1
            if 10 < num < 18:
                id = str(id) + str(letter)
        num = 0
        for letter in country_line:
            num += 1
            if 16 < num < 19:
                country = str(country) + str(letter)

        if (id):
                new_city_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text="New City Name: " + city_name, fg='#00f3c3')
                new_city_name.grid(row=0, column=0)

                country_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text="Country: " + country, fg='#00f3c3')
                country_name.grid(row=1, column=0)

                information = partial(set_city, {'id':id,'name':city_name})

                set_city_button = Button(city_info_frame, font=(settings_font, 15 ), text="Set New City", fg='#222222', command=information)
                set_city_button.grid(row=2, column=0)



    print(id)



header_frame = Frame(root, background = '#00f3c3')
header_frame.pack(fill='x', side= "top")

header_label = Label(header_frame, text="Settings", fg = "#222222", bg="#00f3c3", font=(settings_font, header_size), pady=10)
header_label.pack(fill="both", expand=True)

left_search_frame = Frame(root, background = '#222222')
left_search_frame.pack(fill="both", expand=False, side='left')

search_frame_label = Label(left_search_frame, background = '#222222', font=(settings_font, header_size - 5 ), text="Change City", fg='#00f3c3')
search_frame_label.pack(fill='x', expand=False, side="top")

search_box = Entry(left_search_frame, textvariable=text_imput, font= (settings_font, 15 ))
search_box.pack(fill="x", expand=False, side='top')

search_button = Button(left_search_frame, background = '#222222', font=(settings_font, header_size - 10 ), text="Search", command=callback)
search_button.pack(fill="x", expand=False, side='top')

color_pick_frame = Frame(root, background = '#222222')
color_pick_frame.pack(fill="both", expand=True, side='right')

city_info_frame = Frame(left_search_frame, background = '#222222')
city_info_frame.pack(fill="both", expand=False, side='left')




root.mainloop()















def get_city_id(city_name):
    with open('/Users/ethanburt/Desktop/Coding/Weather_Python/city.list.json', 'rt') as city_list:
        previous_line = ''
        for line in city_list: #For each line of text store in a string variable named "line"
            if str(city_name) in str(line):
                break
            else:
                previous_line = str(line)
        id = ' '
        num = 0
        for letter in previous_line:
            num += 1
            if 10 < num < 18:
                id = str(id) + str(letter)
    return(id)

print(get_city_id("Royal Oak"))





        #print(list)

'''json_data = json.loads(data_string)
for city in json_data['city']:
if city['name'] == city_name:
return city['_id']'''






































































'''
roak_weather_id = 5007804
annarbor_weather_id = 4984247

API_key = '4b89aea78dd85e4582f86b23bc670e98'
''' '''
f1 = OWM(API_key)
global f2
global local2
f2 = f1.three_hours_forecast_at_id(roak_weather_id)
local2 = f1.weather_at_id(roak_weather_id)''''''


class weather_in_area():
    def __init__(self, api_key, weather_id):
        self.weather_id = weather_id
        self.f1 =  OWM(api_key)
        self.new = (self.f1).weather_at_id(self.weather_id)
        self.f2 = (self.f1).three_hours_forecast_at_id(self.weather_id)


    def three_hours_forecast(self):
        return(f1.three_hours_forecast_at_id(self.weather_id))




class day_info(weather_in_area):
    def __init__(self, api_key, weather_id, days_later):
        pass
        super().__init__(api_key, weather_id)
        self.days_later = days_later
        self.this_year = time.strftime('%Y')
        self.this_month = time.strftime('%m')
        self.this_day = time.strftime('%d')
        self.updated_day = int(self.this_day) + int(self.days_later)


    def WeekdayName(self):
        this_week = time.strftime('%w')
        num_list_day = (int(this_week) - 1 + self.days_later)
        days_o_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                           "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday"]
        return((days_o_the_week[num_list_day]).title())

    def AbrivatedDate(self):
        abrv_date = str(int(time.strftime('%m'))) + "/" + str(self.updated_day) + "/" + str(self.this_year)
        return(abrv_date)

    def Forecast(self):
        # String for getting forecast
        # Ex)'2019-02-12 17:00:00+00'
        days_in_month = monthrange(int(self.this_year), int(self.this_month) )
        if (int(self.this_day) + int(self.days_later) > days_in_month[1]):
            self.this_month += 1
            self.updated_day = ((self.this_day + self.days_later) - 31)

        date_string = (str(self.this_year) + '-' + str(self.this_month) + '-' + str(self.updated_day) + ' ' + '12:00:00+00')
        # Getting weather info

        forecast=(self.f2).get_weather_at(date_string)
        # Detailed status for label
        weather_forecast=forecast.get_detailed_status()
        return(weather_forecast.title())

    def Path(self):
        date_string = (str(self.this_year) + '-' + str(self.this_month) + '-' + str(self.updated_day) + ' ' + '12:00:00+00')
        forecast=(self.f2).get_weather_at(date_string)
        simplified_weather=(forecast.get_status()).lower()
        weather_icons={"clear": '01d', "few clouds": '02d', "scattered clouds": '03d', "broken clouds": '04d',
            "shower rain": '05d', "rain": '10d', "thunderstorm": '11d', "snow": '13d', "mist": '50d', "clouds": '03d'}
        for status, code in weather_icons.items():
            if simplified_weather == status:
                path = "http://openweathermap.org/img/w/" + code + ".png"
                print(code)
        if not(path): path = "http://openweathermap.org/img/w/01d.png"
        return(path)

example = day_info(API_key, roak_weather_id, 2)
x = example.weekday_name()
print(x)



class local_weather(weather_in_area):
    pass

    def TempInF(self):
        fahrenheit = (self.new).get_weather()
        return(fahrenheit.get_temperature('fahrenheit'))

    def DetailedStatus(self):
        detailed = (self.new).get_weather()
        status_d = ((detailed).get_detailed_status()).title()
        return(status_d)

    def SimpleStatus(self):
        simple = (self.new).get_weather()
        status_s = (simple).get_status()
        return(status_s)

    def FindPath(self):
        simple = (self.new).get_weather()
        status_s = ((simple).get_status()).lower()
        print(status_s)
        weather_icons={"clear": '01d', "few clouds": '02d', "scattered clouds": '03d', "broken clouds": '04d',
            "shower rain": '05d', "rain": '10d', "thunderstorm": '11d', "snow": '13d', "mist": '50d', "clouds": '03d'}
        for status, code in weather_icons.items():
            if status_s == status:
                path = "http://openweathermap.org/img/w/" + code + ".png"
                print(code)
        if not(path): path = "http://openweathermap.org/img/w/01d.png"
        return(path)



#Not sure if inheritance is setup correctly with the passing thing
#check to make sure its all kosher





def local_weather_stats():
    if pause_weather:
        local_info = {'tempature': {'temp': "32"}, 'detailed': 'real cold',
                      'simple': "cold", 'path': "http://openweathermap.org/img/w/01d.png"}
    else:
        # Recieving weather Information
        local3 = local2.get_weather()
        #Tempature in Fahrenheit
        temp_in_F = local3.get_temperature('fahrenheit')
        # Local Detailed Status
        status_D = (local3.get_detailed_status()).title()
        # Local Simple Status
        status_S = local3.get_status().lower()
        # Icon for weather
        if (status_S == "clear sky"):
            icon_id = '01d'
        elif (status_S == "few clouds"):
            icon_id = '02d'
        elif (status_S == "scattered clouds"):
            icon_id = '03d'
        elif (status_S == "broken clouds"):
            icon_id = '04d'
        elif (status_S == "shower rain"):
            icon_id = '05d'
        elif (status_S == "rain"):
            icon_id = '10d'
        elif (status_S == "thunderstorm"):
            icon_id = '11d'
        elif (status_S == "snow"):
            icon_id = '13d'
        elif (status_S == "mist"):
            icon_id = '50d'
        else:
            icon_id = '01d'
        path = "http://openweathermap.org/img/w/" + icon_id + ".png"

        local_info = {'tempature': temp_in_F, 'detailed': status_D,
                      'simple': status_S.title(), 'path': path}
    return(local_info)




























'''






















































class day_info():

    # Get weather Information for any given day
    def __init__(self, days_later):
        self.days_later = days_later

    def weekday_name(self):
        this_week = time.strftime('%w')
        num_list_day = (int(this_week) - 1 + self.days_later)
        days_o_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                           "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday"]
        return((days_o_the_week[num_list_day]).title())

    def abrivated_date(self):
        updated_day = int(time.strftime('%d')) + int(self.days_later)
        abrv_date = str(int(time.strftime('%m'))) + "/" + \
                        str(updated_day)
        return(abrv_date)

    def forecast(self):
        this_year = time.strftime('%Y')
        this_month = time.strftime('%m')
        this_day = time.strftime('%d')
        # String for getting forecast
        # Ex)'2019-02-12 17:00:00+00'
        days_in_month = monthrange(int(this_year), int(this_month) )
        if (int(this_day) + int(self.days_later) > days_in_month[1]):
            this_month += 1
            updated_day = ((this_day + self.days_later) - 31)
        else: updated_day = int(this_day) + int(self.days_later)

        date_string = (str(this_year) + '-' + str(this_month) + '-' + str(updated_day) + ' ' + '12:00:00+00')
        # Getting weather info
        forecast=f2.get_weather_at(date_string)
        # Detailed status for label
        weather_forecast=forecast.get_detailed_status()
        return(weather_forecast.title())

    def path(self):
        simplified_weather=(forecast.get_status()).lower()
        weather_icons={"clear": '01d', "few clouds": '02d', "scattered clouds": '03d', "broken clouds": '04d',
            "shower rain": '05d', "rain": '10d', "thunderstorm": '11d', "snow": '13d', "mist": '50d', "clouds": '03d'}
        for status, code in weather_icons.items():
            if simplified_weather == status:
                path = "http://openweathermap.org/img/w/" + icon + ".png"
            else:
                path = "http://openweathermap.org/img/w/01d.png"
        return(path)




day1_info = day_info(1)
day2_info = day_info(2)
day3_info = day_info(3)
day4_info = day_info(4)
day5_info = day_info(5)

#print(day1_info.forecast())

'''


# Forecast Banner Information Function
def get_day_info(days_later):

    if pause_weather:
        day_info = {'weekday_name': "Tuesday", "abrivated_full_date": '2/15/2019',
                    "forecast": "real cold", 'icon_path': "http://openweathermap.org/img/w/01d.png"}
    else:
        # Number of Day of the week in the list
        # weekday_name
        def weekday_name(days_later):
            num_list_day = (int(time.strftime('%w')) - 1 + days_later)
            days_o_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                               "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday"]
            return(days_o_the_week[num_list_day])


        this_year= str(time.strftime('%Y'))
        this_month= str(time.strftime('%m'))
        this_day= int(time.strftime('%d'))

        if (this_day + int(days_later) > 31):
            this_month += 0
            this_day= ((this_day + days_later) - 31)

        updated_day= int(this_day) + int(days_later)

        # 5/12/2001
        abrv_date= str(int(time.strftime('%m'))) + "/" + str(updated_day) + "/" + str(time.strftime('%Y'))

        # String for getting forecast
        # Ex)'2019-02-12 17:00:00+00'
        date_string= str(this_year + '-' + this_month +
                          '-' + str(updated_day) + ' ' + '12:00:00+00')

        # Getting weather info
        forecast = f2.get_weather_at(date_string)

        # Detailed status for label
        weather_forecast = forecast.get_detailed_status()

        # Simple status for icon
        simplified_weather = (forecast.get_status()).lower()

        # Icon for weather
        if (simplified_weather == "clear"):
            icon_id = '01d'
        elif (simplified_weather == "few clouds"):
            icon_id = '02d'
        elif (simplified_weather == "scattered clouds"):
            icon_id = '03d'
        elif (simplified_weather == "broken clouds"):
            icon_id = '04d'
        elif (simplified_weather == "shower rain"):
            icon_id = '05d'
        elif (simplified_weather == "rain"):
            icon_id = '10d'
        elif (simplified_weather == "thunderstorm"):
            icon_id = '11d'
        elif (simplified_weather == "snow"):
            icon_id = '13d'
        elif (simplified_weather == "mist"):
            icon_id = '50d'
        elif (simplified_weather == 'clouds'):
            icon_id = '03d'
        else:
            icon_id = '01d'

        path = "http://openweathermap.org/img/w/" + icon_id + ".png"

        day_info = {'weekday_name': weekday_name(days_later), "abrivated_full_date": abrv_date, "forecast": weather_forecast, 'icon_path': path}
    return(day_info)
def local_weather_stats():
    if pause_weather:
        local_info = {'tempature': {'temp': "32"}, 'detailed': 'real cold',
                      'simple': "cold", 'path': "http://openweathermap.org/img/w/01d.png"}
    else:
        # Recieving weather Information
        local3 = local2.get_weather()
        #Tempature in Fahrenheit
        temp_in_F = local3.get_temperature('fahrenheit')
        # Local Detailed Status
        status_D = (local3.get_detailed_status()).title()
        # Local Simple Status
        status_S = local3.get_status().lower()
        # Icon for weather
        if (status_S == "clear sky"):
            icon_id = '01d'
        elif (status_S == "few clouds"):
            icon_id = '02d'
        elif (status_S == "scattered clouds"):
            icon_id = '03d'
        elif (status_S == "broken clouds"):
            icon_id = '04d'
        elif (status_S == "shower rain"):
            icon_id = '05d'
        elif (status_S == "rain"):
            icon_id = '10d'
        elif (status_S == "thunderstorm"):
            icon_id = '11d'
        elif (status_S == "snow"):
            icon_id = '13d'
        elif (status_S == "mist"):
            icon_id = '50d'
        else:
            icon_id = '01d'
        path = "http://openweathermap.org/img/w/" + icon_id + ".png"

        local_info = {'tempature': temp_in_F, 'detailed': status_D,
                      'simple': status_S.title(), 'path': path}
    return(local_info)
'''
