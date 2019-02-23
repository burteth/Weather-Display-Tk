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

self = Frame(root)
self.pack(expand=True, fill='both')

settings_font = "Times"
header_size = 35
text_imput = StringVar()
text_imput.set("City Name")
def callback():
    country_dict = {'AF': 'Afghanistan', 'AX': 'Åland Islands', 'AL': 'Albania', 'DZ': 'Algeria', 'AS': 'American Samoa', 'AD': 'Andorra', 'AO': 'Angola', 'AI': 'Anguilla', 'AQ': 'Antarctica', 'AG': 'Antigua and Barbuda', 'AR': 'Argentina', 'AM': 'Armenia', 'AW': 'Aruba', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbaijan', 'BS': 'Bahamas', 'BH': 'Bahrain', 'BD': 'Bangladesh', 'BB': 'Barbados', 'BY': 'Belarus', 'BE': 'Belgium', 'BZ': 'Belize', 'BJ': 'Benin', 'BM': 'Bermuda', 'BT': 'Bhutan', 'BO': 'Bolivia, Plurinational State of', 'BQ': 'Bonaire, Sint Eustatius and Saba', 'BA': 'Bosnia and Herzegovina', 'BW': 'Botswana', 'BV': 'Bouvet Island', 'BR': 'Brazil', 'IO': 'British Indian Ocean Territory', 'BN': 'Brunei Darussalam', 'BG': 'Bulgaria', 'BF': 'Burkina Faso', 'BI': 'Burundi', 'KH': 'Cambodia', 'CM': 'Cameroon', 'CA': 'Canada', 'CV': 'Cape Verde', 'KY': 'Cayman Islands', 'CF': 'Central African Republic', 'TD': 'Chad', 'CL': 'Chile', 'CN': 'China', 'CX': 'Christmas Island', 'CC': 'Cocos (Keeling) Islands', 'CO': 'Colombia', 'KM': 'Comoros', 'CG': 'Congo', 'CD': 'Congo, the Democratic Republic of the', 'CK': 'Cook Islands', 'CR': 'Costa Rica', 'CI': "Côte d'Ivoire", 'HR': 'Croatia', 'CU': 'Cuba', 'CW': 'Curaçao', 'CY': 'Cyprus', 'CZ': 'Czech Republic', 'DK': 'Denmark', 'DJ': 'Djibouti', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'EC': 'Ecuador', 'EG': 'Egypt', 'SV': 'El Salvador', 'GQ': 'Equatorial Guinea', 'ER': 'Eritrea', 'EE': 'Estonia', 'ET': 'Ethiopia', 'FK': 'Falkland Islands (Malvinas)', 'FO': 'Faroe Islands', 'FJ': 'Fiji', 'FI': 'Finland', 'FR': 'France', 'GF': 'French Guiana', 'PF': 'French Polynesia', 'TF': 'French Southern Territories', 'GA': 'Gabon', 'GM': 'Gambia', 'GE': 'Georgia', 'DE': 'Germany', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GR': 'Greece', 'GL': 'Greenland', 'GD': 'Grenada', 'GP': 'Guadeloupe', 'GU': 'Guam', 'GT': 'Guatemala', 'GG': 'Guernsey', 'GN': 'Guinea', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HT': 'Haiti', 'HM': 'Heard Island and McDonald Islands', 'VA': 'Holy See (Vatican City State)', 'HN': 'Honduras', 'HK': 'Hong Kong', 'HU': 'Hungary', 'IS': 'Iceland', 'IN': 'India', 'ID': 'Indonesia', 'IR': 'Iran, Islamic Republic of', 'IQ': 'Iraq', 'IE': 'Ireland', 'IM': 'Isle of Man', 'IL': 'Israel', 'IT': 'Italy', 'JM': 'Jamaica', 'JP': 'Japan', 'JE': 'Jersey', 'JO': 'Jordan', 'KZ': 'Kazakhstan', 'KE': 'Kenya', 'KI': 'Kiribati', 'KP': "Korea, Democratic People's Republic of", 'KR': 'Korea, Republic of', 'KW': 'Kuwait', 'KG': 'Kyrgyzstan', 'LA': "Lao People's Democratic Republic", 'LV': 'Latvia', 'LB': 'Lebanon', 'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'LI': 'Liechtenstein', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'MO': 'Macao', 'MK': 'Macedonia, the Former Yugoslav Republic of', 'MG': 'Madagascar', 'MW': 'Malawi', 'MY': 'Malaysia', 'MV': 'Maldives', 'ML': 'Mali', 'MT': 'Malta', 'MH': 'Marshall Islands', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MU': 'Mauritius', 'YT': 'Mayotte', 'MX': 'Mexico', 'FM': 'Micronesia, Federated States of', 'MD': 'Moldova, Republic of', 'MC': 'Monaco', 'MN': 'Mongolia', 'ME': 'Montenegro', 'MS': 'Montserrat', 'MA': 'Morocco', 'MZ': 'Mozambique', 'MM': 'Myanmar', 'NA': 'Namibia', 'NR': 'Nauru', 'NP': 'Nepal', 'NL': 'Netherlands', 'NC': 'New Caledonia', 'NZ': 'New Zealand', 'NI': 'Nicaragua', 'NE': 'Niger', 'NG': 'Nigeria', 'NU': 'Niue', 'NF': 'Norfolk Island', 'MP': 'Northern Mariana Islands', 'NO': 'Norway', 'OM': 'Oman', 'PK': 'Pakistan', 'PW': 'Palau', 'PS': 'Palestine, State of', 'PA': 'Panama', 'PG': 'Papua New Guinea', 'PY': 'Paraguay', 'PE': 'Peru', 'PH': 'Philippines', 'PN': 'Pitcairn', 'PL': 'Poland', 'PT': 'Portugal', 'PR': 'Puerto Rico', 'QA': 'Qatar', 'RE': 'Réunion', 'RO': 'Romania', 'RU': 'Russian Federation', 'RW': 'Rwanda', 'BL': 'Saint Barthélemy', 'SH': 'Saint Helena, Ascension and Tristan da Cunha', 'KN': 'Saint Kitts and Nevis', 'LC': 'Saint Lucia', 'MF': 'Saint Martin (French part)', 'PM': 'Saint Pierre and Miquelon', 'VC': 'Saint Vincent and the Grenadines', 'WS': 'Samoa', 'SM': 'San Marino', 'ST': 'Sao Tome and Principe', 'SA': 'Saudi Arabia', 'SN': 'Senegal', 'RS': 'Serbia', 'SC': 'Seychelles', 'SL': 'Sierra Leone', 'SG': 'Singapore', 'SX': 'Sint Maarten (Dutch part)', 'SK': 'Slovakia', 'SI': 'Slovenia', 'SB': 'Solomon Islands', 'SO': 'Somalia', 'ZA': 'South Africa', 'GS': 'South Georgia and the South Sandwich Islands', 'SS': 'South Sudan', 'ES': 'Spain', 'LK': 'Sri Lanka', 'SD': 'Sudan', 'SR': 'Suriname', 'SJ': 'Svalbard and Jan Mayen', 'SZ': 'Swaziland', 'SE': 'Sweden', 'CH': 'Switzerland', 'SY': 'Syrian Arab Republic', 'TW': 'Taiwan, Province of China', 'TJ': 'Tajikistan', 'TZ': 'Tanzania, United Republic of', 'TH': 'Thailand', 'TL': 'Timor-Leste', 'TG': 'Togo', 'TK': 'Tokelau', 'TO': 'Tonga', 'TT': 'Trinidad and Tobago', 'TN': 'Tunisia', 'TR': 'Turkey', 'TM': 'Turkmenistan', 'TC': 'Turks and Caicos Islands', 'TV': 'Tuvalu', 'UG': 'Uganda', 'UA': 'Ukraine', 'AE': 'United Arab Emirates', 'GB': 'United Kingdom', 'US': 'United States', 'UM': 'United States Minor Outlying Islands', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VU': 'Vanuatu', 'VE': 'Venezuela, Bolivarian Republic of', 'VN': 'Viet Nam', 'VG': 'Virgin Islands, British', 'VI': 'Virgin Islands, U.S.', 'WF': 'Wallis and Futuna', 'EH': 'Western Sahara', 'YE': 'Yemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}
    cities = []
    city_name = text_imput.get()
    with open('/Users/ethanburt/Desktop/Coding/Weather_Python/weather-display/Weather_IDs.txt', 'rt') as city_list:
        for line in city_list:
            local_city_id = ''
            city_country = ''
            city_full_name = ''
            city_full_name_2 = ''
            num = 0
            if str(city_name) in str(line):
                for letter in line:
                    if (num < 8) & (letter != ',') & (letter != ' '):
                        local_city_id = str(local_city_id) + str(letter)
                    elif (7 < num < 10):
                        city_country = str(city_country) + str(letter)
                    elif (num > 10) & (letter != ','):
                        city_full_name = str(city_full_name) + str(letter)
                    num += 1
                city_full_name_2 = city_full_name[1:-1]
                city_full_name_2 = city_full_name_2.replace('"', '')
                country_name = country_dict[city_country]
                cities.append([city_full_name_2, country_name, local_city_id])
                print(cities)


        if (cities != []):
                for i in range(len(cities)):
                    new_city_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text=str(cities[0][0]), fg='#00f3c3')
                    new_city_name.grid(row=0, column=0)



                new_city_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text=str(cities[0][0]), fg='#00f3c3')
                new_city_name.grid(row=0, column=0)

                country_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text=country_name, fg='#00f3c3')
                country_name.grid(row=1, column=0)

                #information = partial(set_city, {'id':local_city_id,'name':city_full_name_2})
                def information():
                    print("global value thing")

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






