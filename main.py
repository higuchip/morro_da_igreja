import pandas as pd
from datetime import datetime
import calplot
import matplotlib.pyplot as plt
import matplotlib.font_manager
import streamlit as st
from PIL import Image
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px


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

### Temperatura


fig, ax = calplot.calplot(
    temperature["Air_Temp_Avg"],
    edgecolor="black",
    cmap="PuRd",
    fillcolor="white",
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


min_temp = go.Indicator(
    mode="gauge+number",
    value=temperature["Air_Temp_Avg"].min(),
    gauge={
        "axis": {"range": [0, -10], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "red"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 33], "color": "red"},
            {"range": [33, 66], "color": "yellow"},
            {"range": [66, 100], "color": "green"},
        ],
    },
    domain={"x": [0, 0.25], "y": [0.0, 1.00]},
    title={"text": "Mínima"},
)

mean_temp = go.Indicator(
    mode="gauge+number",
    gauge={
        "axis": {"range": [0, 25], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "red"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
    },
    value=temperature["Air_Temp_Avg"].mean(),
    # number={"suffix": " oC"},
    domain={"x": [0.37, 0.62], "y": [0.0, 1]},
    title={"text": "Média"},
)

max_temp = go.Indicator(
    mode="gauge+number",
    gauge={
        "axis": {"range": [0, 25], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "red"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
    },
    value=temperature["Air_Temp_Avg"].max(),
    domain={"x": [0.71, 0.96], "y": [0.0, 1.00]},
    title={"text": "Máxima"},
)


# layout and figure production
layout = go.Layout(height=300, width=600, autosize=False)
fig_gauge_temp = go.Figure(data=[min_temp, mean_temp, max_temp], layout=layout)

# Chuva

min_rain = go.Indicator(
    mode="gauge+number",
    value=chuva["Rain_mm_Tot"].min(),
    gauge={
        "axis": {"range": [0, 10], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "blue"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
    },
    domain={"x": [0, 0.25], "y": [0.0, 1.00]},
    title={"text": "Mínima"},
)

mean_rain = go.Indicator(
    mode="gauge+number",
    gauge={
        "axis": {"range": [0, 10], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "blue"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
    },
    value=chuva["Rain_mm_Tot"].mean(),
    # number={"suffix": " oC"},
    domain={"x": [0.37, 0.62], "y": [0.0, 1]},
    title={"text": "Média"},
)

max_rain = go.Indicator(
    mode="gauge+number",
    gauge={
        "axis": {"range": [0, 300], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "blue"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
    },
    value=chuva["Rain_mm_Tot"].max(),
    domain={"x": [0.71, 0.96], "y": [0.0, 1.00]},
    title={"text": "Máxima"},
)


# layout and figure production
fig_gauge_chuva = go.Figure(data=[min_rain, mean_rain, max_rain], layout=layout)


fig1, ax = calplot.calplot(
    chuva["Rain_mm_Tot"],
    edgecolor="black",
    cmap="PuBu",
    fillcolor="white",
    dropzero=True,
    textformat="{:.0f}",
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


# Umidade do Ar

# Chuva

min_hum = go.Indicator(
    mode="gauge+number",
    value=umidade["Air_Humidity_Avg"].min(),
    gauge={
        "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "purple"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
    },
    domain={"x": [0, 0.25], "y": [0.0, 1.00]},
    title={"text": "Mínima"},
)

mean_hum = go.Indicator(
    mode="gauge+number",
    gauge={
        "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "purple"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
    },
    value=umidade["Air_Humidity_Avg"].mean(),
    # number={"suffix": " oC"},
    domain={"x": [0.37, 0.62], "y": [0.0, 1]},
    title={"text": "Média"},
)

max_hum = go.Indicator(
    mode="gauge+number",
    gauge={
        "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "darkblue"},
        "bar": {"color": "purple"},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
    },
    value=umidade["Air_Humidity_Avg"].max(),
    domain={"x": [0.71, 0.96], "y": [0.0, 1.00]},
    title={"text": "Máxima"},
)


# layout and figure production
fig_gauge_hum = go.Figure(data=[min_hum, mean_hum, max_hum], layout=layout)


fig2, ax = calplot.calplot(
    umidade["Air_Humidity_Avg"],
    edgecolor="black",
    cmap="gist_heat",
    fillcolor="white",
    dropzero=True,
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


img = Image.open("morro_igreja.jpg")

st.sidebar.title(
    "Condições Climáticas do Morro da Igreja, Parque Nacional de São Joaquim, Urubici, SC"
)

Maxi_date = umidade.index.max()
data_atualizacao = Maxi_date.strftime("%d-%m-%Y")
# text
st.sidebar.text(f"Atualizado em: {data_atualizacao }")
st.sidebar.image(img, use_column_width=True)
st.sidebar.header(
    "Projeto: Influência do clima sobre processos ecossistêmicos em Floresta Nebular"
)
st.sidebar.subheader("Parceria UDESC/ICMBio")

st.sidebar.text("Contao: higuchip@gmail.com")

st.markdown(
    "<h3 style='text-align: center; color: black;'>Temperatura Média Diária ( &#8451 )</h3>",
    unsafe_allow_html=True,
)

st.pyplot(fig)
st.plotly_chart(fig_gauge_temp)


st.markdown(
    "<h3 style='text-align: center; color: black;'>Total de Chuva Diária (mm)</h3>",
    unsafe_allow_html=True,
)
# warning
st.warning(
    "Dados de precipitação ausentes para o periodo de março de 2021 a março de 2022."
)

st.pyplot(fig1)
st.plotly_chart(fig_gauge_chuva)


st.markdown(
    "<h3 style='text-align: center; color: black;'>Umidade do Ar Média Diária (%)</h3>",
    unsafe_allow_html=True,
)
st.pyplot(fig2)
st.plotly_chart(fig_gauge_hum)
