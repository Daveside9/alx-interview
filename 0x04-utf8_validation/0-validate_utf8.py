def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes_to_check = 0
    for num in data:
        if num_bytes_to_check == 0:
            if (num >> 5) == 0b110:
                num_bytes_to_check = 1
            elif (num >> 4) == 0b1110:
                num_bytes_to_check = 2
            elif (num >> 3) == 0b11110:
                num_bytes_to_check = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes_to_check -= 1
    return num_bytes_to_check == 0

