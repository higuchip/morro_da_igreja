import pandas as pd
from datetime import datetime
import calplot

# Importacao clima

# Assign the filename: file
file = "CR1000XSeries_Sensors.dat"

# Read the file into a DataFrame: df
df = pd.read_csv(
    file,
    header=1,
    skiprows=[2, 3],
    na_values=("NAN", "NaN"),
    parse_dates=True,
    index_col="TIMESTAMP",
)

df_clean = df.dropna()
df_clean

temperature = (
    df_clean[["Air_Temp_Avg"]]
    .resample("1D")
    .mean()
    .loc[
        "2020-02-08 12:00:00":,
    ]
)

chuva = (
    df_clean[["Rain_mm_Tot"]]
    .resample("1D")
    .sum()
    .loc[
        "2020-02-08 12:00:00":,
    ]
)

umidade = (
    df_clean[["Air_Humidity_Avg"]]
    .resample("1D")
    .mean()
    .loc[
        "2020-02-08 12:00:00":,
    ]
)

print(chuva)


calplot.calplot(
    temperature["Air_Temp_Avg"],
    edgecolor="black",
    cmap="PuRd",
    suptitle="Temperatura Média Diaria (Celsius) - Morro da Igreja",
    daylabels=["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"],
    monthlabels=[
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dec",
    ],
)
