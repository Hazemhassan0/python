
import math

def calculate_math_operations(numbers):
    results = []
    
    for num in numbers:
        floor_val = math.floor(num)
        ceil_val = math.ceil(num)
        sqrt_val = math.sqrt(num)
        area_of_circle = math.pi * (num ** 2)
        
        results.append({
            'number': num,
            'floor': floor_val,
            'ceil': ceil_val,
            'sqrt': sqrt_val,
            'area_of_circle': area_of_circle
        })

    with open('math_report.txt', 'w') as file:
        for result in results:
            file.write(f"Number: {result['number']}\n")
            file.write(f"Floor: {result['floor']}, Ceil: {result['ceil']}, Square Root: {result['sqrt']}, Area of Circle: {result['area_of_circle']}\n")
            file.write("\n")
    
    return results

def print_report():

    with open('math_report.txt', 'r') as file:
        content = file.read()
    print(content)
