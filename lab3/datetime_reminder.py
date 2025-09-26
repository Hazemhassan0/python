
from datetime import datetime

def add_reminder(target_date_str):
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
    today = datetime.now()
    
    if target_date < today:
        print("This date has already passed.")
        return
    
    days_left = (target_date - today).days
    reminder_text = f"{target_date_str} -> {days_left} days left"
    

    with open('reminders.txt', 'a') as file:
        file.write(reminder_text + '\n')
    
    return reminder_text
