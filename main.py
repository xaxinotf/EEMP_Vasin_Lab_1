import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

# Вхідні дані
data = {
    'Price': [1.25, 1.5, 1.8, 2.25, 2.45, 2.85, 3.3, 3.75, 4.1, 4.75, 5, 5.5],
    'Demand': [106.2, 81.4, 65.3, 61.5, 47.9, 43.7, 35.1, 34.6, 35, 25.2, 12.1, 10],
    'Supply': [7.1, 21, 30.4, 40.1, 48.6, 55.8, 65, 82.3, 90.5, 101.3, 112.5, 120]
}
df = pd.DataFrame(data)

# Функція моделі для попиту
def demand_model(x, a, b):
    return a * np.exp(b * x)

# Функція моделі для пропозиції
def supply_model(x, c, d):
    return c * np.log(x) + d

# Підгонка моделей до даних
popt_demand, pcov_demand = curve_fit(demand_model, df['Price'], df['Demand'])
popt_supply, pcov_supply = curve_fit(supply_model, df['Price'], df['Supply'])

# Генерація прогнозів для візуалізації
price_range = np.linspace(min(df['Price']), max(df['Price']), 100)
predicted_demand = demand_model(price_range, *popt_demand)
predicted_supply = supply_model(price_range, *popt_supply)

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.scatter(df['Price'], df['Demand'], label='Actual Demand', color='blue')
plt.plot(price_range, predicted_demand, label=r'Fitted Demand: $a \cdot e^{b \cdot x}$', color='blue')
plt.scatter(df['Price'], df['Supply'], label='Actual Supply', color='red')
plt.plot(price_range, predicted_supply, label=r'Fitted Supply: $c \cdot \ln(x) + d$', color='red')
plt.title('Demand and Supply Models')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.show()

# Виведення коефіцієнтів моделей
print(f"Аналітичний вигляд функції попиту: a={popt_demand[0]:.2f}, b={popt_demand[1]:.2f}")
print(f"Аналітичний вигляд функції пропозиції: c={popt_supply[0]:.2f}, d={popt_supply[1]:.2f}")