root.mainloop()


































'''
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
'''

'''
def callback(city_name):
    country_dict = {'AF': 'Afghanistan', 'AX': 'Åland Islands', 'AL': 'Albania', 'DZ': 'Algeria', 'AS': 'American Samoa', 'AD': 'Andorra', 'AO': 'Angola', 'AI': 'Anguilla', 'AQ': 'Antarctica', 'AG': 'Antigua and Barbuda', 'AR': 'Argentina', 'AM': 'Armenia', 'AW': 'Aruba', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbaijan', 'BS': 'Bahamas', 'BH': 'Bahrain', 'BD': 'Bangladesh', 'BB': 'Barbados', 'BY': 'Belarus', 'BE': 'Belgium', 'BZ': 'Belize', 'BJ': 'Benin', 'BM': 'Bermuda', 'BT': 'Bhutan', 'BO': 'Bolivia, Plurinational State of', 'BQ': 'Bonaire, Sint Eustatius and Saba', 'BA': 'Bosnia and Herzegovina', 'BW': 'Botswana', 'BV': 'Bouvet Island', 'BR': 'Brazil', 'IO': 'British Indian Ocean Territory', 'BN': 'Brunei Darussalam', 'BG': 'Bulgaria', 'BF': 'Burkina Faso', 'BI': 'Burundi', 'KH': 'Cambodia', 'CM': 'Cameroon', 'CA': 'Canada', 'CV': 'Cape Verde', 'KY': 'Cayman Islands', 'CF': 'Central African Republic', 'TD': 'Chad', 'CL': 'Chile', 'CN': 'China', 'CX': 'Christmas Island', 'CC': 'Cocos (Keeling) Islands', 'CO': 'Colombia', 'KM': 'Comoros', 'CG': 'Congo', 'CD': 'Congo, the Democratic Republic of the', 'CK': 'Cook Islands', 'CR': 'Costa Rica', 'CI': "Côte d'Ivoire", 'HR': 'Croatia', 'CU': 'Cuba', 'CW': 'Curaçao', 'CY': 'Cyprus', 'CZ': 'Czech Republic', 'DK': 'Denmark', 'DJ': 'Djibouti', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'EC': 'Ecuador', 'EG': 'Egypt', 'SV': 'El Salvador', 'GQ': 'Equatorial Guinea', 'ER': 'Eritrea', 'EE': 'Estonia', 'ET': 'Ethiopia', 'FK': 'Falkland Islands (Malvinas)', 'FO': 'Faroe Islands', 'FJ': 'Fiji', 'FI': 'Finland', 'FR': 'France', 'GF': 'French Guiana', 'PF': 'French Polynesia', 'TF': 'French Southern Territories', 'GA': 'Gabon', 'GM': 'Gambia', 'GE': 'Georgia', 'DE': 'Germany', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GR': 'Greece', 'GL': 'Greenland', 'GD': 'Grenada', 'GP': 'Guadeloupe', 'GU': 'Guam', 'GT': 'Guatemala', 'GG': 'Guernsey', 'GN': 'Guinea', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HT': 'Haiti', 'HM': 'Heard Island and McDonald Islands', 'VA': 'Holy See (Vatican City State)', 'HN': 'Honduras', 'HK': 'Hong Kong', 'HU': 'Hungary', 'IS': 'Iceland', 'IN': 'India', 'ID': 'Indonesia', 'IR': 'Iran, Islamic Republic of', 'IQ': 'Iraq', 'IE': 'Ireland', 'IM': 'Isle of Man', 'IL': 'Israel', 'IT': 'Italy', 'JM': 'Jamaica', 'JP': 'Japan', 'JE': 'Jersey', 'JO': 'Jordan', 'KZ': 'Kazakhstan', 'KE': 'Kenya', 'KI': 'Kiribati', 'KP': "Korea, Democratic People's Republic of", 'KR': 'Korea, Republic of', 'KW': 'Kuwait', 'KG': 'Kyrgyzstan', 'LA': "Lao People's Democratic Republic", 'LV': 'Latvia', 'LB': 'Lebanon', 'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'LI': 'Liechtenstein', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'MO': 'Macao', 'MK': 'Macedonia, the Former Yugoslav Republic of', 'MG': 'Madagascar', 'MW': 'Malawi', 'MY': 'Malaysia', 'MV': 'Maldives', 'ML': 'Mali', 'MT': 'Malta', 'MH': 'Marshall Islands', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MU': 'Mauritius', 'YT': 'Mayotte', 'MX': 'Mexico', 'FM': 'Micronesia, Federated States of', 'MD': 'Moldova, Republic of', 'MC': 'Monaco', 'MN': 'Mongolia', 'ME': 'Montenegro', 'MS': 'Montserrat', 'MA': 'Morocco', 'MZ': 'Mozambique', 'MM': 'Myanmar', 'NA': 'Namibia', 'NR': 'Nauru', 'NP': 'Nepal', 'NL': 'Netherlands', 'NC': 'New Caledonia', 'NZ': 'New Zealand', 'NI': 'Nicaragua', 'NE': 'Niger', 'NG': 'Nigeria', 'NU': 'Niue', 'NF': 'Norfolk Island', 'MP': 'Northern Mariana Islands', 'NO': 'Norway', 'OM': 'Oman', 'PK': 'Pakistan', 'PW': 'Palau', 'PS': 'Palestine, State of', 'PA': 'Panama', 'PG': 'Papua New Guinea', 'PY': 'Paraguay', 'PE': 'Peru', 'PH': 'Philippines', 'PN': 'Pitcairn', 'PL': 'Poland', 'PT': 'Portugal', 'PR': 'Puerto Rico', 'QA': 'Qatar', 'RE': 'Réunion', 'RO': 'Romania', 'RU': 'Russian Federation', 'RW': 'Rwanda', 'BL': 'Saint Barthélemy', 'SH': 'Saint Helena, Ascension and Tristan da Cunha', 'KN': 'Saint Kitts and Nevis', 'LC': 'Saint Lucia', 'MF': 'Saint Martin (French part)', 'PM': 'Saint Pierre and Miquelon', 'VC': 'Saint Vincent and the Grenadines', 'WS': 'Samoa', 'SM': 'San Marino', 'ST': 'Sao Tome and Principe', 'SA': 'Saudi Arabia', 'SN': 'Senegal', 'RS': 'Serbia', 'SC': 'Seychelles', 'SL': 'Sierra Leone', 'SG': 'Singapore', 'SX': 'Sint Maarten (Dutch part)', 'SK': 'Slovakia', 'SI': 'Slovenia', 'SB': 'Solomon Islands', 'SO': 'Somalia', 'ZA': 'South Africa', 'GS': 'South Georgia and the South Sandwich Islands', 'SS': 'South Sudan', 'ES': 'Spain', 'LK': 'Sri Lanka', 'SD': 'Sudan', 'SR': 'Suriname', 'SJ': 'Svalbard and Jan Mayen', 'SZ': 'Swaziland', 'SE': 'Sweden', 'CH': 'Switzerland', 'SY': 'Syrian Arab Republic', 'TW': 'Taiwan, Province of China', 'TJ': 'Tajikistan', 'TZ': 'Tanzania, United Republic of', 'TH': 'Thailand', 'TL': 'Timor-Leste', 'TG': 'Togo', 'TK': 'Tokelau', 'TO': 'Tonga', 'TT': 'Trinidad and Tobago', 'TN': 'Tunisia', 'TR': 'Turkey', 'TM': 'Turkmenistan', 'TC': 'Turks and Caicos Islands', 'TV': 'Tuvalu', 'UG': 'Uganda', 'UA': 'Ukraine', 'AE': 'United Arab Emirates', 'GB': 'United Kingdom', 'US': 'United States', 'UM': 'United States Minor Outlying Islands', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VU': 'Vanuatu', 'VE': 'Venezuela, Bolivarian Republic of', 'VN': 'Viet Nam', 'VG': 'Virgin Islands, British', 'VI': 'Virgin Islands, U.S.', 'WF': 'Wallis and Futuna', 'EH': 'Western Sahara', 'YE': 'Yemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}
    cities = []
    with open('/Users/ethanburt/Desktop/Coding/Weather_Python/weather-display/Weather_IDs.txt', 'rt') as city_list:
        for line in city_list:
            local_city_id = ''
            city_country = ''
            city_full_name = ''
            city_full_name_2 = ''
            num = 0
            #has_comma = False
            if str(city_name) in str(line):
                for letter in line:
                    if (num < 8) & (letter != ',') & (letter != ' '):
                        local_city_id = str(local_city_id) + str(letter)
                    elif (7 < num < 10):
                        city_country = str(city_country) + str(letter)
                    elif (num > 10) & (letter != ','):
                        city_full_name = str(city_full_name) + str(letter)
                    num += 1
                city_full_name_2 = city_full_name[1:-1]
                city_full_name_2 = city_full_name_2.replace('"', '')
                country_name = country_dict[city_country]
                cities.append([city_full_name_2, country_name, local_city_id])
        print(cities)



callback('Detroit')
'''




