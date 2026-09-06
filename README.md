#Acepted the second use of AI -- Description of what is happening in the Code

# Flight-Time Calculator

This project implements two functions that compute quadcopter flight time
based on payload weight. The calculation follows the linear formula:

T(w) = 180 - 0.1w

## Files
- flight_calculator.py — main implementation
- .gitignore — ignores Python cache files and virtual environments

## Functions
- calculate_flight_time(weight_grams)
- flight_time_table(max_weight_grams, step_grams)

## How to Run
python flight_calculator.py
