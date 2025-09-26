
import re

def extract_emails(log_file='access.log', output_file='valid_emails.txt'):

    log_data = [
        "user1@example.com some other log data",
        "invalidemail.com",
        "test.email@domain.org",
        "random string without email",
        "valid.email@company.com",
        "another.invalid.email@com",
        "correct.email@domain.net"
    ]
    
    with open(log_file, 'w') as file:
        for line in log_data:
            file.write(line + '\n')
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = [line for line in log_data if re.match(email_pattern, line)]
    
    with open(output_file, 'w') as file:
        for email in set(emails):
            file.write(email + '\n')
    
    return len(set(emails))
