import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
import os


def save_seaborn_plot(df, x, y, hue, title, save_path):
    """
    Save seaborn plot to save_path
    """
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y=y, hue=hue, data=df)
    plt.title(title)
    plt.savefig(save_path)
    plt.close()


def save_px_plot(df, x, y, title, save_path):
    """
    Save plotly express plot to save_path
    """
    fig = px.bar(df, x=x, y=y, title=title)
    fig.write_image(save_path)
