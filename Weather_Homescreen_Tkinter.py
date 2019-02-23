#!/usr/bin/python3
# -*- coding: utf8 -*-
try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    from Tkinter import *
from PIL import Image, ImageTk
from requests import get
from pyowm import OWM
from io import BytesIO
from functools import partial
from datetime import datetime
import time
from math import cos, sin, tan, pi, atan
from calendar import monthrange


global gui_color
global city_id
city_id = 5007804
location_label_name = "Royal Oak"

def set_city(info):
    global city_id
    global city_name
    global location_label_name
    if (location_label_name) != city_name.title():
        print("AY")
    city_id = int(info['id'])
    city_name = info['name']

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class Settings(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        settings_font = "Times"
        header_size = 35
        text_imput = StringVar()
        text_imput.set("City Name")
        def callback():
            city_name = text_imput.get()
            isfound = False
            with open('/Users/ethanburt/Desktop/Coding/Weather_Python/New_ids.txt', 'rt') as city_list:
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



        header_frame = Frame(self, background = '#00f3c3')
        header_frame.pack(fill='x', side= "top")

        header_label = Label(header_frame, text="Settings", fg = "#222222", bg="#00f3c3", font=(settings_font, header_size), pady=10)
        header_label.pack(fill="both", expand=True)

        left_search_frame = Frame(self, background = '#222222')
        left_search_frame.pack(fill="both", expand=False, side='left')

        search_frame_label = Label(left_search_frame, background = '#222222', font=(settings_font, header_size - 5 ), text="Change City", fg='#00f3c3')
        search_frame_label.pack(fill='x', expand=False, side="top")

        search_box = Entry(left_search_frame, textvariable=text_imput, font= (settings_font, 15 ))
        search_box.pack(fill="x", expand=False, side='top')

        search_button = Button(left_search_frame, background = '#222222', font=(settings_font, header_size - 10 ), text="Search", command=callback)
        search_button.pack(fill="x", expand=False, side='top')

        color_pick_frame = Frame(self, background = '#222222')
        color_pick_frame.pack(fill="both", expand=True, side='right')

        city_info_frame = Frame(left_search_frame, background = '#222222')
        city_info_frame.pack(fill="both", expand=False, side='left')

class Home(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        '''
       colors:
       #ffffff
       #00b092
       #333333
       #222222
        '''
        global city_name
        city_name = "Royal Oak"
        home_frame_width, home_frame_height = 800, 385
        hbutton_width = 10
        hbutton_height = 6
        hbuttom_paddingx = 35
        hbutton_paddingy = 30
        roak_weather_id = 5007804
        annarbor_weather_id = 4984247

        API_key_real = '4b89aea78dd85e4582f86b23bc670e98'
        genral_font = "Times"
        # Dashboard Text Sizes
        weekday_size = 35
        month_size = 17
        time_size = 90
        location_size = 40
        weather_size = 24
        tempature_size = 77

        # weather Forecast Text Sizes
        weather_title_size = 17
        weather_date_size = 10
        weather_report_size = 12

        # Dashboard Colors
        primary_text_color = '#ffffff'
        secondary_text_color = '#00b092'

        # Weather Forecast colors
        weather_forecast_background = "#ffffff"
        weather_text_color = '#333333'

        # Size of Image
        image_multiple = 110

        weekday = time.strftime('%A')
        date = str(time.strftime('%B')) + " " + \
            str(time.strftime('%-d')) + "th, " + str(time.strftime('%Y'))


        def check():
            if location_label.cget('text') != city_name.title():
                location_label.config(text=city_name.title())
                day0_info = local_weather(weather_id=city_id, api_key=API_key_real)
                day1_info = day_info(API_key_real,city_id, 1)
                day2_info = day_info(API_key_real,city_id, 2)
                day3_info = day_info(API_key_real,city_id, 3)
                day4_info = day_info(API_key_real,city_id, 4)
                day5_info = day_info(API_key_real,city_id, 5)
                weather_label.config(text=day0_info.DetailedStatus())
                if 1 == 1:

                    img = Image.open(BytesIO((get(day0_info.FindPath())).content))

                    wpercent = (image_multiple / float(img.size[0]))
                    hsize = int((float(img1.size[1]) * float(wpercent)))
                    img = img.resize((image_multiple, hsize), Image.ANTIALIAS)

                    img = ImageTk.PhotoImage(img)
                    panel = Label(image_Frame, image=img, background="#00f3c3")
                    panel.image = img
                temp_label.config(text=(str(day0_info.TempInF()) + "°F"))

                day1_label.config(text=day1_info.WeekdayName())
                day2_label.config(text=day2_info.WeekdayName())
                day3_label.config(text=day3_info.WeekdayName())
                day4_label.config(text=day4_info.WeekdayName())
                day5_label.config(text=day5_info.WeekdayName())

                day1_abrv_date_label.config(text=day1_info.AbrivatedDate())
                day2_abrv_date_label.config(text=day2_info.AbrivatedDate())
                day3_abrv_date_label.config(text=day3_info.AbrivatedDate())
                day4_abrv_date_label.config(text=day4_info.AbrivatedDate())
                day5_abrv_date_label.config(text=day5_info.AbrivatedDate())


                img = ImageTk.PhotoImage(Image.open(BytesIO((get(day1_info.Path())).content)))
                day1_icon.config(image=img)
                day1_icon.image = img

                img = ImageTk.PhotoImage(Image.open(BytesIO((get(day2_info.Path())).content)))
                day2_icon.config(image=img)
                day2_icon.image = img

                img = ImageTk.PhotoImage(Image.open(BytesIO((get(day3_info.Path())).content)))
                day3_icon.config(image=img)
                day3_icon.image = img

                img = ImageTk.PhotoImage(Image.open(BytesIO((get(day4_info.Path())).content)))
                day4_icon.config(image=img)
                day4_icon.image = img

                img = ImageTk.PhotoImage(Image.open(BytesIO((get(day5_info.Path())).content)))
                day5_icon.config(image=img)
                day5_icon.image = img

                print(day0_info.DetailedStatus())

                day1_forecast.config(text=day1_info.Forecast().title())
                day2_forecast.config(text=day2_info.Forecast().title())
                day3_forecast.config(text=day3_info.Forecast().title())
                day4_forecast.config(text=day4_info.Forecast().title())
                day5_forecast.config(text=day5_info.Forecast().title())

                global location_label_name
                location_label_name = str(city_id).title()
            location_label.after(1000, check)

        def tick():
            time1 = ''
            time2 = str(int(time.strftime('%I'))) + ":" + time.strftime('%M')
            if time2 != time1:
                time1 = time2
                time_label.config(text=time2)
            time_label.after(1000, tick)



        class weather_in_area():
            def __init__(self, api_key, weather_id):
                self.weather_id = weather_id
                self.f1 =  OWM(api_key)
                self.new = (self.f1).weather_at_id(self.weather_id)
                self.f2 = (self.f1).three_hours_forecast_at_id(self.weather_id)


            def three_hours_forecast(self):
                return(f1.three_hours_forecast_at_id(self.weather_id))


        # Forecast Banner Information Function
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
                path = 'http://openweathermap.org/img/w/01d.png'
                date_string = (str(self.this_year) + '-' + str(self.this_month) + '-' + str(self.updated_day) + ' ' + '12:00:00+00')
                forecast=(self.f2).get_weather_at(date_string)
                simplified_weather=(forecast.get_status()).lower()
                weather_icons={"clear": '01d', "few clouds": '02d', "scattered clouds": '03d', "broken clouds": '04d',
                    "shower rain": '05d', "rain": '10d', "thunderstorm": '11d', "snow": '13d', "mist": '50d', "clouds": '03d'}
                for status, code in weather_icons.items():
                    if simplified_weather == status:
                        path = "http://openweathermap.org/img/w/" + code + ".png"
                return(path)


        # Info about Location
        class local_weather(weather_in_area):
            pass


            def TempInF(self):
                fahrenheit = ((self.new).get_weather()).get_temperature('fahrenheit')
                return(int(fahrenheit['temp']))

            def DetailedStatus(self):
                detailed = (self.new).get_weather()
                status_d = ((detailed).get_detailed_status()).title()
                return(status_d)

            def SimpleStatus(self):
                simple = (self.new).get_weather()
                status_s = (simple).get_status()
                return(status_s)

            def FindPath(self):
                path = "http://openweathermap.org/img/w/01d.png"
                simple = (self.new).get_weather()
                status_s = ((simple).get_status()).lower()
                weather_icons={"clear": '01d', "few clouds": '02d', "scattered clouds": '03d', "broken clouds": '04d',
                    "shower rain": '05d', "rain": '10d', "thunderstorm": '11d', "snow": '13d', "mist": '50d', "clouds": '03d'}
                for status, code in weather_icons.items():
                    if status_s == status:
                        path = "http://openweathermap.org/img/w/" + code + ".png"
                return(path)


        day0_info = local_weather(weather_id=city_id, api_key=API_key_real)
        day1_info = day_info(API_key_real,city_id, 1)
        day2_info = day_info(API_key_real,city_id, 2)
        day3_info = day_info(API_key_real,city_id, 3)
        day4_info = day_info(API_key_real,city_id, 4)
        day5_info = day_info(API_key_real,city_id, 5)


        # 222222

        # Home Frame
        home_frame = Frame(self, background="#00f3c3",
                           width=home_frame_width, height=home_frame_height)
        home_frame.pack(side="top", fill="both", expand=True)

        # Header Frame
        header_frame = Frame(home_frame, background="#00f3c3")
        header_frame.pack(side="top", fill='both')

        header_left_frame = Frame(header_frame, background="#00f3c3",
                                  width=home_frame_width / 2, height=home_frame_height)
        header_left_frame.pack(side="left", fill="both", expand=True)

        header_right_frame = Frame(
            header_frame, background="#00f3c3", width=home_frame_width / 2, height=home_frame_height)
        header_right_frame.pack(side="left", fill="both", expand=True)

        # Day of the Week
        weekday_frame = Frame(header_left_frame, background="#00f3c3")
        weekday_frame.grid(row=1, column=0, columnspan=1)

        weekday_label = Label(weekday_frame, background="#00f3c3", text=str(
            weekday), font=(genral_font, weekday_size), fg=secondary_text_color, pady=10)
        weekday_label.pack(side="left", fill="x", expand=True)

        # Date Ex) Feburary 11, 2019
        month_frame = Frame(header_left_frame, background="#00f3c3")
        month_frame.grid(row=2, column=0, columnspan=1)

        month_label = Label(month_frame, background="#00f3c3", text=date, font=(
            genral_font, month_size), fg=secondary_text_color)
        month_label.pack(side="left", fill="both", expand=True)

        # Time
        time_frame = Frame(header_left_frame, background="#00f3c3")
        time_frame.grid(row=4, column=0, rowspan=2, columnspan=2)

        time_label = Label(time_frame, background="#00f3c3", font=(
            genral_font, time_size), fg=primary_text_color, padx=30)
        time_label.pack(side="left", fill="both", expand=True)

        # Location
        location_frame = Frame(header_right_frame, background="#00f3c3")
        location_frame.grid(row=1, column=0, columnspan=1)

        location_label = Label(location_frame, background="#00f3c3", text="Royal Oak", font=(
            genral_font, location_size), fg=secondary_text_color, pady=5)
        location_label.pack(side="left", fill="x", expand=True)

        # Current detailed weather
        weather_frame = Frame(header_right_frame, background="#00f3c3")
        weather_frame.grid(row=2, column=0)

        weather_label = Label(weather_frame, background="#00f3c3", text=(day0_info.DetailedStatus()), font=(genral_font, weather_size), fg=secondary_text_color)
        weather_label.pack(side="left", fill="both", expand=True)

        fake_weather_label = Label(weather_frame, background="#00f3c3", text="____", font=(
            genral_font, weather_size), fg="#00f3c3")
        fake_weather_label.pack(side="left", fill="both", expand=True)

        # Icon for weather
        image_Frame = Frame(header_right_frame)
        image_Frame.grid(row=3, column=0, rowspan=2)

        response = get(day0_info.FindPath())
        img1 = Image.open(BytesIO(response.content))

        wpercent = (image_multiple / float(img1.size[0]))
        hsize = int((float(img1.size[1]) * float(wpercent)))
        img1 = img1.resize((image_multiple, hsize), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(img1)
        panel = Label(image_Frame, image=img, background="#00f3c3")
        panel.image = img
        panel.pack()

        # Tempature at location
        temp_frame = Frame(header_right_frame, background="#00f3c3")
        temp_frame.grid(row=3, column=1, rowspan=2)

        temp_label = Label(temp_frame, background="#00f3c3", text=(str(day0_info.TempInF())) + "°F", font=(genral_font, tempature_size), fg=primary_text_color)
        temp_label.pack(side="left", fill="both", expand=True)

        # Lower Forecast Frame
        weather_frame = Frame(home_frame, background="white")
        weather_frame.pack(side="bottom", fill="both")

        # Day 1 Forecast
        day1_frame = Frame(weather_frame, bg=weather_forecast_background)
        day1_frame.pack(side="left", expand=True)

        # Day of the week
        day1_label = Label(day1_frame, bg=weather_forecast_background, text=day1_info.WeekdayName(), font=(
            genral_font, weather_title_size), fg=weather_text_color, pady=5)
        day1_label.grid(row=0, column=0)

        # Abrivated Date
        day1_abrv_date_label = Label(day1_frame, bg=weather_forecast_background, text=day1_info.AbrivatedDate(), font=(
            genral_font, weather_date_size), fg=weather_text_color)
        day1_abrv_date_label.grid(row=1, column=0)

        # Icon for weather
        response = get(day1_info.Path())
        img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        day1_icon = Label(day1_frame, image=img,
                          bg=weather_forecast_background)
        day1_icon.image = img
        day1_icon.grid(row=2, column=0)

        # Detailed weather report
        day1_forecast = Label(day1_frame, bg=weather_forecast_background, text=day1_info.Forecast().title(
        ), font=(genral_font, weather_report_size), fg=weather_text_color)
        day1_forecast.grid(row=3, column=0)

        # Day 2 Forecast
        day2_frame = Frame(weather_frame, bg=weather_forecast_background)
        day2_frame.pack(side="left", expand=True)

        # Day of the week
        day2_label = Label(day2_frame, bg=weather_forecast_background, text=day2_info.WeekdayName(), font=(
            genral_font, weather_title_size), fg=weather_text_color, pady=5)
        day2_label.grid(row=0, column=0)

        # Abrivated Date
        day2_abrv_date_label = Label(day2_frame, bg=weather_forecast_background, text=day2_info.AbrivatedDate(), font=(
            genral_font, weather_date_size), fg=weather_text_color)
        day2_abrv_date_label.grid(row=1, column=0)

        # Icon for weather
        response = get(day2_info.Path())
        img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        day2_icon = Label(day2_frame, image=img,
                          bg=weather_forecast_background)
        day2_icon.image = img
        day2_icon.grid(row=2, column=0)

        day2_forecast = Label(day2_frame, bg=weather_forecast_background, text=day2_info.Forecast().title(
        ), font=(genral_font, weather_report_size), fg=weather_text_color)
        day2_forecast.grid(row=3, column=0)

        # Day 3 Forecast
        day3_frame = Frame(weather_frame, bg=weather_forecast_background)
        day3_frame.pack(side="left", expand=True)

        # Day of the Week
        day3_label = Label(day3_frame, bg=weather_forecast_background, text=day3_info.WeekdayName(), font=(
            genral_font, weather_title_size), fg=weather_text_color, pady=5)
        day3_label.grid(row=0, column=0)

        # Abrivated Date
        day3_abrv_date_label = Label(day3_frame, bg=weather_forecast_background, text=day3_info.AbrivatedDate(), font=(
            genral_font, weather_date_size), fg=weather_text_color)
        day3_abrv_date_label.grid(row=1, column=0)

        # Icon for weather
        response = get(day3_info.Path())
        img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        day3_icon = Label(day3_frame, image=img,
                          bg=weather_forecast_background)
        day3_icon.image = img
        day3_icon.grid(row=2, column=0)

        # Detailed weather report
        day3_forecast = Label(day3_frame, bg=weather_forecast_background, text=day3_info.Forecast().title(
        ), font=(genral_font, weather_report_size), fg=weather_text_color)
        day3_forecast.grid(row=3, column=0)

        # Day 4 Forecast
        day4_frame = Frame(weather_frame, bg=weather_forecast_background)
        day4_frame.pack(side="left", expand=True)

        # Day of the week
        day4_label = Label(day4_frame, bg=weather_forecast_background, text=day4_info.WeekdayName(), font=(
            genral_font, weather_title_size), fg=weather_text_color, pady=5)
        day4_label.grid(row=0, column=0)

        # Abrivated Date
        day4_abrv_date_label = Label(day4_frame, bg=weather_forecast_background, text=day4_info.AbrivatedDate(), font=(
            genral_font, weather_date_size), fg=weather_text_color)
        day4_abrv_date_label.grid(row=1, column=0)

        # Icon for weather
        response = get(day4_info.Path())
        img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        day4_icon = Label(day4_frame, image=img,
                          bg=weather_forecast_background)
        day4_icon.image = img
        day4_icon.grid(row=2, column=0)

        # Detailed weather report
        day4_forecast = Label(day4_frame, bg=weather_forecast_background, text=day4_info.Forecast().title(
        ), font=(genral_font, weather_report_size), fg=weather_text_color)
        day4_forecast.grid(row=3, column=0)

        # Day 5 Forecast
        day5_frame = Frame(weather_frame, bg=weather_forecast_background)
        day5_frame.pack(side="left", expand=True)

        # Day of the week
        day5_label = Label(day5_frame, bg=weather_forecast_background, text=day5_info.WeekdayName(), font=(
            genral_font, weather_title_size), fg=weather_text_color, pady=5)
        day5_label.grid(row=0, column=0)

        # Abrivated Date
        day5_abrv_date_label = Label(day5_frame, bg=weather_forecast_background, text=day5_info.AbrivatedDate(), font=(
            genral_font, weather_date_size), fg=weather_text_color)
        day5_abrv_date_label.grid(row=1, column=0)

        # Icon for weather
        response = get(day5_info.Path())
        img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        day5_icon = Label(day5_frame, image=img,
                          bg=weather_forecast_background)
        day5_icon.image = img
        day5_icon.grid(row=2, column=0)

        # Detailed weather report
        day5_forecast = Label(day5_frame, bg=weather_forecast_background, text=day5_info.Forecast().title(
        ), font=(genral_font, weather_report_size), fg=weather_text_color)
        day5_forecast.grid(row=3, column=0)

        tick()
        check()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        def show_settings(event):
            if settings_label.cget('bg') == "#00b092":
                p1.lift()
                settings_label.config(bg="#222222")
                settings_frame.config(bg="#222222")
            else:
                p2.lift()
                settings_label.config(bg="#00b092")
                settings_frame.config(bg="#00b092")

        p1 = Home(self)
        p2 = Settings(self)



        buttonframe = tk.Frame(self, bg="#222222")
        container = tk.Frame(self, bg="#222222")
        buttonframe.pack(side="bottom", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        settings_image_size = 25
        response = get('https://images.onlinelabels.com/images/clip-art/tobiasluko/Settings%20Button-234562.png')
        settings = Image.open(BytesIO(response.content))

        wpercent = (settings_image_size / float(settings.size[0]))
        hsize = int((float(settings.size[1]) * float(wpercent)))
        settings = settings.resize((settings_image_size, hsize), Image.ANTIALIAS)

        settings = ImageTk.PhotoImage(settings)


        settings_frame = Frame(buttonframe, bg="#222222")
        settings_frame.pack(side="right", fill="none", expand=False)

        settings_label = Label(settings_frame, image=settings, padx=6, pady=6, bg="#222222")
        settings_label.image = settings
        settings_label.bind("<Button-1>", show_settings)
        settings_label.pack(side="right", fill="none", expand=False)



        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Control Center")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x435")
    root.mainloop()
# 572x372


# Dashboard Image) https://www.google.com/search?biw=867&bih=645&tbm=isch&sa=1&ei=sOxhXLO1MpL2tAXkzKfwBQ&q=dashboard+icons+transparent+white&oq=dashboard+icons+transparent+white&gs_l=img.3...203067.208129..208373...0.0..0.178.1665.14j2......1....1..gws-wiz-img.DhZNdd3-fvY#imgdii=fP0n7g4yhDrQGM:&imgrc=M9DcngcD3Ps1tM:
# Light Image) https://previews.123rf.com/images/asmati/asmati1706/asmati170605854/80929914-light-lamp-sign-vector-white-icon-with-soft-shadow-on-transparent-background-.jpg
