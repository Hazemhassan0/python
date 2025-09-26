from math_automation import calculate_math_operations, print_report
from regex_log_cleaner import extract_emails
from datetime_reminder import add_reminder
from product_data_transformer import transform_product_data
from os_file_manager import manage_files
from random_data_generator import generate_random_data
from decorators import log_time

@log_time
def run_task_1():
    numbers = list(map(float, input("Enter numbers (comma-separated): ").split(',')))
    calculate_math_operations(numbers)
    print_report()

@log_time
def run_task_2():
    count = extract_emails()
    print(f"Total valid emails found: {count}")

def run_task_3():
    date = input("Enter a date (YYYY-MM-DD): ")
    reminder = add_reminder(date)
    if reminder:
        print(f"Reminder added: {reminder}")

def run_task_4():
    products = input("Enter product names (comma-separated): ")
    prices = input("Enter product prices (comma-separated): ")
    preview = transform_product_data(products, prices)
    print("Preview of the first 5 products:")
    print(preview)

def run_task_5():
    directory_path = input("Enter a directory path: ")
    copied_files = manage_files(directory_path)
    print(f"{copied_files} .txt files copied to the backup folder.")

def run_task_6():
    count = int(input("How many random numbers to generate? "))
    total_count, average = generate_random_data(count)
    print(f"Generated {total_count} numbers. Average: {average}")

def display_menu():
    print("Select a task:")
    print("1. Math Automation")
    print("2. Regex Log Cleaner")
    print("3. Datetime Reminder Script")
    print("4. Product Data Transformer")
    print("5. OS File Manager")
    print("6. Random Data Generator")

if __name__ == "__main__":
    display_menu()
    task_choice = int(input("Enter task number: "))
    
    if task_choice == 1:
        run_task_1()
    elif task_choice == 2:
        run_task_2()
    elif task_choice == 3:
        run_task_3()
    elif task_choice == 4:
        run_task_4()
    elif task_choice == 5:
        run_task_5()
    elif task_choice == 6:
        run_task_6()
    else:
        print("Invalid task number.")
