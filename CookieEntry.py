import logging
import sys
from datetime import datetime

class CookieEntry:
    def __init__(self, line) -> None:
        self.cookie = line[:-27]
        self.timestamp = None
        try:
            self.timestamp = datetime.fromisoformat(line[-25:])
        except Exception:
            logging.error(f"Input timestamp '{line[-25:]}' is invalid. Timestamp must be in iso format '[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss]'.")
            sys.exit()