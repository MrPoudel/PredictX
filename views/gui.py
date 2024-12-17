import tkinter as tk
from tkinter import messagebox
from views.graph_plotter import plot_graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from utils.api_client import get_real_time_price  # Import the function from api_client.py

class StockPredictionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Prediction")
        self.root.geometry("800x600")

        # Stock symbols available for selection
        self.stock_symbols = ["AAPL", "TSLA", "GOOG", "MSFT", "NVDA"]
        
        # GUI elements
        self.left_frame = tk.Frame(self.root)  # Frame for the left side
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

        self.stock_label = tk.Label(self.left_frame, text="Select Stock:")
        self.stock_label.pack()

        # Create radio buttons for stock selection
        self.stock_var = tk.StringVar(value="TSLA")  # Default to "TSLA"
        for stock in self.stock_symbols:
            tk.Radiobutton(self.left_frame, text=stock, variable=self.stock_var, value=stock).pack(anchor=tk.W)

        # Button to trigger prediction
        self.predict_button = tk.Button(self.left_frame, text="Predict", command=self.show_predictions)
        self.predict_button.pack(pady=20)

        # Frame for graph and predictions (right side)
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Prediction label to show the predicted stock value
        self.prediction_label = tk.Label(self.right_frame, text="Prediction will be shown here")
        self.prediction_label.pack()

        # Canvas for the graph
        self.graph_canvas = None

    def show_predictions(self):
        stock = self.stock_var.get()

        # Fetch the real-time stock price via Polygon.io API
        current_price = get_real_time_price(stock)
        
        if current_price is None:
            messagebox.showerror("Error", "Failed to fetch stock data. Please check the API and try again.")
            return
        
        # Generate predictions based on the current stock price (simulated for this example)
        predicted_data = self.generate_predictions(current_price)

        # Update the prediction label with the predicted price
        predicted_price = predicted_data[-1]  # Latest predicted value
        self.prediction_label.config(text=f"Prediction for {stock}: ${predicted_price:.2f}")

        # Get the current time and predict the next 5 hours in AM/PM format
        current_time = datetime.now()
        time_slots = [(current_time + timedelta(hours=i)).strftime("%I:%M %p") for i in range(5)]

        # Plot the graph within the same GUI window
        self.plot_stock_graph(predicted_data, stock, time_slots)

    def generate_predictions(self, current_price):
        # Here we generate a simple prediction based on the current price
        # For demo purposes, let's simulate small changes in the price
        predicted_data = [current_price]
        for i in range(1, 5):  # Generate predictions for the next 5 time slots
            change = (predicted_data[-1] * 0.01)  # Predict a 1% increase or decrease
            predicted_data.append(predicted_data[-1] + change)  # Add the change to the last predicted value
        return predicted_data

    def plot_stock_graph(self, data, stock, time_slots):
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(6, 5))  # Set the size of the graph
        ax.plot(time_slots, data, label=f'{stock} Stock Prediction', color='blue', marker='o')

        # Add title and labels
        ax.set_title(f'{stock} Stock Prediction')
        ax.set_xlabel('Time (Next 5 hours)')
        ax.set_ylabel('Predicted Price ($)')
        ax.legend()

        # Remove the old graph if it exists
        if self.graph_canvas:
            self.graph_canvas.get_tk_widget().destroy()

        # Embed the plot into the Tkinter GUI using FigureCanvasTkAgg
        self.graph_canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# To run the GUI
def run_gui():
    root = tk.Tk()
    gui = StockPredictionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
