from argparse import ArgumentParser
import re
import sys

def parse_address(address_text):
    """
    Parse a US street address from a single line of text.

    Args:
        address_text (str): A single line of text containing a US street address.

    Returns:
        dict: A dictionary containing the parts of the address with the following keys:
            - "house_number"
            - "street"
            - "city"
            - "state"
            - "zip"

    If the regular expression was unsuccessful, return None.
    """
    # Regular expression pattern to match the address components
    address_pattern = r'^(?P<house_number>[\w\s]+?)\s(?P<street>[^,]+?),\s(?P<city>[^,]+)\s(?P<state>[A-Z]{2})\s(?P<zip>\d{5})$'
    
    match = re.search(address_pattern, address_text)
    
    if match:
        return match.groupdict()
    else:
        return None

def parse_addresses(file_path):
    """
    Parse US street addresses from a file and return a list of dictionaries.

    Args:
        file_path (str): The path to a file containing one address per line.

    Returns:
        list: A list of dictionaries, where each dictionary represents a parsed address.

    The file should contain one address per line.
    """
    addresses = []
    
    with open(file_path, 'r') as file:
        for line in file:
            address = parse_address(line.strip())
            if address:
                addresses.append(address)
    
    return addresses

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="File containing one address per line")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in parse_addresses(args.file):
        print(address)




