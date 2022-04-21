from calendar import TUESDAY
from cgitb import text

from tkinter import *

from operator import truediv
from re import A
from tkinter import *

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
    
p1() #음악 1 재생 함수

def p2():
    mixer.music.load("bell2.mp3") #음악 2 재생
    mixer.music.play()
    time.sleep(13)
    mixer.music.stop()

p2() #음악 2 재생 함수



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



window.mainloop()



def job():
    print("스케쥴 실행중...")

if "exam"():
    schedule.every().at("20:18").do(job)
 
while True:
    schedule.run_pending()
    time.sleep(1)

