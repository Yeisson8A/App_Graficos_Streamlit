import pandas as pd
import plotly.graph_objects as go

color = "#005409"
text_color = "black"
background_color = "white"

def porcentaje_cancelacion_genero(dataset):
    # Calcula el porcentaje de churn por género
    churn_rate = dataset.groupby('gender')['Churn'].mean().reset_index()

    # Crea el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(x=churn_rate['gender'], y=churn_rate['Churn'],
                                text=churn_rate['Churn'].apply(lambda x: '{:.2%}'.format(x)),
                                textposition='auto', marker_color=color)])

    # Personaliza el diseño del gráfico
    fig.update_layout(
        title='Porcentaje de cancelación por género',
        plot_bgcolor=background_color, 
        paper_bgcolor=background_color, 
        title_font_color=text_color,
        title_x=0.4,
        margin=dict(l=80, r=80, t=80, b=80),
        xaxis_title='Género',
        yaxis_title='Porcentaje de cancelación',
        xaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
        yaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
            tickformat=".0%"
        )
    )
    return fig

def porcentaje_cancelacion_persona_mayor(dataset):
    # Calcula el porcentaje de churn por senior citizen
    churn_rate = dataset.groupby('SeniorCitizen')['Churn'].mean().reset_index()

    # Crea el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(x=churn_rate['SeniorCitizen'], y=churn_rate['Churn'],
                                text=churn_rate['Churn'].apply(lambda x: '{:.2%}'.format(x)),
                                textposition='auto', marker_color=color)])

    # Personaliza el diseño del gráfico
    fig.update_layout(
        title='Porcentaje de cancelación por situación de edad',
        plot_bgcolor=background_color, 
        paper_bgcolor=background_color, 
        title_font_color=text_color,
        title_x=0.4,
        margin=dict(l=80, r=80, t=80, b=80),
        xaxis_title='Persona mayor?',
        yaxis_title='Porcentaje de cancelación',
        xaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
            tickvals=[0, 1],
            ticktext=['No', 'Yes']
        ),
        yaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
            tickformat=".0%"
        )
    )
    return fig

def porcentaje_cancelacion_pareja(dataset):
    # Calcula el porcentaje de churn por partner
    churn_rate = dataset.groupby('Partner')['Churn'].mean().reset_index()

    # Crea el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(x=churn_rate['Partner'], y=churn_rate['Churn'],
                                text=churn_rate['Churn'].apply(lambda x: '{:.2%}'.format(x)),
                                textposition='auto', marker_color=color)])

    # Personaliza el diseño del gráfico
    fig.update_layout(
        title='Porcentaje de cancelación por situación de pareja',
        plot_bgcolor=background_color, 
        paper_bgcolor=background_color, 
        title_font_color=text_color,
        title_x=0.4,
        margin=dict(l=80, r=80, t=80, b=80),
        xaxis_title='Tiene pareja?',
        yaxis_title='Porcentaje de cancelación',
        xaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
        yaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
            tickformat=".0%"
        )
    )
    return fig

def porcentaje_cancelacion_tv_streaming(dataset):
    # Calcula el porcentaje de churn por streaming TV
    churn_rate = dataset.groupby('StreamingTV')['Churn'].mean().reset_index()

    # Crea el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(x=churn_rate['StreamingTV'], y=churn_rate['Churn'],
                                text=churn_rate['Churn'].apply(lambda x: '{:.2%}'.format(x)),
                                textposition='auto', marker_color=color)])

    # Personaliza el diseño del gráfico
    fig.update_layout(
        title='Porcentaje de cancelación por TV Streaming',
        plot_bgcolor=background_color, 
        paper_bgcolor=background_color, 
        title_font_color=text_color,
        title_x=0.4,
        margin=dict(l=80, r=80, t=80, b=80),
        xaxis_title='TV Streaming?',
        yaxis_title='Porcentaje de cancelación',
        xaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
        yaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
            tickformat=".0%"
        )
    )
    return fig

