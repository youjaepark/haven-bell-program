from calendar import TUESDAY
from cgitb import text
from tkinter import *
import threading
from operator import truediv
from re import A
from tracemalloc import start
import tkinter.font
from xml.dom import pulldom
import schedule
import time
import datetime
from pygame import mixer
import time



mixer.init()

def p1():
    mixer.music.load("bell1.mp3") #음악 1 재생
    mixer.music.play()
    time.sleep(9)
    mixer.music.stop()
    
 #음악 1 재생 함수

def p2():
    mixer.music.load("bell2.mp3") #음악 2 재생
    mixer.music.play()
    time.sleep(13)
    mixer.music.stop()

 #음악 2 재생 함수



window = Tk()
window.title("School Bell")
window.geometry('800x600')

point = "normal"

font=tkinter.font.Font(family="맑은 고딕", size=25, slant="italic")
labeltext = Label(window, text = "평일 벨소리", font=font)
labeltext.pack(side="top", pady=30)


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
  


btn1 = Button(window, text="평일 벨소리", width=30, height=15, command=first)
btn1.pack(side="left", padx=50)


btn2 = Button(window, text="시험 벨소리", width=30, height=15, command= second)
btn2.pack(side="right", padx=50)


btn2 = Button(window, text="시험 벨소리", width=30, height=15, command=second)
btn2.pack(side="right", padx=50)


import schedule
import time
import datetime

schedule.every().monday.at("08:40").do(p1)
schedule.every().monday.at("08:50").do(p2)

schedule.every().monday.at("08:55").do(p1)
schedule.every().monday.at("09:25").do(p2)

schedule.every().monday.at("09:30").do(p1)
schedule.every().monday.at("10:20").do(p2)

schedule.every().monday.at("10:30").do(p1)
schedule.every().monday.at("11:20").do(p2)

schedule.every().monday.at("11:30").do(p1)
schedule.every().monday.at("12:20").do(p2)

schedule.every().monday.at("13:10").do(p1)
schedule.every().monday.at("14:00").do(p2)

schedule.every().monday.at("14:10").do(p1)
schedule.every().monday.at("15:00").do(p2)

schedule.every().monday.at("15:10").do(p1)
schedule.every().monday.at("16:00").do(p2)

#----------------------------------------------
schedule.every().tuesday.at("08:40").do(p1)
schedule.every().tuesday.at("08:50").do(p2)

schedule.every().tuesday.at("08:55").do(p1)
schedule.every().tuesday.at("09:25").do(p2)

schedule.every().tuesday.at("09:30").do(p1)
schedule.every().tuesday.at("10:20").do(p2)

schedule.every().tuesday.at("10:30").do(p1)
schedule.every().tuesday.at("11:20").do(p2)

schedule.every().tuesday.at("11:30").do(p1)
schedule.every().tuesday.at("12:20").do(p2)

schedule.every().tuesday.at("13:36").do(p1)
schedule.every().tuesday.at("13:37").do(p2)

schedule.every().tuesday.at("14:00").do(p1)
schedule.every().tuesday.at("14:50").do(p2)

schedule.every().tuesday.at("12:50").do(p1)
schedule.every().tuesday.at("15:10").do(p2)

schedule.every().tuesday.at("15:10").do(p1)
schedule.every().tuesday.at("16:20").do(p2)
#----------------------------------------------
schedule.every().wednesday.at("08:40").do(p1)
schedule.every().wednesday.at("08:50").do(p2)

schedule.every().wednesday.at("08:55").do(p1)
schedule.every().wednesday.at("09:25").do(p2)

schedule.every().wednesday.at("09:30").do(p1)
schedule.every().wednesday.at("10:20").do(p2)

schedule.every().wednesday.at("10:30").do(p1)
schedule.every().wednesday.at("11:20").do(p2)

schedule.every().wednesday.at("11:30").do(p1)
schedule.every().wednesday.at("12:20").do(p2)

schedule.every().wednesday.at("13:10").do(p1)
schedule.every().wednesday.at("14:00").do(p2)

schedule.every().wednesday.at("14:10").do(p1)
schedule.every().wednesday.at("15:00").do(p2)

schedule.every().wednesday.at("15:10").do(p1)
schedule.every().wednesday.at("16:00").do(p2)
#----------------------------------------------
schedule.every().thursday.at("08:40").do(p1)
schedule.every().thursday.at("08:50").do(p2)

schedule.every().thursday.at("08:55").do(p1)
schedule.every().thursday.at("09:25").do(p2)

schedule.every().thursday.at("09:30").do(p1)
schedule.every().thursday.at("10:20").do(p2)

schedule.every().thursday.at("10:30").do(p1)
schedule.every().thursday.at("11:20").do(p2)

schedule.every().thursday.at("11:30").do(p1)
schedule.every().thursday.at("12:20").do(p2)

schedule.every().thursday.at("13:10").do(p1)
schedule.every().thursday.at("14:00").do(p2)

schedule.every().thursday.at("14:10").do(p1)
schedule.every().thursday.at("15:00").do(p2)

schedule.every().thursday.at("15:10").do(p1)
schedule.every().thursday.at("16:00").do(p2)
#-------------------------------------------------
schedule.every().friday.at("08:40").do(p1)
schedule.every().friday.at("08:50").do(p2)

schedule.every().friday.at("08:55").do(p1)
schedule.every().friday.at("09:25").do(p2)

schedule.every().friday.at("09:30").do(p1)
schedule.every().friday.at("10:20").do(p2)

schedule.every().friday.at("10:30").do(p1)
schedule.every().friday.at("11:20").do(p2)

schedule.every().friday.at("11:30").do(p1)
schedule.every().friday.at("12:20").do(p2)

schedule.every().friday.at("13:10").do(p1)
schedule.every().friday.at("14:00").do(p2)

schedule.every().friday.at("14:10").do(p1)
schedule.every().friday.at("15:00").do(p2)

schedule.every().friday.at("15:10").do(p1)
schedule.every().friday.at("16:00").do(p2)

class alpha:

    def window_mainloop():
    window.mainloop()

    def schedule_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

t1= threading.Thread(target=window_mainloop)
t2= threading.Thread(target=schedule_loop)

t1.start()
t2.start()

t1.join()
t2.join()