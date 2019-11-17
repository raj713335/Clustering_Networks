import sys
import os
import time
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter.ttk as ttk


#OPTION SELECT GUI CREATION

class CLUSTRING_NETWORK_GUI():

    #OPTION SELECT POP UP CREATION

    def __init__(self, win):



        self.lbl = Label(win, text="DIMENSION", font=("Helvetica", 25, 'bold'), bg='white')
        self.lbl.place(x=300, y=20)

        self.lb2 = Label(win, text="X-AXIS", font=("Helvetica", 25, 'bold'), bg='white')
        self.lb2.place(x=20, y=100)

        self.x_axis = ttk.Entry(win, text="X-AXIS", font=("Helvetica", 25, 'bold'))
        self.x_axis.place(x=140, y=100,width=240)

        self.lb3 = Label(win, text="Y-AXIS", font=("Helvetica", 25, 'bold'), bg='white')
        self.lb3.place(x=400, y=100)

        self.y_axis = ttk.Entry(win, text="Y-AXIS", font=("Helvetica", 25, 'bold'))
        self.y_axis.place(x=520, y=100, width=240)

        self.lb4 = Label(win, text="NUMBER OF NODES", font=("Helvetica", 25, 'bold'), bg='white')
        self.lb4.place(x=20, y=180)

        self.nodes = ttk.Entry(win, text="NODES", font=("Helvetica", 25, 'bold'))
        self.nodes.place(x=360, y=180, width=400)

        self.lb4 = Label(win, text="CLUSTERS", font=("Helvetica", 25, 'bold'), bg='white')
        self.lb4.place(x=20, y=260)

        self.cluster = ttk.Entry(win, text="CLUSTER", font=("Helvetica", 25, 'bold'))
        self.cluster.place(x=360, y=260, width=400)

        self.type_of_cluster_creation=["ARE WISE","DEFAULT"]

        self.cluster_type= Combobox(win, state="readonly",width=15, height=4, justify='center', font=("Helvetica", 25, 'bold'),
                            values=self.type_of_cluster_creation)

        self.cluster_type.place(x=20, y=340,width=350)
        self.cluster_type.set("CLUSTER TYPE")


        self.deployment_type=["RANDOM","SPIRAL","SQUARE","DEFAULT"]

        self.deployment_type = Combobox(win, state="readonly", width=15, height=4, justify='center',
                                     font=("Helvetica", 25, 'bold'),
                                     values=self.deployment_type)

        self.deployment_type.place(x=410, y=340, width=350)
        self.deployment_type.set("DEPLOYMENT TYPE")

        self.lb5 = Label(win, text="INTERVAL   (in sec)", font=("Helvetica", 25, 'bold'), bg='white')
        self.lb5.place(x=20, y=420)

        self.interval = ttk.Entry(win, text="INTERVAL", font=("Helvetica", 25, 'bold'))
        self.interval.place(x=360, y=420, width=400)


        self.b4 = ttk.Button(win, text='QUIT', command=self.quit)
        self.b4.place(x=725, y=-1)


        self.b3 = ttk.Button(win, text='START', command=self.Start_Clustering)
        self.b3.place(x=220, y=500, width=305, height=70)


    #QUIT FROM OPTION SELECT

    def quit(self):
        window.destroy()
        exit(0)

    #STORING ALL THE VALUES IN INI FILE

    def Start_Clustering(self):



        if (self.x_axis.get() == "" or self.y_axis.get() == "" or self.nodes.get() == "" or
                self.cluster.get()=="" or self.cluster_type.get()=="CLUSTER TYPE" or self.deployment_type.get()=="DEPLOYMENT TYPE"
                or self.interval.get()==""):
            messagebox.showwarning("Warning", "SELECT INFORMATION")

            return(0)


        else:





        window.destroy()
        return(indexing_header)


window=Tk()
window.iconbitmap(default='icon.ico')
option_window=CLUSTRING_NETWORK_GUI(window)
window.config(background='white')
window.attributes('-alpha', 0.9)
window.title('CLUSTERING NETWORK')
window.geometry("800x600")
#window.state("zoomed")
window.mainloop()