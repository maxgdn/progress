#!/usr/bin/python3

import tkinter 
from tkinter import ttk

from datetime import *
import calendar


root = tkinter.Tk()
root.geometry('300x240')
root.title('Progress')
root.attributes('-type', 'dialog')
root.grid()

bar_size = 280
label_font_size=10
default_font = "TkDefaultFont"


def number_of_days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

def days_in_year(year=datetime.now().year):
    return 365 + calendar.isleap(year)

def format_bar_label(date_type, percentage):
    return date_type +" progress: " + "{:.2f}".format(percentage) + "%"

now = datetime.now()

current_date_string = now.strftime("%m/%d/%Y")
current_date_label = tkinter.Label(root, text="Date: " + current_date_string, font=(default_font, 16))
current_date_label.grid(column=0, row=0, columnspan=2, padx=0, pady=5)

# day progress bar
day_percentage = (now.hour / 24) * 100
day_label = tkinter.Label(root, text= format_bar_label("Day", day_percentage), font=(default_font,label_font_size))
day_label.grid(column=0, row=1, columnspan=2, padx=0, pady=10)

day_pb = ttk.Progressbar(
    root,
    orient='horizontal',
    length=bar_size
)

day_pb['value'] = day_percentage

day_pb.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# month progress bar
month_percentage =  (now.day / number_of_days_in_month(now.year, now.month)) * 100
month_label = tkinter.Label(root, text= format_bar_label("Month", month_percentage), font=(default_font,label_font_size))
month_label.grid(column=0, row=3, columnspan=2, padx=0, pady=5)

month_pb = ttk.Progressbar(
    root,
    orient='horizontal',
    length=bar_size
)

month_pb['value'] = month_percentage

month_pb.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# year progress bar
year_percentage = (now.timetuple().tm_yday/days_in_year()) * 100
year_label = tkinter.Label(root, text= format_bar_label("Year", year_percentage), font=(default_font,label_font_size))
year_label.grid(column=0, row=5, columnspan=2, padx=0, pady=5)

year_pb = ttk.Progressbar(
    root,
    orient='horizontal',
    length=bar_size
)

year_pb['value'] = year_percentage

year_pb.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

# close after 60 seconds
root.after(60 * 1000, root.destroy)
root.mainloop()