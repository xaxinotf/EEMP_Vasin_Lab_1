import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# дані
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

# Функція для знаходження ціни на основі кількості з функції попиту
def find_price_from_demand(Q):
    return fsolve(lambda P: demand_model(P) - Q, 0)[0]

# Функція для знаходження рівноваги
def equilibrium(p):
    return demand_model(p) - supply_model(p)

# Знаходження оригінальної ціни рівноваги
initial_guess = 2.0
price_eq = fsolve(equilibrium, initial_guess)[0]
quantity_eq = demand_model(price_eq)

# Встановлення квоти і розрахунок нових цін
Q_L = 0.5  # Обмеження попиту на обсяг іноземних товарів
P_L = 2.386183  # Задана ціна виробника після введення податку
P_L_star = find_price_from_demand(Q_L)  # Ціна споживача після введення квоти
t = P_L_star - P_L  # Еквівалентний податок


price_range = np.linspace(1, 6, 100)
plt.figure(figsize=(10, 6))
plt.plot(price_range, demand_model(price_range), label='Demand', color='blue')
plt.plot(price_range, supply_model(price_range), label='Supply', color='orange')
plt.axvline(x=Q_L, color='yellow', linestyle='--', label='Quota (Q_L)')
plt.scatter([P_L_star], [Q_L], color='purple', label='New Consumer Price (with Quota)')
plt.scatter([P_L], [Q_L], color='green', label='New Producer Price (with Tax)')

# Показати на графіку лінію пропозиції після введення податку
supply_after_tax = [s + t for s in supply_model(price_range)]
plt.plot(price_range, supply_after_tax, label='Supply after Tax', color='grey', linestyle='--')

plt.title('Market Equilibrium with Quota and Equivalent Tax')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.show()

# Виведення результатів
print(f"Original Equilibrium Price: ${price_eq:.2f}, Quantity: {quantity_eq:.2f}")
print(f"New Equilibrium with Quota - Consumer Price: ${P_L_star:.2f}, Quantity: {Q_L}")
print(f"New Equilibrium with Tax - Producer Price: ${P_L:.2f}, Quantity: {Q_L}")
print(f"Equivalent Tax: ${t:.7f}, Expected Tax: 0.2545986")
