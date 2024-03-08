import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Дані
data = {
    'Price': [1.25, 1.5, 1.8, 2.25, 2.45, 2.85, 3.3, 3.75, 4.1, 4.75, 5, 5.5],
    'Demand': [106.2, 81.4, 65.3, 61.5, 47.9, 43.7, 35.1, 34.6, 35, 25.2, 12.1, 10],
    'Supply': [7.1, 21, 30.4, 40.1, 48.6, 55.8, 65, 82.3, 90.5, 101.3, 112.5, 120]
}

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

# Визначення початкових та кінцевих значень для розрахунку дугової еластичності
Q0, Qn = data['Demand'][0], data['Demand'][-1]
P0, Pn = data['Price'][0], data['Price'][-1]
Q_сер, P_сер = (Q0 + Qn) / 2, (P0 + Pn) / 2

# Розрахунок дугової еластичності для попиту
arc_elasticity_demand = ((Qn - Q0) / (Pn - P0)) * (P_сер / Q_сер)

# Розрахунок дугової еластичності для пропозиції
S0, Sn = data['Supply'][0], data['Supply'][-1]
arc_elasticity_supply = ((Sn - S0) / (Pn - P0)) * (P_сер / Q_сер)


price_range = np.linspace(data['Price'][0], data['Price'][-1], 100)
plt.figure(figsize=(10, 6))
plt.plot(price_range, demand_model(price_range), label='Demand', color='blue')
plt.plot(price_range, supply_model(price_range), label='Supply', color='red')
plt.scatter([price_eq], [quantity_eq], color='green', zorder=5, label=f'Equilibrium: (${price_eq:.2f}, {quantity_eq:.2f})')
plt.title('Market Equilibrium and Arc Elasticities')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.show()

# рез
print(f"Equilibrium Price: ${price_eq:.2f}, Quantity: {quantity_eq:.2f}")
print(f"Arc Elasticity of Demand: {arc_elasticity_demand:.2f}")
print(f"Arc Elasticity of Supply: {arc_elasticity_supply:.2f}")
