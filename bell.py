

from cgitb import text
from tkinter import *
#from winsound import PlaySound
window = Tk()
window.title("School Bell")
window.geometry('800x600')

point = "normal"

def first(): 
    point = "normal"
    print(point)
    Label1 = Label(window, background='green')
    Label1.pack()

def second():
    point = "exam"
    print(point)
    btn1['bg'] = 'white'
    btn2['bg'] = 'green'

btn1 = Button(window, text="평일 벨소리", width=30, height=15, command=first)
btn1.pack(side="left", padx=50)

btn2 = Button(window, text="시험 벨소리", width=30, height=15, command= second)
btn2.pack(side="right", padx=50)

window.mainloop()

print ("환호가")

#----------- 이줄 위에는 환호 --------------


import schedule
import time
 
if point():
 schedule.run_pending
schedule.every().monday.at("8:40").do(point)
schedule.every().monday.at("8:50").do(point)

schedule.every().monday.at("8:55").do(point)
schedule.every().monday.at("9:25").do(point)

schedule.every().monday.at("9:30").do(point)
schedule.every().monday.at("10:20").do(point)

schedule.every().monday.at("10:30").do(point)
schedule.every().monday.at("11:20").do(point)

schedule.every().monday.at("11:30").do(point)
schedule.every().monday.at("12:20").do(point)

schedule.every().monday.at("13:10").do(point)
schedule.every().monday.at("14:00").do(point)

schedule.every().monday.at("14:10").do(point)
schedule.every().monday.at("15:00").do(point)

schedule.every().monday.at("15:10").do(point)
schedule.every().monday.at("16:00").do(point)
#----------------------------------------------
schedule.every().tuesday.at("8:40").do(point)
schedule.every().tuesday.at("8:50").do(point)

schedule.every().tuesday.at("8:55").do(point)
schedule.every().tuesday.at("9:25").do(point)

schedule.every().tuesday.at("9:30").do(point)
schedule.every().tuesday.at("10:20").do(point)

schedule.every().tuesday.at("10:30").do(point)
schedule.every().tuesday.at("11:20").do(point)

schedule.every().tuesday.at("11:30").do(point)
schedule.every().tuesday.at("12:20").do(point)

schedule.every().tuesday.at("13:05").do(point)
schedule.every().tuesday.at("13:55").do(point)

schedule.every().tuesday.at("14:00").do(point)
schedule.every().tuesday.at("14:50").do(point)

schedule.every().tuesday.at("12:50").do(point)
schedule.every().tuesday.at("15:10").do(point)

schedule.every().tuesday.at("15:10").do(point)
schedule.every().tuesday.at("16:20").do(point)
#----------------------------------------------
schedule.every().wednesday.at("8:40").do(point)
schedule.every().wednesday.at("8:50").do(point)

schedule.every().wednesday.at("8:55").do(point)
schedule.every().wednesday.at("9:25").do(point)

schedule.every().wednesday.at("9:30").do(point)
schedule.every().wednesday.at("10:20").do(point)

schedule.every().wednesday.at("10:30").do(point)
schedule.every().wednesday.at("11:20").do(point)

schedule.every().wednesday.at("11:30").do(point)
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

if second():
  schedule.run_all



while True:
    schedule.run_pending()
    time.sleep(1)






#------------- 이줄 위에는 주환 -------------

#import playsound
#playsound.playsound('sample.mp3')

#------------- 이줄 위에는 유재 ------------
