#!/usr/bin/env python3
"""
Simple implementation of pagination
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Check for index range of items in pages. """
    total = page_size * page
    return total - page_size, total


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        # self.dataset()

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        data = self.dataset()
        # if data:
        start, stop = index_range(page, page_size)
        if start > len(self.__dataset) or stop > len(self.__dataset):
            return []
        return data[start:stop]
        # return []
