import random

import colours as colours
import pandas as pd
import turtle
import math




colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
dataset_cities = pd.read_csv('cities.csv')
# print(dataset_cities['X'][1])
# print(dataset_cities['Y'][1])


wn = turtle.Screen()  # setup screen and its attributes
tess = turtle.Turtle()  # sets tess
wn.title("Path Optimiser")
tess.speed(1000)
tess.setpos(0, 0)




for ite in range(100000):
  print("Latitude: %f"  %dataset_cities['X'][ite])
  print("Longitude: %f"  %dataset_cities['Y'][ite])
  tess.setpos(dataset_cities['X'][ite]/10 - 200,dataset_cities['Y'][ite]/10 - 200)
  tess.color(random.choice(colours))
  tess.dot(10)

wn.exitonclick()






