import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

# Data
prices = np.array([1.25, 1.5, 1.8, 2.25, 2.45, 2.85, 3.3, 3.75, 4.1, 4.75, 5, 5.5])
demand = np.array([106.2, 81.4, 65.3, 61.5, 47.9, 43.7, 35.1, 34.6, 35, 25.2, 12.1, 10])
supply = np.array([7.1, 21, 30.4, 40.1, 48.6, 55.8, 65, 82.3, 90.5, 101.3, 112.5, 120])


deg = 3


demand_coeffs = np.polyfit(prices, demand, deg)
supply_coeffs = np.polyfit(prices, supply, deg)


demand_poly = Polynomial(demand_coeffs[::-1])
supply_poly = Polynomial(supply_coeffs[::-1])


plt.figure(figsize=(10, 6))
plt.scatter(prices, demand, color='blue', label='Demand Data')
plt.scatter(prices, supply, color='red', label='Supply Data')
plt.plot(np.sort(prices), demand_poly(np.sort(prices)), color='blue', linestyle='-', label='Demand Fit')
plt.plot(np.sort(prices), supply_poly(np.sort(prices)), color='red', linestyle='-', label='Supply Fit')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Supply and Demand Curve Fit')
plt.legend()
plt.show()

# Display analytical forms
print(f"Demand Function Coefficients: {demand_coeffs}")
print(f"Supply Function Coefficients: {supply_coeffs}")
