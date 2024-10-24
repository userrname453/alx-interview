#!/usr/bin/python3
'''A script for parsing HTTP request logs.'''
import re
from collections import defaultdict

# Compile regex pattern once to avoid recompiling for each log line
LOG_PATTERN = re.compile(
    r'\s*(?P<ip>\S+)\s*'
    r'\s*\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\]\s*'
    r'"(?P<request>[^"]*)"\s*'
    r'(?P<status_code>\d{3})\s*'
    r'(?P<file_size>\d+)\s*'
)

def extract_input(input_line):
    '''Extracts relevant metrics from a line of an HTTP request log.'''
    match = LOG_PATTERN.fullmatch(input_line)
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size')),
        }
    return {'status_code': '0', 'file_size': 0}

def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.'''
    print(f'File size: {total_file_size}')
    for status_code in sorted(status_codes_stats):
        count = status_codes_stats[status_code]
        if count > 0:
            print(f'{status_code}: {count}')

def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics based on the input log line.'''
    metrics = extract_input(line)
    status_codes_stats[metrics['status_code']] += 1
    return total_file_size + metrics['file_size']

def run():
    '''Starts the log parser.'''
    total_file_size = 0
    status_codes_stats = defaultdict(int)

    try:
        for line_num, line in enumerate(iter(input, ''), start=1):
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
