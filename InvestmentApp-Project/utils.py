import pandas as pd

def get_unique_filter_values(csv_file):
        """
        Reads the given CSV file and returns unique values for each filter category.

        Parameters:
        - csv_file (str): The path to the CSV file.

        Returns:
        - dict: A dictionary containing unique values for each filter category.
            The keys are 'Names', 'Countries', 'Sectors', and 'Industries'.
            The values are lists of unique values for each category.
        """
        symbols = pd.read_csv(csv_file)
        symbols = symbols[['Symbol', 'Name', 'Country', 'Sector', 'Industry', 'Market Cap']]
        return {
                'Names': sorted(symbols['Name'][pd.notna(symbols['Name'])].unique().tolist()),
                'Countries': sorted(symbols['Country'][pd.notna(symbols['Country'])].unique().tolist()),
                'Sectors': sorted(symbols['Sector'][pd.notna(symbols['Sector'])].unique().tolist()),
                'Industries': sorted(symbols['Industry'][pd.notna(symbols['Industry'])].unique().tolist())
        }

def normalize_symbol(symbol):
    """
    Normalizes a stock symbol to conform to Yahoo Finance's format.
    Replaces '/' with '-' if the symbol is a string.
    """
    if isinstance(symbol, str):
        return symbol.replace('/', '-')
    return symbol

# Load symbol data from 'symbols.csv' and apply normalization to the 'Symbol' column
symbols = pd.read_csv('symbols.csv')
symbols = symbols[['Symbol', 'Name', 'Country', 'Sector', 'Industry', 'Market Cap']]
symbols['Symbol'] = symbols['Symbol'].apply(normalize_symbol)