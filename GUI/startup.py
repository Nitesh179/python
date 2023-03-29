from tkinter import *
import json


class Startup:
    def __init__(self):
        f=open('startups.json','r')
        self.data= json.load(f)
        # print(self.data)
        self.loadGui()

    def loadGui(self):
        root=Tk()
        


obj=Startup()
