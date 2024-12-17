import matplotlib
matplotlib.use('TkAgg')  # Or 'Qt5Agg' if you're using Qt

import matplotlib.pyplot as plt

def plot_graph(data):
    plt.plot(data)
    plt.title("Stock Predictions")
    plt.xlabel("Time (Hours)")
    plt.ylabel("Price")
    plt.show()
