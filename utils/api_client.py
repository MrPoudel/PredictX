import requests

# Add your Polygon.io API key here
API_KEY = 'aJ9dDaBOtX0sBFOtNdkQTw_VMGR8i1LA'

BASE_URL = "https://api.polygon.io/v2/aggs/ticker"

def get_real_time_price(stock_symbol):
    """
    Fetch the current stock price for the given stock symbol using Polygon.io API.
    :param stock_symbol: The stock symbol to get the real-time price for (e.g., 'AAPL').
    :return: Current stock price or None if there's an error.
    """
    url = f"{BASE_URL}/{stock_symbol}/prev"
    params = {
        'apiKey': API_KEY
    }

    try:
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Log the data for debugging purposes
            print(f"API Response for {stock_symbol}: {data}")

            # Check if we have the expected data in the response
            if 'results' in data and len(data['results']) > 0:
                latest_price = data['results'][0]['c']  # 'c' is the close price from the most recent trading day
                return latest_price
            else:
                print(f"Error: No valid data found for {stock_symbol}.")
                return None
        else:
            # Log the error if the status code is not 200
            print(f"Error: Failed to fetch data for {stock_symbol}. Status Code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock price for {stock_symbol}: {e}")
        return None
