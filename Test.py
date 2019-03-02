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

self = Frame(root, background = '#222222')
self.pack(expand=True, fill='both')

spectrum_size_width, spectrum_size_height = 300, 300  # Size of the Spectrum Canvas
length_away_factor = 2.1  # How far away from the center the oval is
length_away = spectrum_size_width / length_away_factor
line_width = 5  # Width of the 1530 lines on the spectrum
oval_size = 15
h = length_away * .6  # How far away the oval is when clicking on a color button
global color_combination  # List of all 1530 color on the spectrum
mid_oval_size = 20  # Size of the middle oval

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
                #print(cities)


        if (cities != []):
            for widget in city_info_frame.winfo_children():
                widget.destroy()

            global city_num
            city_num = 0

            def information():
                print("global value thing")

            def move_left(event):
                global city_num
                city_num -= 1
                change_label(city_num)

            def move_right(event):
                global city_num
                city_num += 1
                change_label(city_num)

            range_label = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text="1 of " + str(len(cities)), fg='#00f3c3')
            range_label.pack(fill='y', side="top")


            left_arrow_image = Image.open(BytesIO((get('https://cdn3.iconfinder.com/data/icons/line/36/arrow_left-512.png')).content))
            wpercent = (30 / float(left_arrow_image.size[0]))
            hsize = int((float(left_arrow_image.size[1]) * float(wpercent)))
            left_arrow_image = left_arrow_image.resize((30, hsize), Image.ANTIALIAS)
            left_arrow_image = ImageTk.PhotoImage(left_arrow_image)
            left_arrow_label = Label(city_info_frame, image=left_arrow_image, background="#00f3c3")
            left_arrow_label.bind("<Button-1>", move_left)
            left_arrow_label.image = left_arrow_image
            left_arrow_label.pack(side='left', expand=False)


            detailed_city_info_frame = Frame(city_info_frame, background = '#222222')
            detailed_city_info_frame.pack(side='left', fill='y', pady=40)

            new_city_name = Label(detailed_city_info_frame, background = '#222222', font=(settings_font, 15 ), text=str(cities[0][0]), fg='#00f3c3', width = 25)
            new_city_name.pack(fill='x', padx=10)

            country_name = Label(detailed_city_info_frame, background = '#222222', font=(settings_font, 15 ), text=str(cities[0][1]), fg='#00f3c3')
            country_name.pack(fill='x', padx=10)

            set_city_button = Button(detailed_city_info_frame, font=(settings_font, 15 ), text="Get Weather", fg='#222222', command=information)
            set_city_button.pack(fill='x', padx=10)


            right_arrow_image = Image.open(BytesIO((get('https://cdn3.iconfinder.com/data/icons/line/36/arrow_right-512.png')).content))
            wpercent = (30 / float(right_arrow_image.size[0]))
            hsize = int((float(right_arrow_image.size[1]) * float(wpercent)))
            right_arrow_image = right_arrow_image.resize((30, hsize), Image.ANTIALIAS)

            #shift_right = partial(move_right, city_num)

            right_arrow_image = ImageTk.PhotoImage(right_arrow_image)
            right_arrow_label = Label(city_info_frame, image=right_arrow_image, background="#00f3c3")
            right_arrow_label.bind("<Button-1>", move_right)
            right_arrow_label.image = right_arrow_image
            right_arrow_label.pack(side='left', expand=False)



            def change_label(i):
                new_city_name.config(text=str(cities[i][0]))
                country_name.config(text=str(cities[i][1]))
                #set_city_button.config(text=("Set " + str(cities[i][0])))
                range_label.config(text=(str(i + 1) + " of " + str(len(cities))))


header_frame = Frame(self, background = '#00f3c3')
header_frame.pack(fill='x', side= "top")

header_label = Label(header_frame, text="Settings", fg = "#222222", bg="#00f3c3", font=(settings_font, header_size), pady=10)
header_label.pack(fill="both", expand=True)

left_search_frame = Frame(self, background = '#222222')
left_search_frame.pack(fill="both", expand=False, side='left', padx=35, pady=10)

search_frame_label = Label(left_search_frame, background = '#222222', font=(settings_font, header_size - 5 ), text="Change City", fg='#00f3c3', width = 20)
search_frame_label.pack(fill='x', expand=False, side="top", pady=10)

search_box = Entry(left_search_frame, textvariable=text_imput, font= (settings_font, 15 ))
search_box.pack(fill="x", expand=False, side='top', pady=5)

search_button = Button(left_search_frame, background = '#222222', font=(settings_font, header_size - 10 ), text="Search", command=callback)
search_button.pack(fill="x", expand=False, side='top')

city_info_frame = Frame(left_search_frame, background = '#222222')
city_info_frame.pack(fill="both", expand=False, side='left')

color_pick_frame = Frame(self, background = '#222222')
color_pick_frame.pack(fill="both", expand=True, side='right')


color_header_label = Label(color_pick_frame, background = '#222222', font=(settings_font, header_size - 5 ), fg='#00f3c3', width = 20, text="Change Background Colors")
color_header_label.pack(fill='x', expand=False, side="top", pady=10)

def print_it(event):
    spectrum.delete("first")
    spectrum.delete("oval")
    spectrum.delete("mid_oval")
    x_cord = event.x
    y_cord = event.y
    real_x = int(x_cord) - (spectrum_size_width / 2)
    real_y = int(y_cord) - (spectrum_size_height / 2)
    if (real_x != 0) & (real_y != 0):
        if real_x > 0:
            if real_y > 0:
                theta = atan(real_y / real_x)
            else:
                theta = atan(real_x / abs(real_y)
                             ) + (3 * pi / 2)
        elif (real_x < 0):
            theta = atan(real_y / real_x) + pi

        new_radians = (theta) * (1 / (pi * 2)) * (1530)
        color = color_combination_dict[str(int(new_radians))]
        color_picked = '#%02x%02x%02x' % (color[0], color[1], color[2])
        spectrum.create_oval(int(x_cord) - oval_size, int(y_cord) - oval_size, int(
            x_cord) + oval_size, int(y_cord) + oval_size, fill=color_picked, tags=("oval"))
        spectrum.create_oval((spectrum_size_width / 2) - mid_oval_size, (spectrum_size_width / 2) - mid_oval_size,
                             (spectrum_size_width / 2) + mid_oval_size, (spectrum_size_width / 2) + mid_oval_size, outline="", fill=color_picked, tags="mid_oval")

def draw():
    for i in range(1530):
        global color_combination_dict
        color_combination_draw = color_combination_dict[str(i)]
        new_color = rgb_to_hex((color_combination_draw[0], color_combination_draw[1], color_combination_draw[2]))
        radians_draw = (i / 1530) * (pi) * 2
        x_draw = cos(radians_draw) * length_away + \
            (spectrum_size_width / 2)
        y_draw = sin(radians_draw) * length_away + \
            (spectrum_size_height / 2)
        spectrum.create_line((spectrum_size_width / 2), (spectrum_size_width / 2),
                             x_draw, y_draw, fill=new_color, width=line_width)
    spectrum.bind("<B1-Motion>", print_it)
    spectrum.bind("<Button-1>", print_it)
    spectrum.create_oval((spectrum_size_width / 2) - mid_oval_size, (spectrum_size_width / 2) - mid_oval_size,
                         (spectrum_size_width / 2) + mid_oval_size, (spectrum_size_width / 2) + mid_oval_size, outline="", fill="white")
    spectrum.create_oval((spectrum_size_width / 2) - mid_oval_size, (spectrum_size_width / 2) - mid_oval_size,
                         (spectrum_size_width / 2) + mid_oval_size, (spectrum_size_width / 2) + mid_oval_size, outline="", fill="white", tags=("first"))

# Spectrum Canvas
spectrum = Canvas(color_pick_frame, width=(spectrum_size_width),
                  height=spectrum_size_height, highlightthickness=0, relief='ridge', background="#222222")
spectrum.pack(expand=True, side="top", padx=10)

