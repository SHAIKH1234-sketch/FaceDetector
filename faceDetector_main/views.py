from django.shortcuts import render,redirect
from django.http import HttpResponse
import cv2
import math
import argparse
import gtts
from playsound import playsound
from .detect import *
import os
import numpy as np
def index(request):
    return render(request,'home.html')
def welcome(request):
    t1 = gtts.gTTS("welcome to Kalinga Institute of Industrial Technology, Bhubaneswar. This is gender and age detect website. click to detector to check your gender ad age.")
    # save the audio file
    t1.save("welcome.mp3")
    # play the audio file
    playsound("welcome.mp3")
    if os.path.exists("welcome.mp3"):
      os.remove("welcome.mp3")
    return render(request,'about.html')
def home(request):
    gender,age,imotion=videoCapture()
    print(gender,age,imotion)
    t1 = gtts.gTTS("Sounds Good. Your gender is {} and Age is {} years and you are {} now. I am improving myself. sorry if any mistake".format(gender,age[1:-1],imotion))
    # save the audio file
    t1.save("detection.mp3")
    # play the audio file
    playsound("detection.mp3")

    if os.path.exists("detection.mp3"):
      os.remove("detection.mp3")

    context={
    'gender':gender,
    'age':age,
    'imotion':imotion,
    }
    return render(request,'result.html',context)
