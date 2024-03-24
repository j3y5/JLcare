import re

def is_valid_uk_phone_number(phone_number):
    # check for phone number format
    pattern = r'^\d{4} \d{6}$'
    
    # Check if the input string matches the pattern
    if re.match(pattern, phone_number):
        return True
    else:
        return False

# Test the function
phone_number = input("Enter a UK phone number: +44 ")
if is_valid_uk_phone_number(phone_number):
    print("Valid UK phone number!")
else:
    print("Invalid UK phone number. Please enter a valid UK phone number in the format +44 XXXX XXXXXX.")
