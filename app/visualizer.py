import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df['value'], bins=50)
    ax.set_xlabel('Значение')
    ax.set_ylabel('Частота')
    fig.tight_layout()
    return fig

def plot_sorted(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(np.sort(df['value'].values))
    ax.set_xlabel('Индекс')
    ax.set_ylabel('Значение')
    fig.tight_layout()
    return fig
