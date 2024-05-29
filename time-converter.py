
# Welcome the user to the program
print('Welcome to Time Converter')

# Define the function
def convert_time():

    time_input = input("Enter the time followed by its units "
        "('3 hours', '100 minutes', etc.): ").strip().lower()

# Split input into value and unit
    try:
        time_value, units = time_input.split()
        time_value = float(time_value)
    except ValueError:
        print("Invalid input format. Please enter in format "
            "'3 hours' or '100 minutes'.")
        return

# Check the units and perform the conversion
    if units in ['seconds', 'second', 'sec', 'secs', 's']:
        minutes = time_value / 60
        hours = time_value / 3600
        print(f"{time_value:.2f} seconds is {minutes:.2f} minutes or {hours:.2f} hours.")
    elif units in ['minutes', 'minute', 'mins', 'min', 'm']:
        seconds = time_value * 60
        hours = time_value / 60
        print(f"{time_value:.2f} minutes is {hours:.2f} hours or {seconds:.2f} seconds.")
    elif units in ['hours', 'hour', 'hrs', 'hr', 'h']:
        minutes = time_value * 60
        seconds = time_value * 3600
        print(f"{time_value:.2f} hours is {minutes:.2f} minutes or {seconds:.2f} seconds.")
    else:
        print("Unsupported unit of time. Please use 'hours', 'days', or 'seconds'.")

# Run the conversion
convert_time()
