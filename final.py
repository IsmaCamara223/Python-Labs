# Dictionary to store coin denominations and their values in dollars
coin_values = {"penny": 0.01, "pennies": 0.01, "nickel": 0.05, "nickels": 0.05, "dime": 0.10, "dimes": 0.10, "quarter": 0.25, "quarters": 0.25}

def user_input(sentence):
    # Replace " and " with spaces to simplify splitting
    sentence = sentence.replace(" and ", " ")
    # Split the input sentence into words
    words = sentence.split()
    
    total_amount = 0.0
    
    # Iterate through the words in pairs (qty, name)
    for i in range(0, len(words), 2):
        qty = int(words[i])
        name = words[i + 1].lower()  # Ensure name is in lowercase
        # Add the value to the total amount
        total_amount += qty * coin_values[name]
    
    # Return the total amount formatted to two decimal places
    return "{:.2f}".format(total_amount)

# Test cases
test_cases = [
    "1 penny and 8 nickels",
    "21 nickels and 15 pennies",
    "4 dimes and 7 quarters",
    "21 pennies and 17 dimes and 52 quarters",
    "1 quarter and 46 pennies",
    "1 nickel and 17 quarters",
    "1 dime and 1 nickel and 1 penny and 1 quarter",
    "98 dimes and 83 quarters and 20 nickels and 46 pennies"
]

# Testing the implementation
for test_case in test_cases:
    print(f"{test_case} -> {user_input(test_case)}")
