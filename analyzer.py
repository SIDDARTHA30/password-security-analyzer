import os
import re   # Used to check patterns like uppercase, numbers, and symbols


# This function reads common passwords from the text file
def load_common_passwords():
    # Get the directory where this Python file is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the full path to the common passwords file
    file_path = os.path.join(base_dir, "common_passwords.txt")

    # Open the file and read all passwords
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


# This function analyzes the security of the given password
def analyze_password(password):
    issues = []   # List to store detected security issues

    # Check minimum password length
    if len(password) < 8:
        issues.append("Password is too short (minimum 8 characters required)")

    # Check for uppercase letters
    if not re.search(r"[A-Z]", password):
        issues.append("No uppercase letter found")

    # Check for lowercase letters
    if not re.search(r"[a-z]", password):
        issues.append("No lowercase letter found")

    # Check for numbers
    if not re.search(r"[0-9]", password):
        issues.append("No number found")

    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("No special character found")

    # Load and check common passwords
    common_passwords = load_common_passwords()
    if password.lower() in common_passwords:
        issues.append("Password found in common passwords list")

    # Return all issues found
    return issues


# ---------------- MAIN PROGRAM ----------------

# Take password input from the user
password = input("Enter password to analyze: ")

# Analyze the entered password
problems = analyze_password(password)

# Display report header
print("\nPassword Security Report")
print("------------------------")

# If no issues are found
if not problems:
    print("Password Strength: STRONG")
    print("Good job! Your password looks secure.")
else:
    # If issues exist
    print("Password Strength: WEAK")
    print("\nIssues Found:")
    for issue in problems:
        print("- " + issue)

    # Suggestions to improve password security
    print("\nSuggestions:")
    print("- Use at least 10 characters")
    print("- Mix uppercase, lowercase, numbers, and symbols")
    print("- Avoid common or easy passwords")
