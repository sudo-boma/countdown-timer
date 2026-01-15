# Countdown Timer

A simple command-line countdown timer application that counts down from a specified number of seconds and displays a "BLAST OFF!" message when complete.

## Features

- **User Input**: Prompts the user to enter a countdown time in seconds
- **Formatted Display**: Shows time in MM:SS format with leading zeros
- **Real-time Updates**: Updates the countdown in real-time on a single line
- **Error Handling**: Validates user input for non-negative integers
- **Completion Message**: Displays a fun "BLAST OFF!" message when the timer reaches zero

## Requirements

- Python 3.x
- No external dependencies - uses only Python's standard library

## Installation

No installation required. Simply save the script to a file (e.g., `countdown.py`) and run it with Python.

## Usage

1. Run the script:
   ```bash
   python countdown.py
   ```

2. When prompted, enter the number of seconds for the countdown:
   ```
   Enter the countdown in seconds: 10
   ```

3. Watch the countdown timer in real-time:
   ```
   Time Remaining: 00:10
   ```

4. When the timer reaches zero, you'll see:
   ```
   Time Remaining: 00:00
   BLAST OFF!
   ```

## Code Explanation

### Main Components

1. **`countdown(t)` Function**:
   - Takes an integer `t` representing seconds
   - Uses a while loop to count down from `t` to 0
   - Converts seconds to minutes and seconds using `divmod()`
   - Formats the time as MM:SS with leading zeros
   - Updates the display on the same line using `\r` carriage return
   - Pauses for 1 second between updates with `time.sleep(1)`

2. **Input Handling**:
   - Prompts user for input with `input()`
   - Converts input to integer with error handling
   - Validates that the input is a non-negative integer
   - Provides helpful error messages for invalid input

### Key Functions Used

- `divmod(t, 60)`: Divides total seconds into minutes and seconds
- `time.sleep(1)`: Pauses execution for 1 second
- `print(..., end="\r")`: Prints to the same line by returning to the beginning
- `try/except`: Handles non-integer input gracefully

## Example Output

```
Enter the countdown in seconds: 5
Time Remaining: 00:05
```

The display will update every second:
```
Time Remaining: 00:04
Time Remaining: 00:03
Time Remaining: 00:02
Time Remaining: 00:01
Time Remaining: 00:00
BLAST OFF!
```

## Error Handling

The program handles two types of invalid input:

1. **Non-integer values**: Displays "Invalid input. Please enter an integer."
2. **Negative numbers**: Displays "Please enter a non-negative integer."

## Limitations

- The timer resolution is 1 second
- Requires a terminal/command line environment that supports carriage return (`\r`) behavior
- No pause/resume functionality
- No sound alerts
- Countdown continues even if the terminal loses focus

## Customization Ideas

You can modify the code to:
- Add sound alerts when the timer completes
- Accept time in minutes:seconds format (e.g., "2:30")
- Add pause/resume functionality
- Change the completion message
- Add color to the display using ANSI escape codes
- Create a graphical interface

## License

This is a simple educational project. Feel free to use and modify as needed.

## Contributing

Feel free to fork and modify this code for your own purposes. If you have improvements, consider sharing them with others learning Python.
