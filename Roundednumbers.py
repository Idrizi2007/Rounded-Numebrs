def round_to_nearest_nickel(total):
    # Function to round the total to the nearest nickel (0.05)
    return round(total * 20) / 20

total = 0  # Initialize total value

while True:
    value = input("Enter a value (press Enter to stop): ")  # Prompt user for input
    if value == "":  # Break the loop if the user presses Enter without input
        break
    else:
        try:
            price = float(value)  # Convert input to float
            total += price  # Add the value to the total
        except ValueError:
            print("Please enter a valid value.")  # Error message for invalid input

# Round the total to the nearest nickel
total = round_to_nearest_nickel(total)

print("The total value is:", total)  # Output the final rounded total
