#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_count = defaultdict(int)
line_count = 0

def print_metrics():
    """Print the current metrics."""
    print(f"File size: {total_file_size}")
    for status in sorted(status_count.keys()):
        print(f"{status}: {status_count[status]}")

def handle_sigint(signum, frame):
    """Handle keyboard interruption."""
    print_metrics()
    sys.exit(0)

def main():
    global total_file_size, status_count, line_count

    # Set up signal handling for keyboard interruption
    signal.signal(signal.SIGINT, handle_sigint)

    # Read from stdin line by line
    for line in sys.stdin:
        # Split the line and ensure it matches the expected format
        parts = line.strip().split(" ")
        if len(parts) == 7:
            try:
                # Extract relevant parts
                ip_address = parts[0]
                date = parts[2][1:-1]  # Remove the square brackets
                method = parts[3]  # GET
                status_code = int(parts[5])  # Status code
                file_size = int(parts[6])  # File size

                # Check if the status code is valid
                if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                    # Update totals
                    total_file_size += file_size
                    status_count[status_code] += 1
                    line_count += 1

                    # Print metrics after every 10 lines
                    if line_count % 10 == 0:
                        print_metrics()
            except (ValueError, IndexError):
                continue  # Skip lines that don't match expected format

    # Print final metrics when the input ends
    print_metrics()

if __name__ == '__main__':
    main()
