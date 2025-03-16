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