global color_combination_dict
color_combination_dict = {'0': (255, 0, 0),
                          '1': (255, 1, 0),
                          '2': (255, 2, 0),
                          '3': (255, 3, 0),
                          '4': (255, 4, 0),
                          '5': (255, 5, 0),
                          '6': (255, 6, 0),
                          '7': (255, 7, 0),
                          '8': (255, 8, 0),
                          '9': (255, 9, 0),
                          '10': (255, 10, 0),
                          '11': (255, 11, 0),
                          '12': (255, 12, 0),
                          '13': (255, 13, 0),
                          '14': (255, 14, 0),
                          '15': (255, 15, 0),
                          '16': (255, 16, 0),
                          '17': (255, 17, 0),
                          '18': (255, 18, 0),
                          '19': (255, 19, 0),
                          '20': (255, 20, 0),
                          '21': (255, 21, 0),
                          '22': (255, 22, 0),
                          '23': (255, 23, 0),
                          '24': (255, 24, 0),
                          '25': (255, 25, 0),
                          '26': (255, 26, 0),
                          '27': (255, 27, 0),
                          '28': (255, 28, 0),
                          '29': (255, 29, 0),
                          '30': (255, 30, 0),
                          '31': (255, 31, 0),
                          '32': (255, 32, 0),
                          '33': (255, 33, 0),
                          '34': (255, 34, 0),
                          '35': (255, 35, 0),
                          '36': (255, 36, 0),
                          '37': (255, 37, 0),
                          '38': (255, 38, 0),
                          '39': (255, 39, 0),
                          '40': (255, 40, 0),
                          '41': (255, 41, 0),
                          '42': (255, 42, 0),
                          '43': (255, 43, 0),
                          '44': (255, 44, 0),
                          '45': (255, 45, 0),
                          '46': (255, 46, 0),
                          '47': (255, 47, 0),
                          '48': (255, 48, 0),
                          '49': (255, 49, 0),
                          '50': (255, 50, 0),
                          '51': (255, 51, 0),
                          '52': (255, 52, 0),
                          '53': (255, 53, 0),
                          '54': (255, 54, 0),
                          '55': (255, 55, 0),
                          '56': (255, 56, 0),
                          '57': (255, 57, 0),
                          '58': (255, 58, 0),
                          '59': (255, 59, 0),
                          '60': (255, 60, 0),
                          '61': (255, 61, 0),
                          '62': (255, 62, 0),
                          '63': (255, 63, 0),
                          '64': (255, 64, 0),
                          '65': (255, 65, 0),
                          '66': (255, 66, 0),
                          '67': (255, 67, 0),
                          '68': (255, 68, 0),
                          '69': (255, 69, 0),
                          '70': (255, 70, 0),
                          '71': (255, 71, 0),
                          '72': (255, 72, 0),
                          '73': (255, 73, 0),
                          '74': (255, 74, 0),
                          '75': (255, 75, 0),
                          '76': (255, 76, 0),
                          '77': (255, 77, 0),
                          '78': (255, 78, 0),
                          '79': (255, 79, 0),
                          '80': (255, 80, 0),
                          '81': (255, 81, 0),
                          '82': (255, 82, 0),
                          '83': (255, 83, 0),
                          '84': (255, 84, 0),
                          '85': (255, 85, 0),
                          '86': (255, 86, 0),
                          '87': (255, 87, 0),
                          '88': (255, 88, 0),
                          '89': (255, 89, 0),
                          '90': (255, 90, 0),
                          '91': (255, 91, 0),
                          '92': (255, 92, 0),
                          '93': (255, 93, 0),
                          '94': (255, 94, 0),
                          '95': (255, 95, 0),
                          '96': (255, 96, 0),
                          '97': (255, 97, 0),
                          '98': (255, 98, 0),
                          '99': (255, 99, 0),
                          '100': (255, 100, 0),
                          '101': (255, 101, 0),
                          '102': (255, 102, 0),
                          '103': (255, 103, 0),
                          '104': (255, 104, 0),
                          '105': (255, 105, 0),
                          '106': (255, 106, 0),
                          '107': (255, 107, 0),
                          '108': (255, 108, 0),
                          '109': (255, 109, 0),
                          '110': (255, 110, 0),
                          '111': (255, 111, 0),
                          '112': (255, 112, 0),
                          '113': (255, 113, 0),
                          '114': (255, 114, 0),
                          '115': (255, 115, 0),
                          '116': (255, 116, 0),
                          '117': (255, 117, 0),
                          '118': (255, 118, 0),
                          '119': (255, 119, 0),
                          '120': (255, 120, 0),
                          '121': (255, 121, 0),
                          '122': (255, 122, 0),
                          '123': (255, 123, 0),
                          '124': (255, 124, 0),
                          '125': (255, 125, 0),
                          '126': (255, 126, 0),
                          '127': (255, 127, 0),
                          '128': (255, 128, 0),
                          '129': (255, 129, 0),
                          '130': (255, 130, 0),
                          '131': (255, 131, 0),
                          '132': (255, 132, 0),
                          '133': (255, 133, 0),
                          '134': (255, 134, 0),
                          '135': (255, 135, 0),
                          '136': (255, 136, 0),
                          '137': (255, 137, 0),
                          '138': (255, 138, 0),
                          '139': (255, 139, 0),
                          '140': (255, 140, 0),
                          '141': (255, 141, 0),
                          '142': (255, 142, 0),
                          '143': (255, 143, 0),
                          '144': (255, 144, 0),
                          '145': (255, 145, 0),
                          '146': (255, 146, 0),
                          '147': (255, 147, 0),
                          '148': (255, 148, 0),
                          '149': (255, 149, 0),
                          '150': (255, 150, 0),
                          '151': (255, 151, 0),
                          '152': (255, 152, 0),
                          '153': (255, 153, 0),
                          '154': (255, 154, 0),
                          '155': (255, 155, 0),
                          '156': (255, 156, 0),
                          '157': (255, 157, 0),
                          '158': (255, 158, 0),
                          '159': (255, 159, 0),
                          '160': (255, 160, 0),
                          '161': (255, 161, 0),
                          '162': (255, 162, 0),
                          '163': (255, 163, 0),
                          '164': (255, 164, 0),
                          '165': (255, 165, 0),
                          '166': (255, 166, 0),
                          '167': (255, 167, 0),
                          '168': (255, 168, 0),
                          '169': (255, 169, 0),
                          '170': (255, 170, 0),
                          '171': (255, 171, 0),
                          '172': (255, 172, 0),
                          '173': (255, 173, 0),
                          '174': (255, 174, 0),
                          '175': (255, 175, 0),
                          '176': (255, 176, 0),
                          '177': (255, 177, 0),
                          '178': (255, 178, 0),
                          '179': (255, 179, 0),
                          '180': (255, 180, 0),
                          '181': (255, 181, 0),
                          '182': (255, 182, 0),
                          '183': (255, 183, 0),
                          '184': (255, 184, 0),
                          '185': (255, 185, 0),
                          '186': (255, 186, 0),
                          '187': (255, 187, 0),
                          '188': (255, 188, 0),
                          '189': (255, 189, 0),
                          '190': (255, 190, 0),
                          '191': (255, 191, 0),
                          '192': (255, 192, 0),
                          '193': (255, 193, 0),
                          '194': (255, 194, 0),
                          '195': (255, 195, 0),
                          '196': (255, 196, 0),
                          '197': (255, 197, 0),
                          '198': (255, 198, 0),
                          '199': (255, 199, 0),
                          '200': (255, 200, 0),
                          '201': (255, 201, 0),
                          '202': (255, 202, 0),
                          '203': (255, 203, 0),
                          '204': (255, 204, 0),
                          '205': (255, 205, 0),
                          '206': (255, 206, 0),
                          '207': (255, 207, 0),
                          '208': (255, 208, 0),
                          '209': (255, 209, 0),
                          '210': (255, 210, 0),
                          '211': (255, 211, 0),
                          '212': (255, 212, 0),
                          '213': (255, 213, 0),
                          '214': (255, 214, 0),
                          '215': (255, 215, 0),
                          '216': (255, 216, 0),
                          '217': (255, 217, 0),
                          '218': (255, 218, 0),
                          '219': (255, 219, 0),
                          '220': (255, 220, 0),
                          '221': (255, 221, 0),
                          '222': (255, 222, 0),
                          '223': (255, 223, 0),
                          '224': (255, 224, 0),
                          '225': (255, 225, 0),
                          '226': (255, 226, 0),
                          '227': (255, 227, 0),
                          '228': (255, 228, 0),
                          '229': (255, 229, 0),
                          '230': (255, 230, 0),
                          '231': (255, 231, 0),
                          '232': (255, 232, 0),
                          '233': (255, 233, 0),
                          '234': (255, 234, 0),
                          '235': (255, 235, 0),
                          '236': (255, 236, 0),
                          '237': (255, 237, 0),
                          '238': (255, 238, 0),
                          '239': (255, 239, 0),
                          '240': (255, 240, 0),
                          '241': (255, 241, 0),
                          '242': (255, 242, 0),
                          '243': (255, 243, 0),
                          '244': (255, 244, 0),
                          '245': (255, 245, 0),
                          '246': (255, 246, 0),
                          '247': (255, 247, 0),
                          '248': (255, 248, 0),
                          '249': (255, 249, 0),
                          '250': (255, 250, 0),
                          '251': (255, 251, 0),
                          '252': (255, 252, 0),
                          '253': (255, 253, 0),
                          '254': (255, 254, 0),
                          '255': (255, 255, 0),
                          '256': (254, 255, 0),
                          '257': (253, 255, 0),
                          '258': (252, 255, 0),
                          '259': (251, 255, 0),
                          '260': (250, 255, 0),
                          '261': (249, 255, 0),
                          '262': (248, 255, 0),
                          '263': (247, 255, 0),
                          '264': (246, 255, 0),
                          '265': (245, 255, 0),
                          '266': (244, 255, 0),
                          '267': (243, 255, 0),
                          '268': (242, 255, 0),
                          '269': (241, 255, 0),
                          '270': (240, 255, 0),
                          '271': (239, 255, 0),
                          '272': (238, 255, 0),
                          '273': (237, 255, 0),
                          '274': (236, 255, 0),
                          '275': (235, 255, 0),
                          '276': (234, 255, 0),
                          '277': (233, 255, 0),
                          '278': (232, 255, 0),
                          '279': (231, 255, 0),
                          '280': (230, 255, 0),
                          '281': (229, 255, 0),
                          '282': (228, 255, 0),
                          '283': (227, 255, 0),
                          '284': (226, 255, 0),
                          '285': (225, 255, 0),
                          '286': (224, 255, 0),
                          '287': (223, 255, 0),
                          '288': (222, 255, 0),
                          '289': (221, 255, 0),
                          '290': (220, 255, 0),
                          '291': (219, 255, 0),
                          '292': (218, 255, 0),
                          '293': (217, 255, 0),
                          '294': (216, 255, 0),
                          '295': (215, 255, 0),
                          '296': (214, 255, 0),
                          '297': (213, 255, 0),
                          '298': (212, 255, 0),
                          '299': (211, 255, 0),
                          '300': (210, 255, 0),
                          '301': (209, 255, 0),
                          '302': (208, 255, 0),
                          '303': (207, 255, 0),
                          '304': (206, 255, 0),
                          '305': (205, 255, 0),
                          '306': (204, 255, 0),
                          '307': (203, 255, 0),
                          '308': (202, 255, 0),
                          '309': (201, 255, 0),
                          '310': (200, 255, 0),
                          '311': (199, 255, 0),
                          '312': (198, 255, 0),
                          '313': (197, 255, 0),
                          '314': (196, 255, 0),
                          '315': (195, 255, 0),
                          '316': (194, 255, 0),
                          '317': (193, 255, 0),
                          '318': (192, 255, 0),
                          '319': (191, 255, 0),
                          '320': (190, 255, 0),
                          '321': (189, 255, 0),
                          '322': (188, 255, 0),
                          '323': (187, 255, 0),
                          '324': (186, 255, 0),
                          '325': (185, 255, 0),
                          '326': (184, 255, 0),
                          '327': (183, 255, 0),
                          '328': (182, 255, 0),
                          '329': (181, 255, 0),
                          '330': (180, 255, 0),
                          '331': (179, 255, 0),
                          '332': (178, 255, 0),
                          '333': (177, 255, 0),
                          '334': (176, 255, 0),
                          '335': (175, 255, 0),
                          '336': (174, 255, 0),
                          '337': (173, 255, 0),
                          '338': (172, 255, 0),
                          '339': (171, 255, 0),
                          '340': (170, 255, 0),
                          '341': (169, 255, 0),
                          '342': (168, 255, 0),
                          '343': (167, 255, 0),
                          '344': (166, 255, 0),
                          '345': (165, 255, 0),
                          '346': (164, 255, 0),
                          '347': (163, 255, 0),
                          '348': (162, 255, 0),
                          '349': (161, 255, 0),
                          '350': (160, 255, 0),
                          '351': (159, 255, 0),
                          '352': (158, 255, 0),
                          '353': (157, 255, 0),
                          '354': (156, 255, 0),
                          '355': (155, 255, 0),
                          '356': (154, 255, 0),
                          '357': (153, 255, 0),
                          '358': (152, 255, 0),
                          '359': (151, 255, 0),
                          '360': (150, 255, 0),
                          '361': (149, 255, 0),
                          '362': (148, 255, 0),
                          '363': (147, 255, 0),
                          '364': (146, 255, 0),
                          '365': (145, 255, 0),
                          '366': (144, 255, 0),
                          '367': (143, 255, 0),
                          '368': (142, 255, 0),
                          '369': (141, 255, 0),
                          '370': (140, 255, 0),
                          '371': (139, 255, 0),
                          '372': (138, 255, 0),
                          '373': (137, 255, 0),
                          '374': (136, 255, 0),
                          '375': (135, 255, 0),
                          '376': (134, 255, 0),
                          '377': (133, 255, 0),
                          '378': (132, 255, 0),
                          '379': (131, 255, 0),
                          '380': (130, 255, 0),
                          '381': (129, 255, 0),
                          '382': (128, 255, 0),
                          '383': (127, 255, 0),
                          '384': (126, 255, 0),
                          '385': (125, 255, 0),
                          '386': (124, 255, 0),
                          '387': (123, 255, 0),
                          '388': (122, 255, 0),
                          '389': (121, 255, 0),
                          '390': (120, 255, 0),
                          '391': (119, 255, 0),
                          '392': (118, 255, 0),
                          '393': (117, 255, 0),
                          '394': (116, 255, 0),
                          '395': (115, 255, 0),
                          '396': (114, 255, 0),
                          '397': (113, 255, 0),
                          '398': (112, 255, 0),
                          '399': (111, 255, 0),
                          '400': (110, 255, 0),
                          '401': (109, 255, 0),
                          '402': (108, 255, 0),
                          '403': (107, 255, 0),
                          '404': (106, 255, 0),
                          '405': (105, 255, 0),
                          '406': (104, 255, 0),
                          '407': (103, 255, 0),
                          '408': (102, 255, 0),
                          '409': (101, 255, 0),
                          '410': (100, 255, 0),
                          '411': (99, 255, 0),
                          '412': (98, 255, 0),
                          '413': (97, 255, 0),
                          '414': (96, 255, 0),
                          '415': (95, 255, 0),
                          '416': (94, 255, 0),
                          '417': (93, 255, 0),
                          '418': (92, 255, 0),
                          '419': (91, 255, 0),
                          '420': (90, 255, 0),
                          '421': (89, 255, 0),
                          '422': (88, 255, 0),
                          '423': (87, 255, 0),
                          '424': (86, 255, 0),
                          '425': (85, 255, 0),
                          '426': (84, 255, 0),
                          '427': (83, 255, 0),
                          '428': (82, 255, 0),
                          '429': (81, 255, 0),
                          '430': (80, 255, 0),
                          '431': (79, 255, 0),
                          '432': (78, 255, 0),
                          '433': (77, 255, 0),
                          '434': (76, 255, 0),
                          '435': (75, 255, 0),
                          '436': (74, 255, 0),
                          '437': (73, 255, 0),
                          '438': (72, 255, 0),
                          '439': (71, 255, 0),
                          '440': (70, 255, 0),
                          '441': (69, 255, 0),
                          '442': (68, 255, 0),
                          '443': (67, 255, 0),
                          '444': (66, 255, 0),
                          '445': (65, 255, 0),
                          '446': (64, 255, 0),
                          '447': (63, 255, 0),
                          '448': (62, 255, 0),
                          '449': (61, 255, 0),
                          '450': (60, 255, 0),
                          '451': (59, 255, 0),
                          '452': (58, 255, 0),
                          '453': (57, 255, 0),
                          '454': (56, 255, 0),
                          '455': (55, 255, 0),
                          '456': (54, 255, 0),
                          '457': (53, 255, 0),
                          '458': (52, 255, 0),
                          '459': (51, 255, 0),
                          '460': (50, 255, 0),
                          '461': (49, 255, 0),
                          '462': (48, 255, 0),
                          '463': (47, 255, 0),
                          '464': (46, 255, 0),
                          '465': (45, 255, 0),
                          '466': (44, 255, 0),
                          '467': (43, 255, 0),
                          '468': (42, 255, 0),
                          '469': (41, 255, 0),
                          '470': (40, 255, 0),
                          '471': (39, 255, 0),
                          '472': (38, 255, 0),
                          '473': (37, 255, 0),
                          '474': (36, 255, 0),
                          '475': (35, 255, 0),
                          '476': (34, 255, 0),
                          '477': (33, 255, 0),
                          '478': (32, 255, 0),
                          '479': (31, 255, 0),
                          '480': (30, 255, 0),
                          '481': (29, 255, 0),
                          '482': (28, 255, 0),
                          '483': (27, 255, 0),
                          '484': (26, 255, 0),
                          '485': (25, 255, 0),
                          '486': (24, 255, 0),
                          '487': (23, 255, 0),
                          '488': (22, 255, 0),
                          '489': (21, 255, 0),
                          '490': (20, 255, 0),
                          '491': (19, 255, 0),
                          '492': (18, 255, 0),
                          '493': (17, 255, 0),
                          '494': (16, 255, 0),
                          '495': (15, 255, 0),
                          '496': (14, 255, 0),
                          '497': (13, 255, 0),
                          '498': (12, 255, 0),
                          '499': (11, 255, 0),
                          '500': (10, 255, 0),
                          '501': (9, 255, 0),
                          '502': (8, 255, 0),
                          '503': (7, 255, 0),
                          '504': (6, 255, 0),
                          '505': (5, 255, 0),
                          '506': (4, 255, 0),
                          '507': (3, 255, 0),
                          '508': (2, 255, 0),
                          '509': (1, 255, 0),
                          '510': (0, 255, 0),
                          '511': (0, 255, 1),
                          '512': (0, 255, 2),
                          '513': (0, 255, 3),
                          '514': (0, 255, 4),
                          '515': (0, 255, 5),
                          '516': (0, 255, 6),
                          '517': (0, 255, 7),
                          '518': (0, 255, 8),
                          '519': (0, 255, 9),
                          '520': (0, 255, 10),
                          '521': (0, 255, 11),
                          '522': (0, 255, 12),
                          '523': (0, 255, 13),
                          '524': (0, 255, 14),
                          '525': (0, 255, 15),
                          '526': (0, 255, 16),
                          '527': (0, 255, 17),
                          '528': (0, 255, 18),
                          '529': (0, 255, 19),
                          '530': (0, 255, 20),
                          '531': (0, 255, 21),
                          '532': (0, 255, 22),
                          '533': (0, 255, 23),
                          '534': (0, 255, 24),
                          '535': (0, 255, 25),
                          '536': (0, 255, 26),
                          '537': (0, 255, 27),
                          '538': (0, 255, 28),
                          '539': (0, 255, 29),
                          '540': (0, 255, 30),
                          '541': (0, 255, 31),
                          '542': (0, 255, 32),
                          '543': (0, 255, 33),
                          '544': (0, 255, 34),
                          '545': (0, 255, 35),
                          '546': (0, 255, 36),
                          '547': (0, 255, 37),
                          '548': (0, 255, 38),
                          '549': (0, 255, 39),
                          '550': (0, 255, 40),
                          '551': (0, 255, 41),
                          '552': (0, 255, 42),
                          '553': (0, 255, 43),
                          '554': (0, 255, 44),
                          '555': (0, 255, 45),
                          '556': (0, 255, 46),
                          '557': (0, 255, 47),
                          '558': (0, 255, 48),
                          '559': (0, 255, 49),
                          '560': (0, 255, 50),
                          '561': (0, 255, 51),
                          '562': (0, 255, 52),
                          '563': (0, 255, 53),
                          '564': (0, 255, 54),
                          '565': (0, 255, 55),
                          '566': (0, 255, 56),
                          '567': (0, 255, 57),
                          '568': (0, 255, 58),
                          '569': (0, 255, 59),
                          '570': (0, 255, 60),
                          '571': (0, 255, 61),
                          '572': (0, 255, 62),
                          '573': (0, 255, 63),
                          '574': (0, 255, 64),
                          '575': (0, 255, 65),
                          '576': (0, 255, 66),
                          '577': (0, 255, 67),
                          '578': (0, 255, 68),
                          '579': (0, 255, 69),
                          '580': (0, 255, 70),
                          '581': (0, 255, 71),
                          '582': (0, 255, 72),
                          '583': (0, 255, 73),
                          '584': (0, 255, 74),
                          '585': (0, 255, 75),
                          '586': (0, 255, 76),
                          '587': (0, 255, 77),
                          '588': (0, 255, 78),
                          '589': (0, 255, 79),
                          '590': (0, 255, 80),
                          '591': (0, 255, 81),
                          '592': (0, 255, 82),
                          '593': (0, 255, 83),
                          '594': (0, 255, 84),
                          '595': (0, 255, 85),
                          '596': (0, 255, 86),
                          '597': (0, 255, 87),
                          '598': (0, 255, 88),
                          '599': (0, 255, 89),
                          '600': (0, 255, 90),
                          '601': (0, 255, 91),
                          '602': (0, 255, 92),
                          '603': (0, 255, 93),
                          '604': (0, 255, 94),
                          '605': (0, 255, 95),
                          '606': (0, 255, 96),
                          '607': (0, 255, 97),
                          '608': (0, 255, 98),
                          '609': (0, 255, 99),
                          '610': (0, 255, 100),
                          '611': (0, 255, 101),
                          '612': (0, 255, 102),
                          '613': (0, 255, 103),
                          '614': (0, 255, 104),
                          '615': (0, 255, 105),
                          '616': (0, 255, 106),
                          '617': (0, 255, 107),
                          '618': (0, 255, 108),
                          '619': (0, 255, 109),
                          '620': (0, 255, 110),
                          '621': (0, 255, 111),
                          '622': (0, 255, 112),
                          '623': (0, 255, 113),
                          '624': (0, 255, 114),
                          '625': (0, 255, 115),
                          '626': (0, 255, 116),
                          '627': (0, 255, 117),
                          '628': (0, 255, 118),
                          '629': (0, 255, 119),
                          '630': (0, 255, 120),
                          '631': (0, 255, 121),
                          '632': (0, 255, 122),
                          '633': (0, 255, 123),
                          '634': (0, 255, 124),
                          '635': (0, 255, 125),
                          '636': (0, 255, 126),
                          '637': (0, 255, 127),
                          '638': (0, 255, 128),
                          '639': (0, 255, 129),
                          '640': (0, 255, 130),
                          '641': (0, 255, 131),
                          '642': (0, 255, 132),
                          '643': (0, 255, 133),
                          '644': (0, 255, 134),
                          '645': (0, 255, 135),
                          '646': (0, 255, 136),
                          '647': (0, 255, 137),
                          '648': (0, 255, 138),
                          '649': (0, 255, 139),
                          '650': (0, 255, 140),
                          '651': (0, 255, 141),
                          '652': (0, 255, 142),
                          '653': (0, 255, 143),
                          '654': (0, 255, 144),
                          '655': (0, 255, 145),
                          '656': (0, 255, 146),
                          '657': (0, 255, 147),
                          '658': (0, 255, 148),
                          '659': (0, 255, 149),
                          '660': (0, 255, 150),
                          '661': (0, 255, 151),
                          '662': (0, 255, 152),
                          '663': (0, 255, 153),
                          '664': (0, 255, 154),
                          '665': (0, 255, 155),
                          '666': (0, 255, 156),
                          '667': (0, 255, 157),
                          '668': (0, 255, 158),
                          '669': (0, 255, 159),
                          '670': (0, 255, 160),
                          '671': (0, 255, 161),
                          '672': (0, 255, 162),
                          '673': (0, 255, 163),
                          '674': (0, 255, 164),
                          '675': (0, 255, 165),
                          '676': (0, 255, 166),
                          '677': (0, 255, 167),
                          '678': (0, 255, 168),
                          '679': (0, 255, 169),
                          '680': (0, 255, 170),
                          '681': (0, 255, 171),
                          '682': (0, 255, 172),
                          '683': (0, 255, 173),
                          '684': (0, 255, 174),
                          '685': (0, 255, 175),
                          '686': (0, 255, 176),
                          '687': (0, 255, 177),
                          '688': (0, 255, 178),
                          '689': (0, 255, 179),
                          '690': (0, 255, 180),
                          '691': (0, 255, 181),
                          '692': (0, 255, 182),
                          '693': (0, 255, 183),
                          '694': (0, 255, 184),
                          '695': (0, 255, 185),
                          '696': (0, 255, 186),
                          '697': (0, 255, 187),
                          '698': (0, 255, 188),
                          '699': (0, 255, 189),
                          '700': (0, 255, 190),
                          '701': (0, 255, 191),
                          '702': (0, 255, 192),
                          '703': (0, 255, 193),
                          '704': (0, 255, 194),
                          '705': (0, 255, 195),
                          '706': (0, 255, 196),
                          '707': (0, 255, 197),
                          '708': (0, 255, 198),
                          '709': (0, 255, 199),
                          '710': (0, 255, 200),
                          '711': (0, 255, 201),
                          '712': (0, 255, 202),
                          '713': (0, 255, 203),
                          '714': (0, 255, 204),
                          '715': (0, 255, 205),
                          '716': (0, 255, 206),
                          '717': (0, 255, 207),
                          '718': (0, 255, 208),
                          '719': (0, 255, 209),
                          '720': (0, 255, 210),
                          '721': (0, 255, 211),
                          '722': (0, 255, 212),
                          '723': (0, 255, 213),
                          '724': (0, 255, 214),
                          '725': (0, 255, 215),
                          '726': (0, 255, 216),
                          '727': (0, 255, 217),
                          '728': (0, 255, 218),
                          '729': (0, 255, 219),
                          '730': (0, 255, 220),
                          '731': (0, 255, 221),
                          '732': (0, 255, 222),
                          '733': (0, 255, 223),
                          '734': (0, 255, 224),
                          '735': (0, 255, 225),
                          '736': (0, 255, 226),
                          '737': (0, 255, 227),
                          '738': (0, 255, 228),
                          '739': (0, 255, 229),
                          '740': (0, 255, 230),
                          '741': (0, 255, 231),
                          '742': (0, 255, 232),
                          '743': (0, 255, 233),
                          '744': (0, 255, 234),
                          '745': (0, 255, 235),
                          '746': (0, 255, 236),
                          '747': (0, 255, 237),
                          '748': (0, 255, 238),
                          '749': (0, 255, 239),
                          '750': (0, 255, 240),
                          '751': (0, 255, 241),
                          '752': (0, 255, 242),
                          '753': (0, 255, 243),
                          '754': (0, 255, 244),
                          '755': (0, 255, 245),
                          '756': (0, 255, 246),
                          '757': (0, 255, 247),
                          '758': (0, 255, 248),
                          '759': (0, 255, 249),
                          '760': (0, 255, 250),
                          '761': (0, 255, 251),
                          '762': (0, 255, 252),
                          '763': (0, 255, 253),
                          '764': (0, 255, 254),
                          '765': (0, 255, 255),
                          '766': (0, 254, 255),
                          '767': (0, 253, 255),
                          '768': (0, 252, 255),
                          '769': (0, 251, 255),
                          '770': (0, 250, 255),
                          '771': (0, 249, 255),
                          '772': (0, 248, 255),
                          '773': (0, 247, 255),
                          '774': (0, 246, 255),
                          '775': (0, 245, 255),
                          '776': (0, 244, 255),
                          '777': (0, 243, 255),
                          '778': (0, 242, 255),
                          '779': (0, 241, 255),
                          '780': (0, 240, 255),
                          '781': (0, 239, 255),
                          '782': (0, 238, 255),
                          '783': (0, 237, 255),
                          '784': (0, 236, 255),
                          '785': (0, 235, 255),
                          '786': (0, 234, 255),
                          '787': (0, 233, 255),
                          '788': (0, 232, 255),
                          '789': (0, 231, 255),
                          '790': (0, 230, 255),
                          '791': (0, 229, 255),
                          '792': (0, 228, 255),
                          '793': (0, 227, 255),
                          '794': (0, 226, 255),
                          '795': (0, 225, 255),
                          '796': (0, 224, 255),
                          '797': (0, 223, 255),
                          '798': (0, 222, 255),
                          '799': (0, 221, 255),
                          '800': (0, 220, 255),
                          '801': (0, 219, 255),
                          '802': (0, 218, 255),
                          '803': (0, 217, 255),
                          '804': (0, 216, 255),
                          '805': (0, 215, 255),
                          '806': (0, 214, 255),
                          '807': (0, 213, 255),
                          '808': (0, 212, 255),
                          '809': (0, 211, 255),
                          '810': (0, 210, 255),
                          '811': (0, 209, 255),
                          '812': (0, 208, 255),
                          '813': (0, 207, 255),
                          '814': (0, 206, 255),
                          '815': (0, 205, 255),
                          '816': (0, 204, 255),
                          '817': (0, 203, 255),
                          '818': (0, 202, 255),
                          '819': (0, 201, 255),
                          '820': (0, 200, 255),
                          '821': (0, 199, 255),
                          '822': (0, 198, 255),
                          '823': (0, 197, 255),
                          '824': (0, 196, 255),
                          '825': (0, 195, 255),
                          '826': (0, 194, 255),
                          '827': (0, 193, 255),
                          '828': (0, 192, 255),
                          '829': (0, 191, 255),
                          '830': (0, 190, 255),
                          '831': (0, 189, 255),
                          '832': (0, 188, 255),
                          '833': (0, 187, 255),
                          '834': (0, 186, 255),
                          '835': (0, 185, 255),
                          '836': (0, 184, 255),
                          '837': (0, 183, 255),
                          '838': (0, 182, 255),
                          '839': (0, 181, 255),
                          '840': (0, 180, 255),
                          '841': (0, 179, 255),
                          '842': (0, 178, 255),
                          '843': (0, 177, 255),
                          '844': (0, 176, 255),
                          '845': (0, 175, 255),
                          '846': (0, 174, 255),
                          '847': (0, 173, 255),
                          '848': (0, 172, 255),
                          '849': (0, 171, 255),
                          '850': (0, 170, 255),
                          '851': (0, 169, 255),
                          '852': (0, 168, 255),
                          '853': (0, 167, 255),
                          '854': (0, 166, 255),
                          '855': (0, 165, 255),
                          '856': (0, 164, 255),
                          '857': (0, 163, 255),
                          '858': (0, 162, 255),
                          '859': (0, 161, 255),
                          '860': (0, 160, 255),
                          '861': (0, 159, 255),
                          '862': (0, 158, 255),
                          '863': (0, 157, 255),
                          '864': (0, 156, 255),
                          '865': (0, 155, 255),
                          '866': (0, 154, 255),
                          '867': (0, 153, 255),
                          '868': (0, 152, 255),
                          '869': (0, 151, 255),
                          '870': (0, 150, 255),
                          '871': (0, 149, 255),
                          '872': (0, 148, 255),
                          '873': (0, 147, 255),
                          '874': (0, 146, 255),
                          '875': (0, 145, 255),
                          '876': (0, 144, 255),
                          '877': (0, 143, 255),
                          '878': (0, 142, 255),
                          '879': (0, 141, 255),
                          '880': (0, 140, 255),
                          '881': (0, 139, 255),
                          '882': (0, 138, 255),
                          '883': (0, 137, 255),
                          '884': (0, 136, 255),
                          '885': (0, 135, 255),
                          '886': (0, 134, 255),
                          '887': (0, 133, 255),
                          '888': (0, 132, 255),
                          '889': (0, 131, 255),
                          '890': (0, 130, 255),
                          '891': (0, 129, 255),
                          '892': (0, 128, 255),
                          '893': (0, 127, 255),
                          '894': (0, 126, 255),
                          '895': (0, 125, 255),
                          '896': (0, 124, 255),
                          '897': (0, 123, 255),
                          '898': (0, 122, 255),
                          '899': (0, 121, 255),
                          '900': (0, 120, 255),
                          '901': (0, 119, 255),
                          '902': (0, 118, 255),
                          '903': (0, 117, 255),
                          '904': (0, 116, 255),
                          '905': (0, 115, 255),
                          '906': (0, 114, 255),
                          '907': (0, 113, 255),
                          '908': (0, 112, 255),
                          '909': (0, 111, 255),
                          '910': (0, 110, 255),
                          '911': (0, 109, 255),
                          '912': (0, 108, 255),
                          '913': (0, 107, 255),
                          '914': (0, 106, 255),
                          '915': (0, 105, 255),
                          '916': (0, 104, 255),
                          '917': (0, 103, 255),
                          '918': (0, 102, 255),
                          '919': (0, 101, 255),
                          '920': (0, 100, 255),
                          '921': (0, 99, 255),
                          '922': (0, 98, 255),
                          '923': (0, 97, 255),
                          '924': (0, 96, 255),
                          '925': (0, 95, 255),
                          '926': (0, 94, 255),
                          '927': (0, 93, 255),
                          '928': (0, 92, 255),
                          '929': (0, 91, 255),
                          '930': (0, 90, 255),
                          '931': (0, 89, 255),
                          '932': (0, 88, 255),
                          '933': (0, 87, 255),
                          '934': (0, 86, 255),
                          '935': (0, 85, 255),
                          '936': (0, 84, 255),
                          '937': (0, 83, 255),
                          '938': (0, 82, 255),
                          '939': (0, 81, 255),
                          '940': (0, 80, 255),
                          '941': (0, 79, 255),
                          '942': (0, 78, 255),
                          '943': (0, 77, 255),
                          '944': (0, 76, 255),
                          '945': (0, 75, 255),
                          '946': (0, 74, 255),
                          '947': (0, 73, 255),
                          '948': (0, 72, 255),
                          '949': (0, 71, 255),
                          '950': (0, 70, 255),
                          '951': (0, 69, 255),
                          '952': (0, 68, 255),
                          '953': (0, 67, 255),
                          '954': (0, 66, 255),
                          '955': (0, 65, 255),
                          '956': (0, 64, 255),
                          '957': (0, 63, 255),
                          '958': (0, 62, 255),
                          '959': (0, 61, 255),
                          '960': (0, 60, 255),
                          '961': (0, 59, 255),
                          '962': (0, 58, 255),
                          '963': (0, 57, 255),
                          '964': (0, 56, 255),
                          '965': (0, 55, 255),
                          '966': (0, 54, 255),
                          '967': (0, 53, 255),
                          '968': (0, 52, 255),
                          '969': (0, 51, 255),
                          '970': (0, 50, 255),
                          '971': (0, 49, 255),
                          '972': (0, 48, 255),
                          '973': (0, 47, 255),
                          '974': (0, 46, 255),
                          '975': (0, 45, 255),
                          '976': (0, 44, 255),
                          '977': (0, 43, 255),
                          '978': (0, 42, 255),
                          '979': (0, 41, 255),
                          '980': (0, 40, 255),
                          '981': (0, 39, 255),
                          '982': (0, 38, 255),
                          '983': (0, 37, 255),
                          '984': (0, 36, 255),
                          '985': (0, 35, 255),
                          '986': (0, 34, 255),
                          '987': (0, 33, 255),
                          '988': (0, 32, 255),
                          '989': (0, 31, 255),
                          '990': (0, 30, 255),
                          '991': (0, 29, 255),
                          '992': (0, 28, 255),
                          '993': (0, 27, 255),
                          '994': (0, 26, 255),
                          '995': (0, 25, 255),
                          '996': (0, 24, 255),
                          '997': (0, 23, 255),
                          '998': (0, 22, 255),
                          '999': (0, 21, 255),
                          '1000': (0, 20, 255),
                          '1001': (0, 19, 255),
                          '1002': (0, 18, 255),
                          '1003': (0, 17, 255),
                          '1004': (0, 16, 255),
                          '1005': (0, 15, 255),
                          '1006': (0, 14, 255),
                          '1007': (0, 13, 255),
                          '1008': (0, 12, 255),
                          '1009': (0, 11, 255),
                          '1010': (0, 10, 255),
                          '1011': (0, 9, 255),
                          '1012': (0, 8, 255),
                          '1013': (0, 7, 255),
                          '1014': (0, 6, 255),
                          '1015': (0, 5, 255),
                          '1016': (0, 4, 255),
                          '1017': (0, 3, 255),
                          '1018': (0, 2, 255),
                          '1019': (0, 1, 255),
                          '1020': (0, 0, 255),
                          '1021': (1, 0, 255),
                          '1022': (2, 0, 255),
                          '1023': (3, 0, 255),
                          '1024': (4, 0, 255),
                          '1025': (5, 0, 255),
                          '1026': (6, 0, 255),
                          '1027': (7, 0, 255),
                          '1028': (8, 0, 255),
                          '1029': (9, 0, 255),
                          '1030': (10, 0, 255),
                          '1031': (11, 0, 255),
                          '1032': (12, 0, 255),
                          '1033': (13, 0, 255),
                          '1034': (14, 0, 255),
                          '1035': (15, 0, 255),
                          '1036': (16, 0, 255),
                          '1037': (17, 0, 255),
                          '1038': (18, 0, 255),
                          '1039': (19, 0, 255),
                          '1040': (20, 0, 255),
                          '1041': (21, 0, 255),
                          '1042': (22, 0, 255),
                          '1043': (23, 0, 255),
                          '1044': (24, 0, 255),
                          '1045': (25, 0, 255),
                          '1046': (26, 0, 255),
                          '1047': (27, 0, 255),
                          '1048': (28, 0, 255),
                          '1049': (29, 0, 255),
                          '1050': (30, 0, 255),
                          '1051': (31, 0, 255),
                          '1052': (32, 0, 255),
                          '1053': (33, 0, 255),
                          '1054': (34, 0, 255),
                          '1055': (35, 0, 255),
                          '1056': (36, 0, 255),
                          '1057': (37, 0, 255),
                          '1058': (38, 0, 255),
                          '1059': (39, 0, 255),
                          '1060': (40, 0, 255),
                          '1061': (41, 0, 255),
                          '1062': (42, 0, 255),
                          '1063': (43, 0, 255),
                          '1064': (44, 0, 255),
                          '1065': (45, 0, 255),
                          '1066': (46, 0, 255),
                          '1067': (47, 0, 255),
                          '1068': (48, 0, 255),
                          '1069': (49, 0, 255),
                          '1070': (50, 0, 255),
                          '1071': (51, 0, 255),
                          '1072': (52, 0, 255),
                          '1073': (53, 0, 255),
                          '1074': (54, 0, 255),
                          '1075': (55, 0, 255),
                          '1076': (56, 0, 255),
                          '1077': (57, 0, 255),
                          '1078': (58, 0, 255),
                          '1079': (59, 0, 255),
                          '1080': (60, 0, 255),
                          '1081': (61, 0, 255),
                          '1082': (62, 0, 255),
                          '1083': (63, 0, 255),
                          '1084': (64, 0, 255),
                          '1085': (65, 0, 255),
                          '1086': (66, 0, 255),
                          '1087': (67, 0, 255),
                          '1088': (68, 0, 255),
                          '1089': (69, 0, 255),
                          '1090': (70, 0, 255),
                          '1091': (71, 0, 255),
                          '1092': (72, 0, 255),
                          '1093': (73, 0, 255),
                          '1094': (74, 0, 255),
                          '1095': (75, 0, 255),
                          '1096': (76, 0, 255),
                          '1097': (77, 0, 255),
                          '1098': (78, 0, 255),
                          '1099': (79, 0, 255),
                          '1100': (80, 0, 255),
                          '1101': (81, 0, 255),
                          '1102': (82, 0, 255),
                          '1103': (83, 0, 255),
                          '1104': (84, 0, 255),
                          '1105': (85, 0, 255),
                          '1106': (86, 0, 255),
                          '1107': (87, 0, 255),
                          '1108': (88, 0, 255),
                          '1109': (89, 0, 255),
                          '1110': (90, 0, 255),
                          '1111': (91, 0, 255),
                          '1112': (92, 0, 255),
                          '1113': (93, 0, 255),
                          '1114': (94, 0, 255),
                          '1115': (95, 0, 255),
                          '1116': (96, 0, 255),
                          '1117': (97, 0, 255),
                          '1118': (98, 0, 255),
                          '1119': (99, 0, 255),
                          '1120': (100, 0, 255),
                          '1121': (101, 0, 255),
                          '1122': (102, 0, 255),
                          '1123': (103, 0, 255),
                          '1124': (104, 0, 255),
                          '1125': (105, 0, 255),
                          '1126': (106, 0, 255),
                          '1127': (107, 0, 255),
                          '1128': (108, 0, 255),
                          '1129': (109, 0, 255),
                          '1130': (110, 0, 255),
                          '1131': (111, 0, 255),
                          '1132': (112, 0, 255),
                          '1133': (113, 0, 255),
                          '1134': (114, 0, 255),
                          '1135': (115, 0, 255),
                          '1136': (116, 0, 255),
                          '1137': (117, 0, 255),
                          '1138': (118, 0, 255),
                          '1139': (119, 0, 255),
                          '1140': (120, 0, 255),
                          '1141': (121, 0, 255),
                          '1142': (122, 0, 255),
                          '1143': (123, 0, 255),
                          '1144': (124, 0, 255),
                          '1145': (125, 0, 255),
                          '1146': (126, 0, 255),
                          '1147': (127, 0, 255),
                          '1148': (128, 0, 255),
                          '1149': (129, 0, 255),
                          '1150': (130, 0, 255),
                          '1151': (131, 0, 255),
                          '1152': (132, 0, 255),
                          '1153': (133, 0, 255),
                          '1154': (134, 0, 255),
                          '1155': (135, 0, 255),
                          '1156': (136, 0, 255),
                          '1157': (137, 0, 255),
                          '1158': (138, 0, 255),
                          '1159': (139, 0, 255),
                          '1160': (140, 0, 255),
                          '1161': (141, 0, 255),
                          '1162': (142, 0, 255),
                          '1163': (143, 0, 255),
                          '1164': (144, 0, 255),
                          '1165': (145, 0, 255),
                          '1166': (146, 0, 255),
                          '1167': (147, 0, 255),
                          '1168': (148, 0, 255),
                          '1169': (149, 0, 255),
                          '1170': (150, 0, 255),
                          '1171': (151, 0, 255),
                          '1172': (152, 0, 255),
                          '1173': (153, 0, 255),
                          '1174': (154, 0, 255),
                          '1175': (155, 0, 255),
                          '1176': (156, 0, 255),
                          '1177': (157, 0, 255),
                          '1178': (158, 0, 255),
                          '1179': (159, 0, 255),
                          '1180': (160, 0, 255),
                          '1181': (161, 0, 255),
                          '1182': (162, 0, 255),
                          '1183': (163, 0, 255),
                          '1184': (164, 0, 255),
                          '1185': (165, 0, 255),
                          '1186': (166, 0, 255),
                          '1187': (167, 0, 255),
                          '1188': (168, 0, 255),
                          '1189': (169, 0, 255),
                          '1190': (170, 0, 255),
                          '1191': (171, 0, 255),
                          '1192': (172, 0, 255),
                          '1193': (173, 0, 255),
                          '1194': (174, 0, 255),
                          '1195': (175, 0, 255),
                          '1196': (176, 0, 255),
                          '1197': (177, 0, 255),
                          '1198': (178, 0, 255),
                          '1199': (179, 0, 255),
                          '1200': (180, 0, 255),
                          '1201': (181, 0, 255),
                          '1202': (182, 0, 255),
                          '1203': (183, 0, 255),
                          '1204': (184, 0, 255),
                          '1205': (185, 0, 255),
                          '1206': (186, 0, 255),
                          '1207': (187, 0, 255),
                          '1208': (188, 0, 255),
                          '1209': (189, 0, 255),
                          '1210': (190, 0, 255),
                          '1211': (191, 0, 255),
                          '1212': (192, 0, 255),
                          '1213': (193, 0, 255),
                          '1214': (194, 0, 255),
                          '1215': (195, 0, 255),
                          '1216': (196, 0, 255),
                          '1217': (197, 0, 255),
                          '1218': (198, 0, 255),
                          '1219': (199, 0, 255),
                          '1220': (200, 0, 255),
                          '1221': (201, 0, 255),
                          '1222': (202, 0, 255),
                          '1223': (203, 0, 255),
                          '1224': (204, 0, 255),
                          '1225': (205, 0, 255),
                          '1226': (206, 0, 255),
                          '1227': (207, 0, 255),
                          '1228': (208, 0, 255),
                          '1229': (209, 0, 255),
                          '1230': (210, 0, 255),
                          '1231': (211, 0, 255),
                          '1232': (212, 0, 255),
                          '1233': (213, 0, 255),
                          '1234': (214, 0, 255),
                          '1235': (215, 0, 255),
                          '1236': (216, 0, 255),
                          '1237': (217, 0, 255),
                          '1238': (218, 0, 255),
                          '1239': (219, 0, 255),
                          '1240': (220, 0, 255),
                          '1241': (221, 0, 255),
                          '1242': (222, 0, 255),
                          '1243': (223, 0, 255),
                          '1244': (224, 0, 255),
                          '1245': (225, 0, 255),
                          '1246': (226, 0, 255),
                          '1247': (227, 0, 255),
                          '1248': (228, 0, 255),
                          '1249': (229, 0, 255),
                          '1250': (230, 0, 255),
                          '1251': (231, 0, 255),
                          '1252': (232, 0, 255),
                          '1253': (233, 0, 255),
                          '1254': (234, 0, 255),
                          '1255': (235, 0, 255),
                          '1256': (236, 0, 255),
                          '1257': (237, 0, 255),
                          '1258': (238, 0, 255),
                          '1259': (239, 0, 255),
                          '1260': (240, 0, 255),
                          '1261': (241, 0, 255),
                          '1262': (242, 0, 255),
                          '1263': (243, 0, 255),
                          '1264': (244, 0, 255),
                          '1265': (245, 0, 255),
                          '1266': (246, 0, 255),
                          '1267': (247, 0, 255),
                          '1268': (248, 0, 255),
                          '1269': (249, 0, 255),
                          '1270': (250, 0, 255),
                          '1271': (251, 0, 255),
                          '1272': (252, 0, 255),
                          '1273': (253, 0, 255),
                          '1274': (254, 0, 255),
                          '1275': (255, 0, 255),
                          '1276': (255, 0, 254),
                          '1277': (255, 0, 253),
                          '1278': (255, 0, 252),
                          '1279': (255, 0, 251),
                          '1280': (255, 0, 250),
                          '1281': (255, 0, 249),
                          '1282': (255, 0, 248),
                          '1283': (255, 0, 247),
                          '1284': (255, 0, 246),
                          '1285': (255, 0, 245),
                          '1286': (255, 0, 244),
                          '1287': (255, 0, 243),
                          '1288': (255, 0, 242),
                          '1289': (255, 0, 241),
                          '1290': (255, 0, 240),
                          '1291': (255, 0, 239),
                          '1292': (255, 0, 238),
                          '1293': (255, 0, 237),
                          '1294': (255, 0, 236),
                          '1295': (255, 0, 235),
                          '1296': (255, 0, 234),
                          '1297': (255, 0, 233),
                          '1298': (255, 0, 232),
                          '1299': (255, 0, 231),
                          '1300': (255, 0, 230),
                          '1301': (255, 0, 229),
                          '1302': (255, 0, 228),
                          '1303': (255, 0, 227),
                          '1304': (255, 0, 226),
                          '1305': (255, 0, 225),
                          '1306': (255, 0, 224),
                          '1307': (255, 0, 223),
                          '1308': (255, 0, 222),
                          '1309': (255, 0, 221),
                          '1310': (255, 0, 220),
                          '1311': (255, 0, 219),
                          '1312': (255, 0, 218),
                          '1313': (255, 0, 217),
                          '1314': (255, 0, 216),
                          '1315': (255, 0, 215),
                          '1316': (255, 0, 214),
                          '1317': (255, 0, 213),
                          '1318': (255, 0, 212),
                          '1319': (255, 0, 211),
                          '1320': (255, 0, 210),
                          '1321': (255, 0, 209),
                          '1322': (255, 0, 208),
                          '1323': (255, 0, 207),
                          '1324': (255, 0, 206),
                          '1325': (255, 0, 205),
                          '1326': (255, 0, 204),
                          '1327': (255, 0, 203),
                          '1328': (255, 0, 202),
                          '1329': (255, 0, 201),
                          '1330': (255, 0, 200),
                          '1331': (255, 0, 199),
                          '1332': (255, 0, 198),
                          '1333': (255, 0, 197),
                          '1334': (255, 0, 196),
                          '1335': (255, 0, 195),
                          '1336': (255, 0, 194),
                          '1337': (255, 0, 193),
                          '1338': (255, 0, 192),
                          '1339': (255, 0, 191),
                          '1340': (255, 0, 190),
                          '1341': (255, 0, 189),
                          '1342': (255, 0, 188),
                          '1343': (255, 0, 187),
                          '1344': (255, 0, 186),
                          '1345': (255, 0, 185),
                          '1346': (255, 0, 184),
                          '1347': (255, 0, 183),
                          '1348': (255, 0, 182),
                          '1349': (255, 0, 181),
                          '1350': (255, 0, 180),
                          '1351': (255, 0, 179),
                          '1352': (255, 0, 178),
                          '1353': (255, 0, 177),
                          '1354': (255, 0, 176),
                          '1355': (255, 0, 175),
                          '1356': (255, 0, 174),
                          '1357': (255, 0, 173),
                          '1358': (255, 0, 172),
                          '1359': (255, 0, 171),
                          '1360': (255, 0, 170),
                          '1361': (255, 0, 169),
                          '1362': (255, 0, 168),
                          '1363': (255, 0, 167),
                          '1364': (255, 0, 166),
                          '1365': (255, 0, 165),
                          '1366': (255, 0, 164),
                          '1367': (255, 0, 163),
                          '1368': (255, 0, 162),
                          '1369': (255, 0, 161),
                          '1370': (255, 0, 160),
                          '1371': (255, 0, 159),
                          '1372': (255, 0, 158),
                          '1373': (255, 0, 157),
                          '1374': (255, 0, 156),
                          '1375': (255, 0, 155),
                          '1376': (255, 0, 154),
                          '1377': (255, 0, 153),
                          '1378': (255, 0, 152),
                          '1379': (255, 0, 151),
                          '1380': (255, 0, 150),
                          '1381': (255, 0, 149),
                          '1382': (255, 0, 148),
                          '1383': (255, 0, 147),
                          '1384': (255, 0, 146),
                          '1385': (255, 0, 145),
                          '1386': (255, 0, 144),
                          '1387': (255, 0, 143),
                          '1388': (255, 0, 142),
                          '1389': (255, 0, 141),
                          '1390': (255, 0, 140),
                          '1391': (255, 0, 139),
                          '1392': (255, 0, 138),
                          '1393': (255, 0, 137),
                          '1394': (255, 0, 136),
                          '1395': (255, 0, 135),
                          '1396': (255, 0, 134),
                          '1397': (255, 0, 133),
                          '1398': (255, 0, 132),
                          '1399': (255, 0, 131),
                          '1400': (255, 0, 130),
                          '1401': (255, 0, 129),
                          '1402': (255, 0, 128),
                          '1403': (255, 0, 127),
                          '1404': (255, 0, 126),
                          '1405': (255, 0, 125),
                          '1406': (255, 0, 124),
                          '1407': (255, 0, 123),
                          '1408': (255, 0, 122),
                          '1409': (255, 0, 121),
                          '1410': (255, 0, 120),
                          '1411': (255, 0, 119),
                          '1412': (255, 0, 118),
                          '1413': (255, 0, 117),
                          '1414': (255, 0, 116),
                          '1415': (255, 0, 115),
                          '1416': (255, 0, 114),
                          '1417': (255, 0, 113),
                          '1418': (255, 0, 112),
                          '1419': (255, 0, 111),
                          '1420': (255, 0, 110),
                          '1421': (255, 0, 109),
                          '1422': (255, 0, 108),
                          '1423': (255, 0, 107),
                          '1424': (255, 0, 106),
                          '1425': (255, 0, 105),
                          '1426': (255, 0, 104),
                          '1427': (255, 0, 103),
                          '1428': (255, 0, 102),
                          '1429': (255, 0, 101),
                          '1430': (255, 0, 100),
                          '1431': (255, 0, 99),
                          '1432': (255, 0, 98),
                          '1433': (255, 0, 97),
                          '1434': (255, 0, 96),
                          '1435': (255, 0, 95),
                          '1436': (255, 0, 94),
                          '1437': (255, 0, 93),
                          '1438': (255, 0, 92),
                          '1439': (255, 0, 91),
                          '1440': (255, 0, 90),
                          '1441': (255, 0, 89),
                          '1442': (255, 0, 88),
                          '1443': (255, 0, 87),
                          '1444': (255, 0, 86),
                          '1445': (255, 0, 85),
                          '1446': (255, 0, 84),
                          '1447': (255, 0, 83),
                          '1448': (255, 0, 82),
                          '1449': (255, 0, 81),
                          '1450': (255, 0, 80),
                          '1451': (255, 0, 79),
                          '1452': (255, 0, 78),
                          '1453': (255, 0, 77),
                          '1454': (255, 0, 76),
                          '1455': (255, 0, 75),
                          '1456': (255, 0, 74),
                          '1457': (255, 0, 73),
                          '1458': (255, 0, 72),
                          '1459': (255, 0, 71),
                          '1460': (255, 0, 70),
                          '1461': (255, 0, 69),
                          '1462': (255, 0, 68),
                          '1463': (255, 0, 67),
                          '1464': (255, 0, 66),
                          '1465': (255, 0, 65),
                          '1466': (255, 0, 64),
                          '1467': (255, 0, 63),
                          '1468': (255, 0, 62),
                          '1469': (255, 0, 61),
                          '1470': (255, 0, 60),
                          '1471': (255, 0, 59),
                          '1472': (255, 0, 58),
                          '1473': (255, 0, 57),
                          '1474': (255, 0, 56),
                          '1475': (255, 0, 55),
                          '1476': (255, 0, 54),
                          '1477': (255, 0, 53),
                          '1478': (255, 0, 52),
                          '1479': (255, 0, 51),
                          '1480': (255, 0, 50),
                          '1481': (255, 0, 49),
                          '1482': (255, 0, 48),
                          '1483': (255, 0, 47),
                          '1484': (255, 0, 46),
                          '1485': (255, 0, 45),
                          '1486': (255, 0, 44),
                          '1487': (255, 0, 43),
                          '1488': (255, 0, 42),
                          '1489': (255, 0, 41),
                          '1490': (255, 0, 40),
                          '1491': (255, 0, 39),
                          '1492': (255, 0, 38),
                          '1493': (255, 0, 37),
                          '1494': (255, 0, 36),
                          '1495': (255, 0, 35),
                          '1496': (255, 0, 34),
                          '1497': (255, 0, 33),
                          '1498': (255, 0, 32),
                          '1499': (255, 0, 31),
                          '1500': (255, 0, 30),
                          '1501': (255, 0, 29),
                          '1502': (255, 0, 28),
                          '1503': (255, 0, 27),
                          '1504': (255, 0, 26),
                          '1505': (255, 0, 25),
                          '1506': (255, 0, 24),
                          '1507': (255, 0, 23),
                          '1508': (255, 0, 22),
                          '1509': (255, 0, 21),
                          '1510': (255, 0, 20),
                          '1511': (255, 0, 19),
                          '1512': (255, 0, 18),
                          '1513': (255, 0, 17),
                          '1514': (255, 0, 16),
                          '1515': (255, 0, 15),
                          '1516': (255, 0, 14),
                          '1517': (255, 0, 13),
                          '1518': (255, 0, 12),
                          '1519': (255, 0, 11),
                          '1520': (255, 0, 10),
                          '1521': (255, 0, 9),
                          '1522': (255, 0, 8),
                          '1523': (255, 0, 7),
                          '1524': (255, 0, 6),
                          '1525': (255, 0, 5),
                          '1526': (255, 0, 4),
                          '1527': (255, 0, 3),
                          '1528': (255, 0, 2),
                          '1529': (255, 0, 1)}
