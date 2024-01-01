from flask import Flask, render_template, request, jsonify
from flask.views import MethodView
import pandas as pd
from utils import get_unique_filter_values
from api_connection import get_basic_info, get_historical_data
from data_processing import filter_symbols, generate_plotly_figure
import plotly.graph_objs as go
import plotly.io as pio
from stock_prediction import predict_stock_performance

# Base class for the application
class InvestmentApp(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)
        self.configure_routes()

    def configure_routes(self):
        self.add_url_rule('/', view_func=IndexView.as_view('index'))
        self.add_url_rule('/get_data', view_func=GetDataView.as_view('get_data'))
        self.add_url_rule('/predict_prices', view_func=PredictPricesView.as_view('predict_prices'))

# View class for the home page
class IndexView(MethodView):
    def get(self):
        filters = get_unique_filter_values('symbols.csv')
        return render_template('index.html', filters=filters)

    def post(self):
        filters = get_unique_filter_values('symbols.csv')
        symbol = request.form.get('name')
        historical_data = get_historical_data(symbol)
        fig = generate_plotly_figure(historical_data)
        plot_html = pio.to_html(fig, full_html=False)
        data_to_display = pd.DataFrame(historical_data).to_html(classes='table table-striped', index=False)
        return render_template('index.html', plot_html=plot_html, filters=filters, data_to_display=data_to_display)

# View class for '/get_data'
class GetDataView(MethodView):
    def post(self):
        criteria = {
            'name': request.form.get('name'),
            'country': request.form.get('country'),
            'sector': request.form.get('sector'),
            'industry': request.form.get('industry'),
            'amount': int(request.form.get('amount', 10))
        }
        filter_values = filter_symbols('Name', criteria['name'], criteria['amount'], name=criteria['name'], country=criteria['country'], sector=criteria['sector'], industry=criteria['industry'])
        basic_info_data = [get_basic_info(symbol) for symbol in filter_values['Symbol']]
        data_to_display = pd.DataFrame(basic_info_data).to_html(classes='table table-striped', index=False)
        historical_data = get_historical_data(filter_values['Symbol'].tolist())
        fig = generate_plotly_figure(historical_data)
        plot_html = pio.to_html(fig, full_html=False, include_plotlyjs=False)
        return jsonify({'plot_html': plot_html, 'html_table': data_to_display, 'symbols': filter_values['Symbol'].tolist()})

# View class for '/predict_prices'
class PredictPricesView(MethodView):
    """
    View class for predicting stock prices.

    Methods:
    - post: Handles the POST request and returns the predicted prices for the given symbols.
    """

    def post(self):
        data = request.get_json()
        symbols = data['symbols']
        predictions = []
        for symbol in symbols:
            historical_data = get_historical_data([symbol])
            current_close_price = historical_data.iloc[-1]['Close']
            predicted_prices = predict_stock_performance(historical_data, symbol, forecast_days=[7, 30, 365])
            perc_diff_7_days = round(((predicted_prices[7] - current_close_price) / current_close_price) * 100, 2)
            perc_diff_30_days = round(((predicted_prices[30] - current_close_price) / current_close_price) * 100, 2)
            perc_diff_365_days = round(((predicted_prices[365] - current_close_price) / current_close_price) * 100, 2)
            predictions.append({
                'symbol': symbol,
                'current_price': round(current_close_price, 2),
                '7_days': round(predicted_prices[7], 2),
                '30_days': round(predicted_prices[30], 2),
                '365_days': round(predicted_prices[365], 2),
                '7_days_diff': perc_diff_7_days,
                '30_days_diff': perc_diff_30_days,
                '365_days_diff': perc_diff_365_days
            })
        predictions_html = render_template('predictions.html', predictions=predictions)
        return jsonify({'predictions_html': predictions_html})

# Run the application
if __name__ == '__main__':
    app = InvestmentApp(__name__)
    app.run(debug=True)
