#!/usr/bin/python3

import tkinter 
from tkinter import ttk

from datetime import *;
from dateutil.relativedelta import *

import calendar

root = tkinter.Tk()
root.geometry('300x240')
root.title('Progress')
root.attributes('-type', 'dialog')
root.grid()

bar_size = 280
label_font_size=10

def number_of_days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

def days_in_year(year=datetime.now().year):
    return 365 + calendar.isleap(year)

now = datetime.now()

current_date_string = now.strftime("%m/%d/%Y")
current_date_label = tkinter.Label(root, text="Date: " +current_date_string, font=("TkDefaultFont",16))
current_date_label.grid(column=0, row=0, columnspan=2, padx=0, pady=5)

day_percentage = (now.hour / 24) * 100
day_label = tkinter.Label(root, text="Day progress: " + "{:.2f}".format(day_percentage) + "%", font=("TkDefaultFont",label_font_size))
day_label.grid(column=0, row=1, columnspan=2, padx=0, pady=10)

day_pb = ttk.Progressbar(
    root,
    orient='horizontal',
    length=bar_size
)

day_pb['value'] = day_percentage

day_pb.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

month_percentage =  (now.day / number_of_days_in_month(now.year, now.month)) * 100
month_label = tkinter.Label(root, text="Month progress: " + "{:.2f}".format(month_percentage) + "%", font=("TkDefaultFont",label_font_size))
month_label.grid(column=0, row=3, columnspan=2, padx=0, pady=5)

month_pb = ttk.Progressbar(
    root,
    orient='horizontal',
    length=bar_size
)

month_pb['value'] = month_percentage

month_pb.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

year_percentage = (now.timetuple().tm_yday/days_in_year()) * 100
year_label = tkinter.Label(root, text="Year progress: " + "{:.2f}".format(year_percentage) + "%", font=("TkDefaultFont",label_font_size))
year_label.grid(column=0, row=5, columnspan=2, padx=0, pady=5)

year_pb = ttk.Progressbar(
    root,
    orient='horizontal',
    length=bar_size
)

year_pb['value'] = year_percentage

year_pb.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

root.after(60 * 1000, root.destroy)
root.mainloop()