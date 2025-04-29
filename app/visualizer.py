import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(df):
    fig, ax = plt.subplots()
    ax.hist(df['value'], bins=50)
    ax.set_xlabel('Значение')
    ax.set_ylabel('Частота')
    return fig

def plot_sorted(df):
    fig, ax = plt.subplots()
    ax.plot(np.sort(df['value'].values))
    ax.set_xlabel('Индекс')
    ax.set_ylabel('Значение')
    return fig
