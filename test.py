import sys
from datetime import datetime
import re

def if_contain_symbol(keyword):
    if re.search(r"\W", keyword):
        return True
    else:
        return False

def map():
    count=0
    for line in sys.stdin:
        print(line)

if __name__ == "__main__":
    map()