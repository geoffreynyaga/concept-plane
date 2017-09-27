# coding: utf-8
__author__ = 'Geoffrey Nyaga'

import sys
sys.path.append('../')
from API.db_API import write_to_db, read_from_db




# import math

# knp = .8

# P = 250  #hp

# np = .7

# ARp = 8

# rhoAlt = .592 #kg/m3

# CLp = .3

# cruiseSpeed = 130 #knots

# tipspeed = 270 #m/s


# # dp = knp * math.sqrt((2*P*np*ARp)/(rhoAlt*Vav**2*CLp*VC))

# dp = knp * math.sqrt((2*P*745.7*np*ARp)/(0.592*(.7*tipspeed)**2*CLp*(cruiseSpeed*0.514)))

# print(dp)



# import webview
# webview.create_window("It works, Jim!", "http://geoffreynyaga.com")


# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np


# fig = plt.figure(figsize = (6,6), facecolor = 'white')
# ax = fig.add_axes( [0,0,1,1], frameon = False , aspect = 1)

# n = 50
# size_min = 50
# size_max = 50*50

# P = np.random.uniform(0,1,(n,2))

# C = np.ones((n,4)) * (0,0,0,1)
# C[:,3] = np.linspace (0,1,n)

# S = np.linspace(size_min,size_max ,n)
# scat = ax.scatter(P[:,0], P[:,1], s=S, lw=0.5, edgecolors=C, facecolor = 'None')

# ax.set_xlim(0,1) , ax.set_xticks([])
# ax.set_ylim(0,1) , ax.set_yticks([])

# def update(frame):
# 	global P, C, S

# 	C[:,3] = np.maximum(0,C[:,3] - 1.0/n)
# 	S += (size_max - size_min)/n
# 	i = frame % 50
# 	P[i]  = np.random.uniform(0,1,2)
# 	S[i] = size_min
# 	C[i,3] = 1

# 	scat.set_edgecolors(C)
# 	scat.set_sizes(S)
# 	scat.set_offsets(P)

# 	return scat,

# animation = FuncAnimation(fig,update, interval=10 , blit = True , frames = 200)
# plt.show()

# fig = plt.figure()

# ax1 = fig.add_subplot(2,2,1)
# ax1.plot([1,2,3,4,5], [10,5,10,5,10], 'r-')

# ax2 = fig.add_subplot(222)
# ax2.plot([1,2,3,4], [1,4,9,16], 'k-')

# ax3 = fig.add_subplot(223)
# ax3.plot([1,2,3,4], [1,10,100,1000], 'b-')

# ax4 = fig.add_subplot(224)
# ax4.plot([1,2,3,4], [0,0,1,1], 'g-')


# # plt.tight_layout()
# plt.show()



# def subplots():
#     nrows = 4
#     fig, axes = plt.subplots(nrows, 2)

#     for row in axes:
#       x = np.random.normal(0, 1, 100).cumsum()
#       y = np.random.normal(0, 0.5, 100).cumsum()
#       plot(row,x, y)

#     plt.show()

# def plot(axrow, x, y):
#     axrow[0].plot(x, color='red')
#     axrow[1].plot(y, color='green')

# subplots()

# plt.scatter(np.linspace(30, 200, 3), np.random.randn(3))
# import PyQt4

# pyuic5 -x example.ui -o example.py


# dict = {'name':'Zara','Age': 7,'class':'first'}
# dict['Age']= 8

# dict['hair'] = "long"
# print((dict)
# a=(dict['Age'])
# print((a*2)

# mydict = {}
# from values import prerequisites
# AR = prerequisites['AR'] * 2
# print((prerequisites['AR'],"print( test")
# test1 = 2.0
# test2 = 2

# mydict = {} #'initialising" the an empty dictionary to be used locally in the function below
# def writeToValues(name):
# 	# mydict = {}
#     fileName = os.path.splitext(os.path.basename(sys.argv[0]))[0]
#     valueprint(=open("values.py","a")
#     def namestr(obj,namespace):
#         return[name for name in namespace if namespace[name] is obj]
#     b = namestr(name, globals())
#     c = "".join(str(x) for x in b)
#     mydict[(c)] = name
#     valueprint(.write(fileName)
#     valueprint(.write("=")
#     valueprint(.write(str(mydict))
#     valueprint(.write("\n")
#     valueprint(.close()
#     return mydict

