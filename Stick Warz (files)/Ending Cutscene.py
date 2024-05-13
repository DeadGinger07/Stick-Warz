import tkinter
import tkinter as tk
import pygame
import moviepy
import proglog
proglog.notebook()
# Import everything needed to edit video clips 
from moviepy.editor import *
  
# loading video dsa gfg intro video 
clip = VideoFileClip("Ending.mp4") 
  
# showing clip 
clip.ipython_display(width = 280, height = 320) 
clip.preview(fps = 30)
