from tkinter import *
import tkinter as tk
import tkinter.font as tf
import schedule
import time
import datetime
import pygame

pygame.init()
pygame.mixer.init()

window = Tk()
window.title("헤이븐 벨소리 프로그램")
window.resizable(True, True)
window.geometry("700x700")
def openbell():
   pygame.mixer.music.load("bell1.mp3")
   pygame.mixer.music.play()
openbell()
print('test') 
window.mainloop()
