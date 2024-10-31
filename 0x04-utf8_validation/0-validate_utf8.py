#!/usr/bin/python3
"""Module to validate UTF-8 encoded data."""

def isValidUTF8(data):
    """Determines if a list of integers represents valid UTF-8 encoded characters.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    remaining_bytes = 0
    data_len = len(data)
    for idx in range(data_len):
        if remaining_bytes > 0:
            remaining_bytes -= 1
            continue
        if type(data[idx]) != int or data[idx] < 0 or data[idx] > 0x10ffff:
            return False
        elif data[idx] <= 0x7f:
            remaining_bytes = 0
        elif data[idx] & 0b11111000 == 0b11110000:
            # 4-byte sequence in UTF-8
            byte_count = 4
            if data_len - idx >= byte_count:
                following_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + byte_count],
                ))
                if not all(following_bytes):
                    return False
                remaining_bytes = byte_count - 1
            else:
                return False
        elif data[idx] & 0b11110000 == 0b11100000:
            # 3-byte sequence in UTF-8
            byte_count = 3
            if data_len - idx >= byte_count:
                following_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + byte_count],
                ))
                if not all(following_bytes):
                    return False
                remaining_bytes = byte_count - 1
            else:
                return False
        elif data[idx] & 0b11100000 == 0b11000000:
            # 2-byte sequence in UTF-8
            byte_count = 2
            if data_len - idx >= byte_count:
                following_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + byte_count],
                ))
                if not all(following_bytes):
                    return False
                remaining_bytes = byte_count - 1
            else:
                return False
        else:
            return False
    return True