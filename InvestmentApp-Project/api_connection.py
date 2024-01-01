import yfinance as yf
import pandas as pd
from utils import normalize_symbol

symbols = pd.read_csv('symbols.csv')
symbols = symbols[['Symbol', 'Name', 'Country', 'Sector', 'Industry', 'Market Cap']]
symbols = symbols.dropna()
symbols['Symbol'] = symbols['Symbol'].apply(normalize_symbol)


def get_basic_info(symbol):
    """
    Retrieves basic company information for the given symbol.
    Handles exceptions gracefully and returns data with user-friendly column names.

    Parameters:
    symbol (str): The symbol of the company to retrieve information for.

    Returns:
    dict: A dictionary containing the basic company information with user-friendly column names.
          If an error occurs during retrieval, None is returned.
    """
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        column_name_mapping = {
            "longName": "Company Name",
            "symbol": "Symbol",
            "country": "Country",
            "sector": "Sector",
            "industry": "Industry",
            "previousClose": "Previous Close",
            "open": "Open Price",
            "dividendRate": "Dividend Rate",
            "dividendYield": "Dividend Yield",
            "marketCap": "Market Cap",
            "volume": "Volume"
        }

        return {column_name_mapping[key]: info.get(key, "") for key in column_name_mapping}

    except Exception as e:
        print(f"Error retrieving data for {symbol}: {e}")
        return None

def get_historical_data(symbols_list):
    """
    Retrieves historical data for a list of symbols, resets the index to make 'Date' a column,
    and adds a new column with the company symbol for each.
    """
    historical_data_list = []
    
    for symbol in symbols_list:
        stock = yf.Ticker(symbol)
        df = stock.history(period='max')
        df.reset_index(inplace=True)
        df['Symbol'] = symbol
        historical_data_list.append(df)

    historical_data = pd.concat(historical_data_list, ignore_index=True)
    return historical_data
