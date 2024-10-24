#/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
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

if __name__ == "__main__":
    main()
