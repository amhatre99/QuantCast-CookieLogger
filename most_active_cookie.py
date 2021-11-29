import argparse
import logging
from typing import List
from CookieLog import CookieLog

def get_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Return the most active cookie for specified day.")
    parser.add_argument("cookie_log_filename", type=str, help="CSV file with cookies to process")
    parser.add_argument("-d", "--date", type=str, help="Specified date to find most active cookies on", required=True)
    return parser.parse_args()

def main() -> None:
    logging.basicConfig()
    args = get_args()
    file = args.cookie_log_filename

    if args.date:
        logger = CookieLog(file)
        most_active_cookies = logger.most_active_cookie(args.date)
        for cookie in most_active_cookies:
            print(cookie)
    else:
        logging.error("No date argument given. Please choose a date to search on.")

if __name__ == "__main__":
    main()