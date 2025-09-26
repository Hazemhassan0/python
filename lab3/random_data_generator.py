
import random
import csv

def generate_random_data(count):
    numbers = [random.randint(1, 100) for _ in range(count)]
    
    # Write to CSV
    with open('random_numbers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['index', 'value'])
        for idx, number in enumerate(numbers, 1):
            writer.writerow([idx, number])
    
    avg = sum(numbers) / len(numbers)
    return len(numbers), avg
