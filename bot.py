import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_signals(prices):
    signals = []
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            signals.append("BUY")
        elif prices[i] < prices[i-1]:
            signals.append("SELL")
        else:
            signals.append("HOLD")
    return signals

if __name__ == "__main__":
    prices = [100, 101, 102, 100, 99, 101]
    signals = generate_signals(prices)
    print(list(zip(prices[1:], signals)))
