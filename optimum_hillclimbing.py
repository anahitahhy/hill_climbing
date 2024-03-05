import random
import math

def ackley(x, y):
    a = 20
    b = 0.2
    c = 2 * math.pi
    term1 = -a * math.exp(-b * math.sqrt((x**2 + y**2) / 2))
    term2 = -math.exp((math.cos(c * x) + math.cos(c * y)) / 2)
    return term1 + term2 + a + math.exp(1)

def hill_climbing():
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    step_size = 0.1
    max_iterations = 1000
    
    for _ in range(max_iterations):
        neighbors = [(x + step_size, y), (x - step_size, y), (x, y + step_size), (x, y - step_size)]
        current_value = ackley(x, y)
        best_value = current_value
        best_neighbor = (x, y)
        
        for neighbor in neighbors:
            neighbor_value = ackley(neighbor[0], neighbor[1])
            if neighbor_value < best_value:
                best_value = neighbor_value
                best_neighbor = neighbor
        
        if best_value >= current_value:
            break
        
        x, y = best_neighbor
    
    return x, y

result = hill_climbing()
print("Optimum solution:", result)