import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        reader = csv.DictReader(file)
        return list(reader)
