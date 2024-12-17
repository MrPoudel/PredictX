# PredictX

## Overview
The goal of PredictX is to predict the stock price of selected companies (like Nvidia, Google, Tesla, Microsoft, and Broadcom) for the next 24 hours. The system will pull real-time data every 10 minutes, analyze it, and predict the stock price for the next 24 hours. It will also display the results in a colorful GUI, with a graph of predicted stock prices. Users can modify which stocks to predict via a configuration file, with a limit of 10 stocks.

## Key Requirements

1. Real-Time Data Pulling: The system will use Polygon.io API to pull real-time stock data every 10 minutes.

2. Prediction Algorithm: Based on the collected data, a prediction model will predict stock prices for the next 24 hours.

3. User Interface: A GUI to display predictions, stock names, and real-time graphs.

4. Configuration Management: The user can modify the configuration file, and the system should automatically update the stock selection.

5. Platform: The system is designed to run on an Ubuntu machine.

## Key Components

- Polygon.io API: For fetching real-time stock data.
- Data Pooling Mechanism: Fetch data every 10 minutes.
- Prediction Algorithm: A machine learning model (e.g., Linear Regression, ARIMA, or LSTM) to predict stock prices for the next 24 hours.
- GUI Framework: For displaying results with graphs. We can use Tkinter (for simplicity) or PyQt.
- Configuration File: A text-based file (JSON or YAML) to allow users to configure which stocks to track

## Software Architecture

1. Data Collection Layer
- API Client: An API client will interact with Polygon.io API to fetch real-time stock data.This client will be set up to poll the data every 10 minutes.Fetch the historical stock price data for the past few hours to make predictions.
- Scheduler: A task scheduler will trigger data collection every 10 minutes. Python's schedule module or cron jobs can be used for this purpose.
2. Prediction Layer
- Data Preprocessing: The collected stock data will be cleaned and prepared for model consumption.
- Data transformation (e.g., scaling or normalization) will be performed for predictive analysis.
- Prediction Model: A machine learning model will predict stock prices for the next 24 hours. Possible algorithms include:
- Linear Regression: A basic method to predict future values based on past trends.
- LSTM (Long Short-Term Memory): A type of neural network suitable for time-series forecasting.
Prediction Output: The system will compute the predicted price for each stock and prepare the data for GUI display.
3. GUI Layer
- Framework: The GUI will be created using Tkinter or PyQt5.
- Real-Time Graphs: The results of the predictions will be displayed in a dynamic graph. Matplotlib or Plotly can be used to generate the graphs.
- Stock Selection: Users can input or select stock symbols from a drop-down list (up to 10 stocks).
- Configuration Options: The GUI will allow users to modify the configuration (e.g., change the list of stock symbols).
- Display: The GUI will show the stock name, predicted value for the next 24 hours, and a graph of the predicted data.
4. Configuration File
The configuration file (e.g., config.json) will contain the list of stocks to track.
It will be updated dynamically via the GUI, and the system will reload it to update the stock list.

## Component Diagram

+------------------------+
|       User Interface    |
|                        |
|  - Select stocks       |
|  - View predictions    |
|  - View graphs         |
|  - Edit config         |
+------------------------+
          |
          V
+-------------------------+         +-----------------------+
|     Configuration       |         |  Data Collection      |
|       (JSON file)       |         |   & API Client        |
|  - Stock list (10 max)  |         |  - Fetch data from    |
+-------------------------+         |    Polygon.io API     |
          |                         |  - Collect data       |
          V                         +-----------------------+
+-------------------------+
|     Prediction Model    |
|   (Linear Regression,    |
|        ARIMA, LSTM)      |
|  - Process data         |
|  - Predict stock prices |
|  - Return predictions   |
+-------------------------+
          |
          V
+--------------------------+
|    Graph Display & GUI   |
|  - Show predictions      |
|  - Display graphs        |
+--------------------------+
