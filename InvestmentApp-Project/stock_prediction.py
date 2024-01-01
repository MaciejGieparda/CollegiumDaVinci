import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings

def predict_stock_performance(historical_data, symbol, forecast_days=[7, 30, 365]):
    """
    Predicts the stock's closing price for different numbers of days ahead using ARIMA.

    :param historical_data: DataFrame containing historical stock data.
    :param symbol: The stock symbol to predict.
    :param forecast_days: List of numbers of trading days ahead for the predictions.
    :return: Dictionary with predicted closing prices for the specified days ahead.
    """
    symbol_data = historical_data[historical_data['Symbol'] == symbol]
    close_prices = symbol_data['Close']
    warnings.filterwarnings("ignore")
    model = ARIMA(close_prices, order=(2, 1, 2))
    model_fit = model.fit()
    predictions = {}
    for days in forecast_days:
        forecast = model_fit.forecast(steps=days)
        predictions[days] = forecast.iloc[-1]
        print(symbol_data['Symbol'])  # Print the symbol for debugging purposes
    return predictions