draw()



root.mainloop()


































'''
print(i)
print(str(cities[i][0]))
print(str(cities[i][1]))
new_city_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text=str(cities[i][0]), fg='#00f3c3')
new_city_name.grid(row=((i*3)+1), column=0)

country_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text=str(cities[i][1]), fg='#00f3c3')
country_name.grid(row=((i*3)+2), column=0)


set_city_button = Button(city_info_frame, font=(settings_font, 15 ), text="Set " + str(cities[i][0]), fg='#222222', command=information)
set_city_button.grid(row=((i*3)+3), column=0)
'''



'''
set_city_button = Button(city_info_frame, font=(settings_font, 15 ), text="Set New City", fg='#222222', command=information)
set_city_button.grid(row=2, column=0)

new_city_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text=str(cities[0][0]), fg='#00f3c3')
new_city_name.grid(row=0, column=0)

country_name = Label(city_info_frame, background = '#222222', font=(settings_font, 15 ), text=country_name, fg='#00f3c3')
country_name.grid(row=1, column=0)

#information = partial(set_city, {'id':local_city_id,'name':city_full_name_2})
def information():
    print("global value thing")

set_city_button = Button(city_info_frame, font=(settings_font, 15 ), text="Set New City", fg='#222222', command=information)
set_city_button.grid(row=2, column=0)
'''

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
