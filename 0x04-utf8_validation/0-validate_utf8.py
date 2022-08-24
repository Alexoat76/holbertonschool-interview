#!/usr/bin/python3
"""
This module contains a method that determines if a given data set
is valid UTF-8 encoding.
"""
# HINT:
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the
# following rules:
#
# For 1-byte character, the first bit is a 0, followed by its unicode code.
# For n-bytes character, the first n-bits are all one's, the n+1 bit is 0,
# followed by n-1 bytes with most significant 2 bits being 10.
# This is how the UTF-8 encoding would work:
#
#   Char. number range  |        UTF-8 octet sequence
#       (hexadecimal)    |              (binary)
#   --------------------+---------------------------------------------
#   0000 0000-0000 007F | 0xxxxxxx
#   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# Given an array of integers representing the data, return whether it is a
# valid utf-8 encoding.
#
# Note:
# The input is an array of integers.
# Only the least significant 8 bits of each integer is used to store the data.
# This means each integer represents only 1 byte of data.


def validUTF8(data):
    """
    Determine if a given data set is valid UTF-8 encoding.
    - Returns: True if data is valid UTF-8 encoding, False otherwise.
    - A character in UTF-8 can be 1 to 4 bytes long.
    - The data set can contain multiple characters.
    - The data will be represented by a list of integers, where each integer
        represents a byte, therefore you only need to handle the 8 least
        significant bits of each integer.
    """
    # number of bytes in the current UTF-8 character being processed
    number_of_bytes = 0

    # Mask to check if the most significant bit is set to 1 or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6
    for byte in data:  # for each byte in the data set
        if number_of_bytes == 0:
            if byte & mask1 == 0:  # if the most significant bit is 0
                # reset the number of bytes in the current UTF-8 character
                number_of_bytes = 0
                """if the most significant bit is 1 and the second most
                   significant bit is 0 (110xxxxx) then the number of bytes in
                   the current UTF-8 character is 1 byte.
                """
            elif byte & mask1 == mask1:
                number_of_bytes = 1
                """if the most significant bit is 1 and the second most
                   significant bit is 1 (1110xxxx) then the number of bytes
                   in the current UTF-8 character is 2 bytes.
                """
            elif byte & mask2 == mask2:
                # reset the number of bytes in the current UTF-8 character
                number_of_bytes = 2
            else:
                return False
        else:
            """if the most significant bit is 0 then the number of bytes in
               the current UTF-8 character is invalid.
            """
            if byte & mask1 == 0:
                return False
            number_of_bytes -= 1
    """if number_of_bytes is 0, then all bytes are valid UTF-8 characters and
       the data is valid UTF-8 encoding
    """
    return number_of_bytes == 0