# writeToValues(test1)
# writeToValues(test2)



# print((mydict,"this is my dict")
# x= 2
# y=20
# z=x+y
#
# def mul():
#         z = x+y
#         return z
#
# answer = mul()
# print((answer)
#
# class Hero:
#
#     def __init__ (self,names):
#
#         self.name=names
#         self.health=100
#
#     def eat(self,food):
#         if (food == 'apple'):
#             self.health -= 100
#         elif (food=='ham'):
#             self.health += 20
#
# Bob = Hero('Bob')
# print( (Bob.name)
# print( (Bob.health)
# Bob.eat('apple')
# print( (Bob.health)
# Bob.eat('ham')
# print( (Bob.health)
# print((z)
#
# class Employee:
#     raise_amount = 1.05
#
#     def __init__ (self,first,last,pay):
#         self.first = first
#         self.last= last
#         self.pay = pay
#
#     def fullname(self):
#
#         return '{} {}'.format(self.first , self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay*self.raise_amount)
#
#
# emp_1 = Employee('Geoffrey','Nyaga', 5000)
#
# print((emp_1.first)
# print((emp_1.last)
# print((emp_1.raise_amount)
# print((emp_1.fullname())
#
# x=np.arange(100)
# f=np.arange(100)
# g=(np.sin(x))*100
# idx = np.argwhere(np.diff(np.sign(f-g))!=0).reshape(-1)+0
# plt.axvline(x=6)
# plt.plot(x,g)
# plt.plot(x,f)
# plt.plot(x[idx], f[idx], 'ro')
# d = x[idx]
# print((d)
# plt.show()
#
#
# #finding the minimum value in array and its index
# #a = np.array([2,5,5,1])
# #b= np.argmin(a)
# #print( (b)
# #c= a[b]
# #print((c)
#
#
# a= np.array([6,2,3,4])
# b=np.argmin(a)
# c=([1,2.3,4])
# d=c[b]
# print((b)
# print((d)
#
# def is_even(i):
#     print( ("inside is even")
#     return i%2 == 0
# is_even(4)
#
#
#
# def func_a():
#     print( ('inside func_a')
#
# def func_b(y):
#     print( ('inside func_b')
#     return y
#
# def func_c(z):
#     print( ('inside func_c')
#     return z
#
# print( (func_a())
#
# print( ('\n')
#
# print( (5+func_b(2))
#
# print( ('\n')
#
# print( (func_c(func_a))
#
# def g(x):
#     def h():
#         x = "abc"
#     x = x+1
#     print(("g: x = ", x)
#     h()
#     return x
# x = 3
# z = g(x)
#
#
# x = 1
# y = 2
# x = y
# y = x
# print( (x)
# print( (y)
# print(("\n")
# x = 1
# y = 2
# temp = x
# x=y
# y=temp
# print( (x)
# print( (y)
# print(("\n")
# x = 1
# y = 2
# (x,y)=(y,x)
# print( (x)
# print( (y)
# print(("\n")

# x = [1,2,3,4,5]
# f = [2,4,6,8,10]
# g = [10,8,6,4,2]
# h = [(x[i], f[i]) for i,_ in enumerate(zip(f,g)) if f[i] == g[i]]

# print((h)



#
# intersections.py
#
# Python for finding line intersections
#   intended to be easily adaptable for line-segment intersections
#

# from scipy.optimize import fsolve
# import pylab
# import numpy

# def findIntersection(fun1,fun2,x0):
#  return fsolve(lambda x : fun1(x) - fun2(x),x0)

# result = findIntersection(numpy.sin,numpy.cos,0.0)
# x = numpy.linspace(-2,2,50)
# pylab.plot(x,numpy.sin(x),x,numpy.cos(x),result,numpy.sin(result),'ro')
# pylab.show()

# import numpy as np
# import matplotlib.pyplot as plt

# xs = np.linspace(-np.pi, np.pi, 30)
# ys = np.sin(xs)
# markers_on = [1, 17, 18, 19]
# plt.plot(xs, ys, '-gD', markevery=markers_on)
# plt.show()