# 🔓 Brute Force CAPTCHA Bypass  

A Python script to brute-force login pages on CTFs while solving CAPTCHA dynamically. Handles username enumeration, password brute-forcing, and CAPTCHA bypass.

---

## 📌 Overview  
This script automates **username enumeration** and **password brute-force attacks** on login pages that use **simple arithmetic CAPTCHAs** (addition, subtraction, multiplication). It attempts multiple passwords while dynamically solving CAPTCHAs and handling incorrect attempts.  

- 🔹 **Works on websites with numeric CAPTCHAs**  
- 🔹 **Extracts and solves CAPTCHA in real-time**  
- 🔹 **Handles username discovery and password brute-force**  
- 🔹 **Uses session handling for better reliability**  

---

## ✨ Features  
✅ **Username enumeration** – Detects valid usernames based on server responses.  
✅ **Password brute-force** – Attempts multiple passwords efficiently.  
✅ **CAPTCHA solver** – Automatically solves arithmetic CAPTCHAs (+, -, *).  
✅ **Error handling** – Detects invalid logins, incorrect CAPTCHAs, and retries.  
✅ **Session handling** – Uses persistent sessions to maintain cookies.  
✅ **Customizable attack** – Works with any website login form.  

---

## 🚀 Usage  

### 1️⃣ Finding the Correct Username
Run username.py to enumerate valid usernames from usernames.txt:

python3 user_enum.py

🔹 What it does:
Tries each username from usernames.txt.
Identifies the correct username based on the server's response.
Stops when a valid username is found.

🔹 Where to modify:
Change the target IP inside username.py:
url = "http://TARGET_IP/login"  # Update with the correct target
