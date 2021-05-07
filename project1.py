# water.mp3 ko play krwana hain phir uske baad mujhe usse har 30 mins ke baad chalana hain or jiss time mein vo chala usse ek file mein note krna hain
from pygame import mixer
import time
while True:
    f=open("tep.txt","a")
    mixer.init()
    mixer.music.load("BA.mp3")
    mixer.music.play()
    a=str(input("Enter the World:- "))
    if a=="stop":
        mixer.music.stop()
        b=f.write(time.strftime("%d %B %Y %H:%M:%S"))
        print(b)
        time.sleep(10)
    
    break    
     