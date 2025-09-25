import random

def task_1():
    numbers = []
    for i in range(5):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    print("Ascending order:", sorted(numbers))
    print("Descending order:", sorted(numbers, reverse=True))


def task_2():
    while True:
        try:
            length = int(input("Enter the length: "))
            start = int(input("Enter the starting number: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    
    sequence = [start + i for i in range(length)]
    print("Generated sequence:", sequence)

def task_3():
    total = 0
    count = 0
    
    while True:
        user_input = input("Enter a number (type 'done' to finish): ")
        
        if user_input == "done":
            break
        try:
            num = float(user_input)
            total += num
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")
    
    if count > 0:
        average = total / count
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average}")
    else:
        print("No valid numbers entered.")


def task_4():
    user_input = input("Enter a list of numbers ")
    try:
        numbers = [int(x) for x in user_input.split(' ')]
        numbers = list(set(numbers)) 
        numbers.sort()
        print("output", numbers)
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers separated by commas.")


def task_6():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_count = {}
    
    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    
    print("Words count:", word_count)

def task_7():
    students = {}
    
    for i in range(5):
        while True:
            name = input(f"Enter the name of student {i + 1}: ")
            try:
                score = float(input(f"Enter the score for {name}: "))
                students[name] = score
                break
            except ValueError:
                print("Invalid score. Please enter a valid number.")
    
    highest_score = max(students.values())
    lowest_score = min(students.values())
    average_score = sum(students.values()) / len(students)
    
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Average score: {average_score}")


def task_8():
    cart = {}
    
    while True:
        action = input("What would you like to do? (add/remove/view/total/quit): ").lower()
        
        if action == "add":
            item = input("Enter the item name: ")
            try:
                price = float(input(f"Enter the price for {item}: "))
                cart[item] = price
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        
        elif action == "remove":
            item = input("Enter the item name to remove: ")
            if item in cart:
                del cart[item]
                print(f"{item} has been removed from the cart.")
            else:
                print(f"{item} not found in the cart.")
        
        elif action == "view":
            print("Items in your cart:")
            for item, price in cart.items():
                print(f"{item}: ${price:.2f}")
        
        elif action == "total":
            total_cost = sum(cart.values())
            print(f"Total cost: ${total_cost:.2f}")
        
        elif action == "quit":
            break
        
        else:
            print("Invalid action. Please choose from add/remove/view/total/quit.")


def task_9():
    target_number = random.randint(1, 20)
    attempts = 0
    
    print("let the games begin!")
    while True:
        try:
            guess = int(input("Guess between 1 and 20: "))
            attempts += 1
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print(f"Correct! You won in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20.")


def main_menu():
    while True:
        print("\nPlease choose a task:")
        print("1: Task 1 - Enter 5 numbers")
        print("2: Task 2 - Generate a sequence of numbers")
        print("3: Task 3 - Keep asking for numbers until 'done'")
        print("4: Task 4 - Remove duplicates and sort a list")
        print("6: Task 6 - Count word freq ")
        print("7: Task 7 - Gradebook system")
        print("8: Task 8 - Shopping cart ")
        print("9: Task 9 - Number guessing game")
        print("0: Exit")
        
        try:
            choice = int(input("Enter the task number: "))
            
            if choice == 1:
                task_1()
            elif choice == 2:
                task_2()
            elif choice == 3:
                task_3()
            elif choice == 4:
                task_4()
            elif choice == 6:
                task_6()
            elif choice == 7:
                task_7()
            elif choice == 8:
                task_8()
            elif choice == 9:
                task_9()
            elif choice == 0:
                print("bye")
                break
            else:
                print("Invalid choice. Please enter a valid number between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


main_menu()
