from models.prediction_model import PredictionModel

class PredictionController:
    def __init__(self):
        self.model = PredictionModel()

    def predict(self, stock_data):
        """
        Use the prediction model to forecast the next 24 hours of stock prices.
        """
        return self.model.predict(stock_data)
