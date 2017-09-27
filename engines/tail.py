
# coding: utf-8
__author__ = 'Geoffrey Nyaga'

import sys
sys.path.append('../')
from API.db_API import write_to_db,read_from_db
from API.wingAPI import wingDimensions


import numpy as np
from math import pi,sqrt
import matplotlib.pyplot as plt


Sref =  read_from_db('S')*10.76 #ft^2
Cref = read_from_db('meanGeometricChord') #ft   #Shit is confusing, do i use MGC or Cref?????
bref = read_from_db('wingSpan')

VHT = 0.75
ConeRadius1 = 1.5 #ft
ConeRadius2 = 0.5 #ft


##DIMENSIONING

HtailAR = 4
HtailTaper = 0.8

#INITIAL TAIL SIZING CONSIDERING H.TAIL ONLY - GUDMUNDSSON

#Optimim tail Arm
# HtailArm = sqrt ((2*VHT*Sref*Cref)/(pi*(ConeRadius1+ConeRadius2)))
# Swet = pi*(ConeRadius1+ConeRadius2)*HtailArm + (2*VHT*Sref*Cref/HtailArm)
# print (HtailArm,"ft is the Tail Arm for the VHT input of", VHT,"ft")
# print (Swet, "ft^2 is the correponding wetted area")


# # In[57]:

# HtailArea = ((VHT*Sref*Cref)/HtailArm)
# HtailWingspan = sqrt(HtailAR*HtailArea)
# HtailCavg = HtailWingspan/HtailAR


# # In[58]:

# print (HtailArea,"ft^2 Horizontal Tail Area")
# print (HtailWingspan,"ft Horizontal Tail wingspan")
# print (HtailCavg,"ft Horizontal Tail average chord")


# # In[59]:

# def SurfaceAreavsTailArm():
#         tailArm = np.arange(2,20)#THIS WILL CHANGE FIR DRONES AND COMMERCIAL JETS
#         tailArea = (VHT*Sref*Cref/tailArm)
        
#         coneArea = np.pi*(ConeRadius1+ConeRadius2)*tailArm
#         Swet = coneArea+(2*tailArea)
        
#         a= min(Swet)
#         b = np.argmin(Swet)
#         c = tailArm[b]
        
        
#         plt.subplot(2,1,2)
    
#         plt.axhline(a)
#         plt.axvline(c)
        
#         plt.plot(tailArm,tailArea)
#         plt.plot(tailArm,coneArea)
#         plt.plot(tailArm,Swet)
        
#         plt.subplot(2,2,1)
        
#         vht = np.arange(0.4,1,0.1)
#         for i in vht:
#             tailArea = i*Sref*Cref / tailArm
#             plt.plot(tailArm,tailArea)
#             plt.plot(tailArm,coneArea)            
                      
                       
#         plt.subplot(2,2,2)
        
#         vht = np.arange(0.4,1,0.1)
#         # print("these are the minimum wetted areas on the second graph on the right. More visualization coming soon")   
#         for i in vht:
#             tailArea = i*Sref*Cref / tailArm         
#             Swet1 = np.array(coneArea+(2*tailArea))
#             #a = np.asarray([min(Swet1)])
#             a = (min(Swet1))
                       
#             # print(a)  
#             plt.plot(tailArm,Swet1)
#             #plt.scatter(tailArm,a)
            
#         # plt.show()     
        
# SurfaceAreavsTailArm()

# #INITIAL TAIL SIZING OPTIMIZATION CONSIDERING V.TAIL ONLY - GUDMUNDSSON

Vvt = 0.040
VtailAR = 1.4
VtailTaper = .5


# VtailArm = sqrt((Vvt*Sref*bref)/(pi*(ConeRadius1+ConeRadius2)))
# print(VtailArm,"ft Optimum V.Tail arm")


# if HtailArm >= VtailArm:
#     VtailArea = (Vvt * Sref * bref) / HtailArm
# else:
#     VtailArea = (Vvt * Sref * bref) / VtailArm
# print (VtailArea,"ft^2 VTail area")


# VtailWingspan = sqrt(VtailAR * VtailArea)
# VtailCavg = VtailWingspan/VtailAR

# print (VtailWingspan,"ft VTail wingspan")
# print (VtailCavg,"ft VTail average chord")

#INITIAL TAIL SIZING OPTIMIZATION CONSIDERING H.TAIL and V.TAIL  - GUDMUNDSSON


tailArm = sqrt ( (2*Sref*(VHT*Cref + Vvt*bref))/(pi*(ConeRadius1+ConeRadius2)) )
Sht = (VHT*Sref*Cref )/ tailArm   
Svt = (Vvt*Sref*bref )/ tailArm      
HtailWingspan = sqrt(HtailAR*Sht)
VtailWingspan = sqrt(VtailAR * Svt)
HtailCavg = HtailWingspan/HtailAR
HtailCroot = 2*HtailCavg/(1+HtailTaper)
HtailCtip = HtailTaper * HtailCroot
VtailCavg = VtailWingspan/VtailAR
VtailCroot = 2*VtailCavg/(1+VtailTaper)
VtailCtip = VtailTaper * VtailCroot
print (tailArm,"tailArm")
print (Sht,"Sht")
print(Svt,'svt')
print(HtailWingspan,"HtailWingspan")
print(VtailWingspan,"VtailWingspan")
print(HtailCavg,"HtailCavg")
print(HtailCroot,"HtailCroot")

print(HtailCtip,"HtailCtip")

print(VtailCroot,"VtailCroot")
print(VtailCtip,"VtailCtip")
print(VtailCavg,"VtailCavg")

# def combined():

#     VHT = Sht*lt / (Sref*Cref)
#     Vvt = Svt *lt /(Sref*bref)

#     Sf = pi*(ConeRadius1+ConeRadius2)*lt

#     Swet = Sf + (2*Sht)+(s*Svt)