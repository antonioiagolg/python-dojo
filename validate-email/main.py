import re
from email import utils

def print_valid_emails(emails):
    pattern = r'[a-zA-Z][a-zA-Z\-\._0-9]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    for email in emails:
        possible_email = utils.parseaddr(email, strict=True)
        if possible_email and re.match(pattern, possible_email[1]):
            print(utils.formataddr(possible_email))

if __name__ == '__main__':
    size = int(input())
    emails = []
    for i in range(size):
        emails.append(input())
    
    print_valid_emails(emails)