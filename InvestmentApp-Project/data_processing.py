import pandas as pd
from api_connection import symbols
import plotly.graph_objs as go
import plotly.io as pio

def filter_symbols(filter_category, filter_value, amount, name=None, country=None, sector=None, industry=None):
    """
    Filters symbols based on specified criteria and returns the top 'amount' symbols.
    
    Args:
        filter_category (str): The category to filter on (e.g., 'Name', 'Country', 'Sector', 'Industry').
        filter_value (str): The value to filter on.
        amount (int): The number of symbols to return.
        name (str, optional): The name of the symbol. Defaults to None.
        country (str, optional): The country of the symbol. Defaults to None.
        sector (str, optional): The sector of the symbol. Defaults to None.
        industry (str, optional): The industry of the symbol. Defaults to None.
    
    Returns:
        pandas.DataFrame: The filtered symbols sorted by market cap in descending order.
    """
    filtered_symbols = symbols.copy()

    if name:
        filtered_symbols = filtered_symbols[filtered_symbols['Name'] == name]
    if country:
        filtered_symbols = filtered_symbols[filtered_symbols['Country'] == country]
    if sector:
        filtered_symbols = filtered_symbols[filtered_symbols['Sector'] == sector]
    if industry:
        filtered_symbols = filtered_symbols[filtered_symbols['Industry'] == industry]

    if filter_category and filter_value:
        filtered_symbols = filtered_symbols[filtered_symbols[filter_category] == filter_value]

    return filtered_symbols.sort_values('Market Cap', ascending=False).head(amount)

def generate_plotly_figure(historical_data):
    """
    Generates a Plotly figure for visualizing stock prices over time.
    
    Args:
        historical_data (pandas.DataFrame): The historical stock price data.
    
    Returns:
        plotly.graph_objs._figure.Figure: The Plotly figure object.
    """
    fig = go.Figure()

    for symbol in historical_data['Symbol'].unique():
        symbol_data = historical_data[historical_data['Symbol'] == symbol]

        fig.add_trace(go.Scatter(
            x=symbol_data['Date'],
            y=symbol_data['Close'],
            mode='lines',
            name=symbol
        ))

    fig.update_layout(title='Stock Prices Over Time', xaxis_title='Date', yaxis_title='Price')

    return fig
