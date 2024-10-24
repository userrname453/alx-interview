#!/usr/bin/python3
'''A script for parsing and tracking statistics from HTTP request logs.'''

import re

def extract_input(input_line):
    '''Extracts relevant sections from a line in the HTTP request log.

    Args:
        input_line (str): A single line from the log.

    Returns:
        dict: A dictionary containing the extracted status code and file size.
    '''
    # Define the regular expression pattern for matching log components.
    fp = (
        r'\s*(?P<ip>\S+)\s*',  # IP address
        r'\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]',  # Timestamp
        r'\s*"(?P<request>[^"]*)"\s*',  # HTTP request line
        r'\s*(?P<status_code>\S+)',  # Status code
        r'\s*(?P<file_size>\d+)'  # File size
    )

    # Initialize default values for the status code and file size.
    info = {
        'status_code': 0,
        'file_size': 0,
    }

    # Compile the full regex pattern for matching a log entry.
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)

    # If the line matches the pattern, extract and store the data.
    if resp_match is not None:
        info['status_code'] = resp_match.group('status_code')
        info['file_size'] = int(resp_match.group('file_size'))
    
    return info

def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics from the HTTP request log.

    Args:
        total_file_size (int): The total size of all files requested.
        status_codes_stats (dict): A dictionary of status codes and their counts.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the log metrics based on the given input line.

    Args:
        line (str): A line from the log file.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): The current status code statistics.

    Returns:
        int: The updated total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')

    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1

    return total_file_size + line_info['file_size']

def run():
    '''Starts the log parser to continuously read and analyze input.'''
    line_num = 0
    total_file_size = 0
    # Initialize the status codes we're tracking.
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }

    try:
        while True:
            line = input()
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            line_num += 1

            # Print statistics every 10 lines.
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)

    except (KeyboardInterrupt, EOFError):
        # Print final statistics before exiting.
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
