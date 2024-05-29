import datetime

def format_date(date_str, date_format="%Y-%m-%d"):
    """
    Format a date string to a specific format.

    Args:
    - date_str: str. The date string to format.
    - date_format: str, optional, default="%Y-%m-%d". The desired format for the date string.

    Returns:
    - Formatted date string.
    """
    try:
        formatted_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime(date_format)
        return formatted_date
    except ValueError:
        return None

def check_valid_email(email):
    """
    Check if an email address is valid.

    Args:
    - email: str. The email address to check.

    Returns:
    - True if the email is valid, False otherwise.
    """
    # Example simple email validation
    if "@" in email and "." in email:
        return True
    else:
        return False

def convert_to_float(value):
    """
    Convert a value to a float.

    Args:
    - value: str or int or float. The value to convert.

    Returns:
    - Converted float value, or None if conversion fails.
    """
    try:
        float_value = float(value)
        return float_value
    except ValueError:
        return None

def remove_duplicates(data_list):
    """
    Remove duplicates from a list.

    Args:
    - data_list: list. The list to remove duplicates from.

    Returns:
    - List with duplicates removed.
    """
    return list(set(data_list))

def generate_random_number(min_value, max_value):
    """
    Generate a random number within a specified range.

    Args:
    - min_value: int. The minimum value of the range.
    - max_value: int. The maximum value of the range.

    Returns:
    - Random number within the specified range.
    """
    import random
    return random.randint(min_value, max_value)

