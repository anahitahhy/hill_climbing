#importing libraries
import numpy as np
from matplotlib import pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

def ackley_function(x1,x2):
  
  part_1 = -0.2*math.sqrt(0.5*(x1*x1 + x2*x2))
  part_2 = 0.5*(math.cos(2*math.pi*x1) + math.cos(2*math.pi*x2))
  value = math.exp(1) + 20 -20*math.exp(part_1) - math.exp(part_2)
  
  return value

def ackley_function_range(x_range_array):
  
  value = np.empty([len(x_range_array[0])])
  for i in range(len(x_range_array[0])):
    
    
    part_1 = -0.2*math.sqrt(0.5*(x_range_array[0][i]*x_range_array[0][i] + x_range_array[1][i]*x_range_array[1][i]))
    part_2 = 0.5*(math.cos(2*math.pi*x_range_array[0][i]) + math.cos(2*math.pi*x_range_array[1][i]))
    
    value_point = math.exp(1) + 20 -20*math.exp(part_1) - math.exp(part_2)
    value[i] = value_point
  
  return value

def plot_ackley_general():
  
  limit = 1000
  lower_limit = -5
  upper_limit = 5
  
  x1_range = [np.random.uniform(lower_limit,upper_limit) for x in range(limit)]
  x2_range = [np.random.uniform(lower_limit,upper_limit) for x in range(limit)]
  
  x_range_array = [x1_range,x2_range]
  
  z_range = ackley_function_range(x_range_array)
  
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.scatter(x1_range, x2_range, z_range, label='Ackley Function')
  
  def plot_ackley(x1_range,x2_range):
  
  x_range_array = [x1_range,x2_range]
  z_range = ackley_function_range(x_range_array)
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.scatter(x1_range, x2_range, z_range, label='Ackley Function')