'''
        previous_line = ''
        for line in city_list: #For each line of text store in a string variable named "line"
            if str(city_name) in str(line):
                for letter in line:




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








def get_local_city_id(city_name):
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

#print(get_city_id("Royal Oak"))
'''




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



'''
codes = [{"Code": "AF", "Name": "Afghanistan"},{"Code": "AX", "Name": "\u00c5land Islands"},{"Code": "AL", "Name": "Albania"},{"Code": "DZ", "Name": "Algeria"},{"Code": "AS", "Name": "American Samoa"},{"Code": "AD", "Name": "Andorra"},{"Code": "AO", "Name": "Angola"},{"Code": "AI", "Name": "Anguilla"},{"Code": "AQ", "Name": "Antarctica"},{"Code": "AG", "Name": "Antigua and Barbuda"},{"Code": "AR", "Name": "Argentina"},{"Code": "AM", "Name": "Armenia"},{"Code": "AW", "Name": "Aruba"},{"Code": "AU", "Name": "Australia"},{"Code": "AT", "Name": "Austria"},{"Code": "AZ", "Name": "Azerbaijan"},{"Code": "BS", "Name": "Bahamas"},{"Code": "BH", "Name": "Bahrain"},{"Code": "BD", "Name": "Bangladesh"},{"Code": "BB", "Name": "Barbados"},{"Code": "BY", "Name": "Belarus"},{"Code": "BE", "Name": "Belgium"},{"Code": "BZ", "Name": "Belize"},{"Code": "BJ", "Name": "Benin"},{"Code": "BM", "Name": "Bermuda"},{"Code": "BT", "Name": "Bhutan"},{"Code": "BO", "Name": "Bolivia, Plurinational State of"},{"Code": "BQ", "Name": "Bonaire, Sint Eustatius and Saba"},{"Code": "BA", "Name": "Bosnia and Herzegovina"},{"Code": "BW", "Name": "Botswana"},{"Code": "BV", "Name": "Bouvet Island"},{"Code": "BR", "Name": "Brazil"},{"Code": "IO", "Name": "British Indian Ocean Territory"},{"Code": "BN", "Name": "Brunei Darussalam"},{"Code": "BG", "Name": "Bulgaria"},{"Code": "BF", "Name": "Burkina Faso"},{"Code": "BI", "Name": "Burundi"},{"Code": "KH", "Name": "Cambodia"},{"Code": "CM", "Name": "Cameroon"},{"Code": "CA", "Name": "Canada"},{"Code": "CV", "Name": "Cape Verde"},{"Code": "KY", "Name": "Cayman Islands"},{"Code": "CF", "Name": "Central African Republic"},{"Code": "TD", "Name": "Chad"},{"Code": "CL", "Name": "Chile"},{"Code": "CN", "Name": "China"},{"Code": "CX", "Name": "Christmas Island"},{"Code": "CC", "Name": "Cocos (Keeling) Islands"},{"Code": "CO", "Name": "Colombia"},{"Code": "KM", "Name": "Comoros"},{"Code": "CG", "Name": "Congo"},{"Code": "CD", "Name": "Congo, the Democratic Republic of the"},{"Code": "CK", "Name": "Cook Islands"},{"Code": "CR", "Name": "Costa Rica"},{"Code": "CI", "Name": "C\u00f4te d'Ivoire"},{"Code": "HR", "Name": "Croatia"},{"Code": "CU", "Name": "Cuba"},{"Code": "CW", "Name": "Cura\u00e7ao"},{"Code": "CY", "Name": "Cyprus"},{"Code": "CZ", "Name": "Czech Republic"},{"Code": "DK", "Name": "Denmark"},{"Code": "DJ", "Name": "Djibouti"},{"Code": "DM", "Name": "Dominica"},{"Code": "DO", "Name": "Dominican Republic"},{"Code": "EC", "Name": "Ecuador"},{"Code": "EG", "Name": "Egypt"},{"Code": "SV", "Name": "El Salvador"},{"Code": "GQ", "Name": "Equatorial Guinea"},{"Code": "ER", "Name": "Eritrea"},{"Code": "EE", "Name": "Estonia"},{"Code": "ET", "Name": "Ethiopia"},{"Code": "FK", "Name": "Falkland Islands (Malvinas)"},{"Code": "FO", "Name": "Faroe Islands"},{"Code": "FJ", "Name": "Fiji"},{"Code": "FI", "Name": "Finland"},{"Code": "FR", "Name": "France"},{"Code": "GF", "Name": "French Guiana"},{"Code": "PF", "Name": "French Polynesia"},{"Code": "TF", "Name": "French Southern Territories"},{"Code": "GA", "Name": "Gabon"},{"Code": "GM", "Name": "Gambia"},{"Code": "GE", "Name": "Georgia"},{"Code": "DE", "Name": "Germany"},{"Code": "GH", "Name": "Ghana"},{"Code": "GI", "Name": "Gibraltar"},{"Code": "GR", "Name": "Greece"},{"Code": "GL", "Name": "Greenland"},{"Code": "GD", "Name": "Grenada"},{"Code": "GP", "Name": "Guadeloupe"},{"Code": "GU", "Name": "Guam"},{"Code": "GT", "Name": "Guatemala"},{"Code": "GG", "Name": "Guernsey"},{"Code": "GN", "Name": "Guinea"},{"Code": "GW", "Name": "Guinea-Bissau"},{"Code": "GY", "Name": "Guyana"},{"Code": "HT", "Name": "Haiti"},{"Code": "HM", "Name": "Heard Island and McDonald Islands"},{"Code": "VA", "Name": "Holy See (Vatican City State)"},{"Code": "HN", "Name": "Honduras"},{"Code": "HK", "Name": "Hong Kong"},{"Code": "HU", "Name": "Hungary"},{"Code": "IS", "Name": "Iceland"},{"Code": "IN", "Name": "India"},{"Code": "ID", "Name": "Indonesia"},{"Code": "IR", "Name": "Iran, Islamic Republic of"},{"Code": "IQ", "Name": "Iraq"},{"Code": "IE", "Name": "Ireland"},{"Code": "IM", "Name": "Isle of Man"},{"Code": "IL", "Name": "Israel"},{"Code": "IT", "Name": "Italy"},{"Code": "JM", "Name": "Jamaica"},{"Code": "JP", "Name": "Japan"},{"Code": "JE", "Name": "Jersey"},{"Code": "JO", "Name": "Jordan"},{"Code": "KZ", "Name": "Kazakhstan"},{"Code": "KE", "Name": "Kenya"},{"Code": "KI", "Name": "Kiribati"},{"Code": "KP", "Name": "Korea, Democratic People's Republic of"},{"Code": "KR", "Name": "Korea, Republic of"},{"Code": "KW", "Name": "Kuwait"},{"Code": "KG", "Name": "Kyrgyzstan"},{"Code": "LA", "Name": "Lao People's Democratic Republic"},{"Code": "LV", "Name": "Latvia"},{"Code": "LB", "Name": "Lebanon"},{"Code": "LS", "Name": "Lesotho"},{"Code": "LR", "Name": "Liberia"},{"Code": "LY", "Name": "Libya"},{"Code": "LI", "Name": "Liechtenstein"},{"Code": "LT", "Name": "Lithuania"},{"Code": "LU", "Name": "Luxembourg"},{"Code": "MO", "Name": "Macao"},{"Code": "MK", "Name": "Macedonia, the Former Yugoslav Republic of"},{"Code": "MG", "Name": "Madagascar"},{"Code": "MW", "Name": "Malawi"},{"Code": "MY", "Name": "Malaysia"},{"Code": "MV", "Name": "Maldives"},{"Code": "ML", "Name": "Mali"},{"Code": "MT", "Name": "Malta"},{"Code": "MH", "Name": "Marshall Islands"},{"Code": "MQ", "Name": "Martinique"},{"Code": "MR", "Name": "Mauritania"},{"Code": "MU", "Name": "Mauritius"},{"Code": "YT", "Name": "Mayotte"},{"Code": "MX", "Name": "Mexico"},{"Code": "FM", "Name": "Micronesia, Federated States of"},{"Code": "MD", "Name": "Moldova, Republic of"},{"Code": "MC", "Name": "Monaco"},{"Code": "MN", "Name": "Mongolia"},{"Code": "ME", "Name": "Montenegro"},{"Code": "MS", "Name": "Montserrat"},{"Code": "MA", "Name": "Morocco"},{"Code": "MZ", "Name": "Mozambique"},{"Code": "MM", "Name": "Myanmar"},{"Code": "NA", "Name": "Namibia"},{"Code": "NR", "Name": "Nauru"},{"Code": "NP", "Name": "Nepal"},{"Code": "NL", "Name": "Netherlands"},{"Code": "NC", "Name": "New Caledonia"},{"Code": "NZ", "Name": "New Zealand"},{"Code": "NI", "Name": "Nicaragua"},{"Code": "NE", "Name": "Niger"},{"Code": "NG", "Name": "Nigeria"},{"Code": "NU", "Name": "Niue"},{"Code": "NF", "Name": "Norfolk Island"},{"Code": "MP", "Name": "Northern Mariana Islands"},{"Code": "NO", "Name": "Norway"},{"Code": "OM", "Name": "Oman"},{"Code": "PK", "Name": "Pakistan"},{"Code": "PW", "Name": "Palau"},{"Code": "PS", "Name": "Palestine, State of"},{"Code": "PA", "Name": "Panama"},{"Code": "PG", "Name": "Papua New Guinea"},{"Code": "PY", "Name": "Paraguay"},{"Code": "PE", "Name": "Peru"},{"Code": "PH", "Name": "Philippines"},{"Code": "PN", "Name": "Pitcairn"},{"Code": "PL", "Name": "Poland"},{"Code": "PT", "Name": "Portugal"},{"Code": "PR", "Name": "Puerto Rico"},{"Code": "QA", "Name": "Qatar"},{"Code": "RE", "Name": "R\u00e9union"},{"Code": "RO", "Name": "Romania"},{"Code": "RU", "Name": "Russian Federation"},{"Code": "RW", "Name": "Rwanda"},{"Code": "BL", "Name": "Saint Barth\u00e9lemy"},{"Code": "SH", "Name": "Saint Helena, Ascension and Tristan da Cunha"},{"Code": "KN", "Name": "Saint Kitts and Nevis"},{"Code": "LC", "Name": "Saint Lucia"},{"Code": "MF", "Name": "Saint Martin (French part)"},{"Code": "PM", "Name": "Saint Pierre and Miquelon"},{"Code": "VC", "Name": "Saint Vincent and the Grenadines"},{"Code": "WS", "Name": "Samoa"},{"Code": "SM", "Name": "San Marino"},{"Code": "ST", "Name": "Sao Tome and Principe"},{"Code": "SA", "Name": "Saudi Arabia"},{"Code": "SN", "Name": "Senegal"},{"Code": "RS", "Name": "Serbia"},{"Code": "SC", "Name": "Seychelles"},{"Code": "SL", "Name": "Sierra Leone"},{"Code": "SG", "Name": "Singapore"},{"Code": "SX", "Name": "Sint Maarten (Dutch part)"},{"Code": "SK", "Name": "Slovakia"},{"Code": "SI", "Name": "Slovenia"},{"Code": "SB", "Name": "Solomon Islands"},{"Code": "SO", "Name": "Somalia"},{"Code": "ZA", "Name": "South Africa"},{"Code": "GS", "Name": "South Georgia and the South Sandwich Islands"},{"Code": "SS", "Name": "South Sudan"},{"Code": "ES", "Name": "Spain"},{"Code": "LK", "Name": "Sri Lanka"},{"Code": "SD", "Name": "Sudan"},{"Code": "SR", "Name": "Suriname"},{"Code": "SJ", "Name": "Svalbard and Jan Mayen"},{"Code": "SZ", "Name": "Swaziland"},{"Code": "SE", "Name": "Sweden"},{"Code": "CH", "Name": "Switzerland"},{"Code": "SY", "Name": "Syrian Arab Republic"},{"Code": "TW", "Name": "Taiwan, Province of China"},{"Code": "TJ", "Name": "Tajikistan"},{"Code": "TZ", "Name": "Tanzania, United Republic of"},{"Code": "TH", "Name": "Thailand"},{"Code": "TL", "Name": "Timor-Leste"},{"Code": "TG", "Name": "Togo"},{"Code": "TK", "Name": "Tokelau"},{"Code": "TO", "Name": "Tonga"},{"Code": "TT", "Name": "Trinidad and Tobago"},{"Code": "TN", "Name": "Tunisia"},{"Code": "TR", "Name": "Turkey"},{"Code": "TM", "Name": "Turkmenistan"},{"Code": "TC", "Name": "Turks and Caicos Islands"},{"Code": "TV", "Name": "Tuvalu"},{"Code": "UG", "Name": "Uganda"},{"Code": "UA", "Name": "Ukraine"},{"Code": "AE", "Name": "United Arab Emirates"},{"Code": "GB", "Name": "United Kingdom"},{"Code": "US", "Name": "United States"},{"Code": "UM", "Name": "United States Minor Outlying Islands"},{"Code": "UY", "Name": "Uruguay"},{"Code": "UZ", "Name": "Uzbekistan"},{"Code": "VU", "Name": "Vanuatu"},{"Code": "VE", "Name": "Venezuela, Bolivarian Republic of"},{"Code": "VN", "Name": "Viet Nam"},{"Code": "VG", "Name": "Virgin Islands, British"},{"Code": "VI", "Name": "Virgin Islands, U.S."},{"Code": "WF", "Name": "Wallis and Futuna"},{"Code": "EH", "Name": "Western Sahara"},{"Code": "YE", "Name": "Yemen"},{"Code": "ZM", "Name": "Zambia"},{"Code": "ZW", "Name": "Zimbabwe"}]
new_dict = {}
for i in range(len(codes)):
    dict = codes[i]
    code = str(dict['Code'])
    name = str(dict['Name'])
    new_dict[code] = name
print(new_dict)
'''








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
