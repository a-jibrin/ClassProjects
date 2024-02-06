import argparse
import requests
import sys

def get_holidays(country_code, year):
    api_url = f"https://date.nager.at/Api/v1/Get/{country_code}/{year}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        holidays = response.json()
        
        for holiday in holidays:
            date = holiday['date']
            local_name = holiday.get('localName', 'No translation')
            english_name = holiday.get('name', local_name)
            
            print(f"{date}: {english_name}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error finding holidays: {e}")

def parse_args(args):
    parser = argparse.ArgumentParser(description="Get holidays for a country and year.")
    parser.add_argument("country_code", help="Two-letter country code")
    parser.add_argument("year", type=int, help="Four-digit year")
    return parser.parse_args(args)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    get_holidays(args.country_code, args.year)