def porcentaje_cancelacion_seguridad_online(dataset):
    # Calcula el porcentaje de churn por online security
    churn_rate = dataset.groupby('OnlineSecurity')['Churn'].mean().reset_index()

    # Crea el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(x=churn_rate['OnlineSecurity'], y=churn_rate['Churn'],
                                text=churn_rate['Churn'].apply(lambda x: '{:.2%}'.format(x)),
                                textposition='auto', marker_color=color)])

    # Personaliza el diseño del gráfico
    fig.update_layout(
        title='Porcentaje de cancelación por seguridad online',
        plot_bgcolor=background_color, 
        paper_bgcolor=background_color, 
        title_font_color=text_color,
        title_x=0.4,
        margin=dict(l=80, r=80, t=80, b=80),
        xaxis_title='Seguridad Online?',
        yaxis_title='Porcentaje de cancelación',
        xaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
        yaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
            tickformat=".0%"
        )
    )
    return fig

def porcentaje_cancelacion_tipo_internet(dataset):
    # Calcula el porcentaje de churn por internet service
    churn_rate = dataset.groupby('InternetService')['Churn'].mean().reset_index()

    # Crea el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(x=churn_rate['InternetService'], y=churn_rate['Churn'],
                                text=churn_rate['Churn'].apply(lambda x: '{:.2%}'.format(x)),
                                textposition='auto', marker_color=color)])

    # Personaliza el diseño del gráfico
    fig.update_layout(
        title='Porcentaje de cancelación por tipo de internet',
        plot_bgcolor=background_color, 
        paper_bgcolor=background_color, 
        title_font_color=text_color,
        title_x=0.4,
        margin=dict(l=80, r=80, t=80, b=80),
        xaxis_title='Servicio de internet',
        yaxis_title='Porcentaje de cancelación',
        xaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
        yaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
            tickformat=".0%"
        )
    )
    return fig

def tasa_cancelacion_cargos_mensuales(dataset):
    # Crear una nueva columna en el dataset agrupando en intervalos los valores de la columna MonthlyCharges
    dataset["MonthlyChargesGroup"] = pd.cut(dataset["MonthlyCharges"], bins=[0, 30, 50, 70, 90, 110, 150])

    # Calcular el porcentaje de churn por grupo de cargos mensuales
    churn_rate = dataset.groupby('MonthlyChargesGroup')['Churn'].mean().reset_index()

    # Crear el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(x=churn_rate['MonthlyChargesGroup'].astype(str), y=churn_rate['Churn'],
                                text=churn_rate['Churn'].apply(lambda x: '{:.2%}'.format(x)),
                                textposition='auto', marker_color=color)])

    # Personalizar el diseño del gráfico
    fig.update_layout(
        title='Tasas de cancelación por cargos mensuales',
        plot_bgcolor=background_color, 
        paper_bgcolor=background_color, 
        title_font_color=text_color,
        title_x=0.4,
        margin=dict(l=80, r=80, t=80, b=80),
        xaxis_title='Grupos de cargos mensuales',
        yaxis_title='Tasa de cancelación',
        xaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
        yaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
            tickformat=".0%"
        )
    )
    return fig

def distrib_cargos_mensuales_estado(dataset):
    # Crear histogramas con Plotly
    fig = go.Figure()

    # Histograma para clientes que no cancelaron (Churn == 0)
    fig.add_trace(go.Histogram(
        x=dataset.query("Churn == 0")["MonthlyCharges"],
        name="Retención",
        opacity=0.35,
        histnorm="probability density",
        marker_color='#98b3e9'
    ))

    # Histograma para clientes que cancelaron (Churn == 1)
    fig.add_trace(go.Histogram(
        x=dataset.query("Churn == 1")["MonthlyCharges"],
        name="Cancelación",
        opacity=0.35,
        histnorm="probability density",
        marker_color='#c43e24'
    ))

    # Personalizar el diseño del gráfico
    fig.update_layout(
        title="Distribución de cargos mensuales por estado de cancelación",
        plot_bgcolor=background_color, 
        paper_bgcolor=background_color, 
        title_font_color=text_color,
        title_x=0.4,
        margin=dict(l=80, r=80, t=80, b=80),
        xaxis_title="Cargos mensuales",
        yaxis_title="Densidad",
        xaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
        yaxis=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
        barmode="overlay",
        legend=dict(
            x=0.8, 
            y=0.95,
            title_font=dict(color=text_color),
            font=dict(color=text_color)
        ),
        bargap=0.1
    )
    return fig