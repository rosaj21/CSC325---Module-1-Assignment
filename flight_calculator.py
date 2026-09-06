#T(W) = 180 - 0.1w, this is the main Equation.


#Acepted the first example of using AI 
"""
    Calculate the flight time based on the weight of the object.

    Parameters:
    weight (float): The weight of the object in kilograms.

    Returns:
    float: The calculated flight time in seconds.
    """

def calculate_flight_time(weight):
  
    if weight < 0:
        raise ValueError("Weight cannot be negative.")
    
    flight_time = 180 - 0.1 * weight
    return flight_time 


#checks to see if the weight is negative or not and if it is negative it will raise a ValueError.
def flight_time_table(max_weight_grams, step_grams):
    if max_weight_grams < 0 or step_grams <= 0:
        raise ValueError("Max weight must be non-negative and step must be positive.")

    table = []
    weight = 0

    while weight <= max_weight_grams:
        time = calculate_flight_time(weight)
        table.append((weight, time))
        weight += step_grams

    return table
