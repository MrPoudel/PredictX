#!/bin/bash

# Create the required folders
mkdir -p config controllers models views utils tests

# Create files in the config folder
echo "{}" > config/config.json
echo "# Makes the config folder a package" > config/__init__.py

# Create files in the controllers folder
echo "# Makes the controllers folder a package" > controllers/__init__.py
echo "# Controls data fetching and validation" > controllers/data_controller.py
echo "# Controls prediction logic" > controllers/prediction_controller.py
echo "# Manages updates to configuration" > controllers/config_controller.py

# Create files in the models folder
echo "# Makes the models folder a package" > models/__init__.py
echo "# Model for storing and managing stock data" > models/stock_data.py
echo "# Machine learning model for predictions" > models/prediction_model.py

# Create files in the views folder
echo "# Makes the views folder a package" > views/__init__.py
echo "# Handles GUI rendering" > views/gui.py
echo "# Handles graph creation and display" > views/graph_plotter.py

# Create files in the utils folder
echo "# Makes the utils folder a package" > utils/__init__.py
echo "# Helper functions for API communication" > utils/api_client.py
echo "# Task scheduling utilities" > utils/scheduler.py

# Create files in the tests folder
echo "# Makes the tests folder a package" > tests/__init__.py
echo "# Unit tests for data_controller" > tests/test_data_controller.py
echo "# Unit tests for prediction_model" > tests/test_prediction_model.py
echo "# Unit tests for GUI functionality" > tests/test_gui.py

# Create top-level files
echo "# Main entry point for the application" > main.py
echo "# Python dependencies" > requirements.txt
echo "# Documentation for the project" > README.md
echo "# Project license" > LICENSE

# Print success message
echo "Folder structure generated successfully!"
