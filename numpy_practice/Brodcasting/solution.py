import numpy as np

prices = np.array([100, 200, 300])
# discounts = np.array([0.1, 0.2, 0.3])
discounts = 10
final_prices = prices - (prices * discounts / 100)
print(final_prices)