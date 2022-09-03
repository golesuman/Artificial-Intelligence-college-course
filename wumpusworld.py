#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:31:59 2022

@author: rakeshkumarbachchan
"""

import random
import matplotlib.pyplot as plt
from random import randint
from time import sleep
import matplotlib.image as mpimg
import matplotlib.offsetbox as plt1

def main(state):
    var=0
    while(True):
        status = random.randint(0,1)
        x=check(status)
        if x==0:
            print('Status code is',status,'Location is Clean')
            if state=='A' or state=='a':
                print("Your location is clean. Move to Location", location(state),".")
                view(state, status)
                sleep(5)
                state=location(state)
            elif state=='B' or state=='b':
                print("Your location is clean. Move to Location", location(state),".")
                view(state, status)
                sleep(5)
                state=location(state)
            else:
                print("Invalid Location. Try Again!")
                break
        else:
            print('Status code is',status,'Hence Location is Dirty')
            if state=='A' or state=='a':
                print("Pick up dirt and recheck the status of location", state,".")
                view(state, status)
                sleep(5)
            elif state=='B' or state=='b':
                print("Pick up dirt and recheck the status of location", state,".")
                view(state, status)
                sleep(5)
            else:
                print("Invalid Location. Try Again!")
                break
        var+=1
        if var>=10:
            print("Moving to sleep mode.")
            sleep(60)
            state=location(state)
            print("Machine awake. Checking status of location ",location(state),".")
            main(state)

            


def check(s):
    if s==0:
        return 0
    else:
        return 1

    

def location(l):
    if l=='A' or l=='a':
        return 'B'
    elif l=='B' or l=='b':
        return 'A'
    else:
        print("Invalid location terminating task.")
        exit(0)
        
        
        
def view(state, status):
    img=mpimg.imread('/home/suman/Documents/AI lab/Artificial-Intelligence-college-course/agents.png')
    fig, a = plt.subplots()
    plt.plot((0,0),(0,1000),'-o')
    plt.plot((0,1000),(1000,1000),'-o')
    plt.plot((1000,1000),(1000,0),'-o')
    plt.plot((1000,0),(0,0),'-o')
    plt.text(100,900,"A")

    plt.plot((1000,2000),(0,0),'-o')
    plt.plot((2000,2000),(0,1000),'-o')
    plt.plot((2000,1000),(1000,1000),'-o')
    plt.text(1100,900,"B")
    
    
    a.set_xlim([0, 2000])
    a.set_ylim([0, 1000])
    xy1=[500,500]
    xy2=[1500,500]

    a_img=plt1.OffsetImage(img, zoom=0.40)
    
    if state=='A' or state=='a':
        agent=plt1.AnnotationBbox(a_img, xy1)
        if status==1:
            plt.plot((200,200),(100,100),'-*')
            plt.plot((300,300),(100,100),'-*')
            plt.plot((400,400),(100,100),'-*')
            plt.plot((500,500),(100,100),'-*')
            plt.plot((600,600),(100,100),'-*')
            plt.plot((700,700),(100,100),'-*')
    else:
        agent=plt1.AnnotationBbox(a_img, xy2)
        if status==1:
            plt.plot((1200,1200),(100,100),'-*')
            plt.plot((1300,1300),(100,100),'-*')
            plt.plot((1400,1400),(100,100),'-*')
            plt.plot((1500,1500),(100,100),'-*')
            plt.plot((1600,1600),(100,100),'-*')
            plt.plot((1700,1700),(100,100),'-*')
    
    a.add_artist(agent)

    plt.show()
    


state=input("Enter your location(A/B): ")
main(state)
