from calendar import TUESDAY
from cgitb import text

from tkinter import *

from operator import truediv
from re import A
from tkinter import *

from tracemalloc import start

import tkinter.font

import schedule
import time
import datetime


#from winsound import PlaySound
window = Tk()
window.title("School Bell")
window.geometry('800x600')

point = "normal"

font=tkinter.font.Font(family="맑은 고딕", size=25, slant="italic")
labeltext = Label(window, text = "평일 벨소리", font=font)
labeltext.pack(side="top", pady=30)

labeltexttime = Label(window, text = datetime.datetime.now(), font=font)
labeltexttime.pack(side="bottom", pady=30)


def first(): 
    point = "normal"
    print(point)
    labeltext.config(text="평일 벨소리")
    labeltext.pack()


def second():
    point = "exam"
    print(point)
    labeltext.config(text="시험 벨소리")
    labeltext.pack()
  
print()




btn1 = Button(window, text="평일 벨소리", width=30, height=15, command=first)
btn1.pack(side="left", padx=50)


btn2 = Button(window, text="시험 벨소리", width=30, height=15, command= second)
btn2.pack(side="right", padx=50)


btn2 = Button(window, text="시험 벨소리", width=30, height=15, command=second)
btn2.pack(side="right", padx=50)




def reset():
  a = datetime.datetime.now()
  print(a)
  labeltexttime.config(text=a)
  labeltexttime.pack()

schedule.every(1).seconds.do(reset)
schedule.run_all

window.mainloop()


#----------- 이줄 위에는 환호 --------------

import schedule
import time
import datetime

 
if first():
 schedule.run_pending
schedule.every().monday.at("8:40").do(first)
schedule.every().monday.at("8:50").do(first)

schedule.every().monday.at("8:55").do(first)
schedule.every().monday.at("9:25").do(first)

schedule.every().monday.at("9:30").do(first)
schedule.every().monday.at("10:20").do(first)

schedule.every().monday.at("10:30").do(first)
schedule.every().monday.at("11:20").do(first)

schedule.every().monday.at("11:30").do(first)
schedule.every().monday.at("12:20").do(first)

schedule.every().monday.at("13:10").do(first)
schedule.every().monday.at("14:00").do(first)

schedule.every().monday.at("14:10").do(first)
schedule.every().monday.at("15:00").do(first)

schedule.every().monday.at("15:10").do(first)
schedule.every().monday.at("16:00").do(first)
#----------------------------------------------
schedule.every().tuesday.at("8:40").do(first)
schedule.every().tuesday.at("8:50").do(first)

schedule.every().tuesday.at("8:55").do(first)
schedule.every().tuesday.at("9:25").do(first)

schedule.every().tuesday.at("9:30").do(first)
schedule.every().tuesday.at("10:20").do(first)

schedule.every().tuesday.at("10:30").do(first)
schedule.every().tuesday.at("11:20").do(first)

schedule.every().tuesday.at("11:30").do(first)
schedule.every().tuesday.at("12:20").do(first)

schedule.every().tuesday.at("13:05").do(first)
schedule.every().tuesday.at("13:55").do(first)

schedule.every().tuesday.at("14:00").do(first)
schedule.every().tuesday.at("14:50").do(first)

schedule.every().tuesday.at("12:50").do(first)
schedule.every().tuesday.at("15:10").do(first)

schedule.every().tuesday.at("15:10").do(first)
schedule.every().tuesday.at("16:20").do(first)
#----------------------------------------------
schedule.every().wednesday.at("8:40").do(first)
schedule.every().wednesday.at("8:50").do(first)

schedule.every().wednesday.at("8:55").do(first)
schedule.every().wednesday.at("9:25").do(first)

schedule.every().wednesday.at("9:30").do(first)
schedule.every().wednesday.at("10:20").do(first)

schedule.every().wednesday.at("10:30").do(first)
schedule.every().wednesday.at("11:20").do(first)

schedule.every().wednesday.at("11:30").do(first)
schedule.every().wednesday.at("12:20").do(point)

schedule.every().wednesday.at("13:10").do(point)
schedule.every().wednesday.at("14:00").do(point)

schedule.every().wednesday.at("14:10").do(point)
schedule.every().wednesday.at("15:00").do(point)

schedule.every().wednesday.at("15:10").do(point)
schedule.every().wednesday.at("16:00").do(point)
#----------------------------------------------
schedule.every().thursday.at("8:40").do(point)
schedule.every().thursday.at("8:50").do(point)

schedule.every().thursday.at("8:55").do(point)
schedule.every().thursday.at("9:25").do(point)

schedule.every().thursday.at("9:30").do(point)
schedule.every().thursday.at("10:20").do(point)

schedule.every().thursday.at("10:30").do(point)
schedule.every().thursday.at("11:20").do(point)

schedule.every().thursday.at("11:30").do(point)
schedule.every().thursday.at("12:20").do(point)

schedule.every().thursday.at("13:10").do(point)
schedule.every().thursday.at("14:00").do(point)

schedule.every().thursday.at("14:10").do(point)
schedule.every().thursday.at("15:00").do(point)

schedule.every().thursday.at("15:10").do(point)
schedule.every().thursday.at("16:00").do(point)
#-------------------------------------------------
schedule.every().friday.at("8:40").do(point)
schedule.every().friday.at("8:50").do(point)

schedule.every().friday.at("8:55").do(point)
schedule.every().friday.at("9:25").do(point)
schedule.every().friday.at("9:30").do(point)
schedule.every().friday.at("10:20").do(point)

schedule.every().friday.at("10:30").do(point)
schedule.every().friday.at("11:20").do(point)

schedule.every().friday.at("11:30").do(point)
schedule.every().friday.at("12:20").do(point)

schedule.every().friday.at("13:10").do(point)
schedule.every().friday.at("14:00").do(point)

schedule.every().friday.at("14:10").do(point)
schedule.every().friday.at("15:00").do(point)

schedule.every().friday.at("15:10").do(point)
schedule.every().friday.at("16:00").do(point)



while True:
    schedule.run_pending()
    time.sleep(1)





#------------- 이줄 위에는 주환 -------------

from playsound import playsound 
playsound ('bell1.mp3')

playsound ('bell2.mp3')

#------------- 이줄 위에는 유재 ------------


#------------- 이줄 위에는 유재 ------------

