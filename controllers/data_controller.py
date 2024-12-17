import requests
import json

class DataController:
    def __init__(self, config_path="config/config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.api_key = self.config["api_key"]

    def fetch_stock_data(self, stock_symbol):
        """
        Fetch historical stock data for the given stock symbol from Polygon.io.
        """
        base_url = f"https://api.polygon.io/v1/open-close/{stock_symbol}/2024-12-15"
        params = {"apiKey": self.api_key}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data for {stock_symbol}: {response.text}")
