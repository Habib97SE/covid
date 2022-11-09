import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def read_excel_tab_data(file_path: str, sheet_name: str) -> pd.DataFrame:
    """ 
    Read excel tab data
    param file_path: excel file path
    param sheet_name: excel sheet name
    return: pandas dataframe
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df


def plot_bar_chart(df: pd.DataFrame, x: str, y: str, title: str, file_path: str) -> None:
    """ 
    Plot bar chart
    param df: pandas dataframe
    param x: x axis
    param y: y axis
    param title: chart title
    param file_path: file path to save chart
    """
    sns.set(style="whitegrid")
    ax = sns.barplot(x=x, y=y, data=df)
    ax.set_title(title)
    # save chart as png in output directory
    plt.savefig(os.path.join(file_path, title + '.png'))


file_path = os.path.join(
    os.getcwd(), 'data', 'Folkhalsomyndigheten_Covid19.xlsx')

df_covid_19 = read_excel_tab_data(file_path, 'Veckodata Riket')


# merge two columms into one
df_covid_19["datum"] = df_covid_19["år"].astype(
    str) + "v" + df_covid_19["veckonummer"].astype(str)

# drop the two columns
df_covid_19 = df_covid_19.drop(["år", "veckonummer"], axis=1)

# set the index to the new column
df_covid_19 = df_covid_19.set_index("datum")


# sort the dataframe by Antal_avlidna_milj_inv_vecka by descending order
df_covid_19 = df_covid_19.sort_values(
    by="Antal_avlidna_vecka", ascending=False)

# plot bar chart Antal_avlidna_vecka
plot_bar_chart(df_covid_19, "datum", "Antal_avlidna_vecka",
               "Deaths by week", "Antal_avlidna_vecka")

# plot bar chart Antal_fall_vecka
plot_bar_chart(df_covid_19, "datum", "Antal_fall_vecka",
               "Cases by week", "Antal_fall_vecka")
