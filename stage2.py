import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Функції моделей для попиту та пропозиції
def demand_model(x):
    return 176.21 * np.exp(-0.477 * x)

def supply_model(x):
    return 74.826 * np.log(x) - 15.076

# Функція для знаходження рівноваги
def equilibrium(p):
    return demand_model(p) - supply_model(p)

# Початкове наближення ціни
initial_guess = 2.0

# Знаходження ціни ринкової рівноваги
price_eq = fsolve(equilibrium, initial_guess)[0]
quantity_eq = demand_model(price_eq)

# Функції нахилу попиту та пропозиції
def demand_slope(x):
    return -0.477 * 176.21 * np.exp(-0.477 * x)

def supply_slope(x):
    return 74.826 / x

# Обчислення нахилів в точці рівноваги
demand_slope_eq = demand_slope(price_eq)
supply_slope_eq = supply_slope(price_eq)

# Обчислення еластичностей для попиту та пропозиції в точці рівноваги
elasticity_demand_eq = (demand_slope_eq * price_eq) / quantity_eq
elasticity_supply_eq = (supply_slope_eq * price_eq) / quantity_eq

# Визначення стабільності рівноваги
equilibrium_stability = "стабільна рівновага" if abs(elasticity_demand_eq) > abs(elasticity_supply_eq) else "не стабільна рівновага"

# Візуалізація
price_range = np.linspace(1, 6, 100)
plt.figure(figsize=(10, 6))
plt.plot(price_range, demand_model(price_range), label='Demand', color='blue')
plt.plot(price_range, supply_model(price_range), label='Supply', color='red')
plt.scatter([price_eq], [quantity_eq], color='green', zorder=5, label=f'Equilibrium: (${price_eq:.2f}, {quantity_eq:.2f})')
plt.title('Market Equilibrium')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.show()

# Виведення результатів
print(f"Equilibrium Price: ${price_eq:.2f}, Quantity: {quantity_eq:.2f}")
print(f"Demand Slope at Equilibrium: {demand_slope_eq:.2f}, Supply Slope at Equilibrium: {supply_slope_eq:.2f}")
print(f"Demand Elasticity at Equilibrium: {elasticity_demand_eq:.2f}, Supply Elasticity at Equilibrium: {elasticity_supply_eq:.2f}")
print(f"Equilibrium is {equilibrium_stability}")
