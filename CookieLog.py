import sys
import logging
from CookieEntry import CookieEntry
from datetime import datetime
from typing import List, Dict

class CookieLog:
    def __init__(self, cookies_file) -> None:
        self.cookie_entries = []
        try:
            f = open(cookies_file, "r")
            for line in f:
                if line == '\n':
                    print("Warning: empty line in input file")
                else:
                    self.cookie_entries.append(CookieEntry(line.strip()))
            f.close()

            if not self.cookie_entries:
                logging.error(f"Input CSV file: '{cookies_file}' is empty.")
                sys.exit()

        except FileNotFoundError:
            logging.fatal(f"Input CSV file: '{cookies_file}' not found.")
            sys.exit()
    
    def cookies_from_date(self, date) -> List[str]:
        try:
            date = datetime.fromisoformat(date).date()
        except Exception:
            logging.error(f"Input date '{date}' is invalid. Timestamp must be in iso format '[YYYY]-[MM]-[DD]'.")
            sys.exit()
        answer = []
        for cookie_entry in self.cookie_entries:
            if cookie_entry.timestamp.date() == date:
                answer.append(cookie_entry)
        return answer


    def most_active_cookie(self, date) -> List[str]:
        cookie_counter = {}
        for cookie_entry in self.cookies_from_date(date):
            if cookie_entry.cookie in cookie_counter:
                cookie_counter[cookie_entry.cookie] += 1
            else:
                cookie_counter[cookie_entry.cookie] = 1

        if not cookie_counter:
            logging.error(f"No cookies found on input date {date}.")
            sys.exit()
        max_counter = max(cookie_counter.values())
        most_active_cookies = [cookie for cookie in cookie_counter if cookie_counter[cookie] == max_counter]

        return most_active_cookies
    